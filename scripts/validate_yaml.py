import sys
import argparse
from pathlib import Path
from typing import Any, Dict, Set, Tuple, List

import yaml


# ----------------------------
# Output helpers
# ----------------------------

def fail(msg: str) -> None:
    print(f"\n❌ ERROR: {msg}")
    sys.exit(1)

def warn(msg: str) -> None:
    print(f"⚠️  WARN: {msg}")

def ok(msg: str) -> None:
    print(f"✅ {msg}")


# ----------------------------
# YAML loading + normalization
# ----------------------------

def load_yaml(path: Path) -> dict:
    try:
        data = yaml.safe_load(path.read_text(encoding="utf-8"))
    except Exception as e:
        fail(f"Failed to load YAML: {e}")
    if not isinstance(data, dict):
        fail("Top-level YAML must be a mapping/object")
    return data

def normalize_answer_key(k: Any) -> str:
    """
    CHANGE: handle YAML 1.1 boolean coercion (yes/no -> True/False)
    """
    if k is True:
        return "yes"
    if k is False:
        return "no"
    if isinstance(k, str):
        return k.strip().lower()
    return str(k).strip().lower()


# ----------------------------
# Schema helpers
# ----------------------------

def is_nonempty_str(v: Any) -> bool:
    return isinstance(v, str) and bool(v.strip())

def node_is_visible_in_field(node: dict) -> bool:
    """
    CHANGE: field visibility rules for policy lint.
    - If show_in_field is explicitly true => visible
    - If show_in_field explicitly false => not visible
    - Else: visible if it has a field_prompt (because runner can show something)
    """
    if node.get("show_in_field") is True:
        return True
    if node.get("show_in_field") is False:
        return False
    return is_nonempty_str(node.get("field_prompt"))

def node_is_visible_in_workshop(node: dict) -> bool:
    """
    Workshop nodes are generally visible if they have workshop_prompt or prompt.
    """
    return is_nonempty_str(node.get("workshop_prompt")) or is_nonempty_str(node.get("prompt"))


def collect_edges(nodes: Dict[str, dict]) -> List[Tuple[str, str, str]]:
    """
    CHANGE: gather graph edges from:
    - question.answers yes/no
    - result.next menu links
    Returns (src, dst, kind)
    """
    edges: List[Tuple[str, str, str]] = []
    for nid, node in nodes.items():
        ntype = node.get("type")

        if ntype == "question":
            answers = node.get("answers", {})
            if isinstance(answers, dict):
                for raw_k, dst in answers.items():
                    k = normalize_answer_key(raw_k)
                    if isinstance(dst, str) and dst.strip():
                        edges.append((nid, dst.strip(), f"answer:{k}"))

        if ntype == "result":
            nxt = node.get("next")
            if isinstance(nxt, list):
                for opt in nxt:
                    if isinstance(opt, dict):
                        dst = opt.get("node")
                        if isinstance(dst, str) and dst.strip():
                            edges.append((nid, dst.strip(), "next_menu"))

    return edges


def reachable_in_mode(spec: dict, mode: str) -> Tuple[Set[str], List[str]]:
    """
    CHANGE: compute reachable nodes in a specific mode.
    If a visible node points to a non-visible node in that mode, record a "leak".
    """
    nodes: Dict[str, dict] = spec.get("nodes", {})
    entry = spec.get("entry")
    if not isinstance(entry, str) or entry not in nodes:
        return set(), [f"Invalid/missing entry node '{entry}'"]

    def visible(nid: str) -> bool:
        node = nodes[nid]
        if mode == "field":
            return node_is_visible_in_field(node)
        return node_is_visible_in_workshop(node)

    # BFS with leak detection
    leaks: List[str] = []
    seen: Set[str] = set()
    queue: List[str] = []

    # Entry must be visible to start in that mode; if not, that's a leak-by-design.
    if not visible(entry):
        leaks.append(f"Entry node '{entry}' is not visible in {mode} mode.")
        # still traverse so you can see what else is reachable
    queue.append(entry)

    edges = collect_edges(nodes)

    # adjacency
    adj: Dict[str, List[Tuple[str, str]]] = {}
    for s, d, k in edges:
        adj.setdefault(s, []).append((d, k))

    while queue:
        cur = queue.pop(0)
        if cur in seen:
            continue
        seen.add(cur)

        for (dst, kind) in adj.get(cur, []):
            if dst not in nodes:
                continue

            # If current is visible in this mode, but destination is not, flag leak
            if visible(cur) and not visible(dst):
                leaks.append(
                    f"{mode.upper()} leak: '{cur}' ({kind}) -> '{dst}' (not visible in {mode})"
                )

            queue.append(dst)

    return seen, leaks


# ----------------------------
# Main validation
# ----------------------------

def validate(spec: dict, policy_errors: bool = False) -> None:
    # Basic structure
    if "nodes" not in spec:
        fail("Missing top-level 'nodes' key")

    nodes = spec["nodes"]
    if not isinstance(nodes, dict):
        fail("'nodes' must be a mapping/object")

    node_ids = set(nodes.keys())

    # Validate each node
    for node_id, node in nodes.items():
        if not isinstance(node, dict):
            fail(f"Node '{node_id}' must be a mapping/object")

        ntype = node.get("type")
        if ntype not in ("question", "result"):
            fail(f"Node '{node_id}' has invalid or missing type '{ntype}' (must be 'question' or 'result')")

        # CHANGE: prompt schema supports prompt OR field_prompt/workshop_prompt
        if ntype == "question":
            has_any_prompt = any(
                is_nonempty_str(node.get(k))
                for k in ("prompt", "field_prompt", "workshop_prompt")
            )
            if not has_any_prompt:
                fail(
                    f"Question '{node_id}' must contain 'prompt' OR ('field_prompt'/'workshop_prompt')"
                )

            answers = node.get("answers")
            if not isinstance(answers, dict):
                fail(f"Question '{node_id}' missing 'answers' or 'answers' is not a mapping")

            normalized = {}
            for raw_k, target in answers.items():
                k = normalize_answer_key(raw_k)

                if k not in ("yes", "no"):
                    fail(f"Invalid answer '{raw_k}' in '{node_id}'. Only 'yes' or 'no' allowed.")

                if not isinstance(target, str) or not target.strip():
                    fail(f"Answer '{k}' in '{node_id}' must point to a node id string")

                if target not in node_ids:
                    fail(f"'{node_id}' → '{k}' points to unknown node '{target}'")

                normalized[k] = target

            if "yes" not in normalized or "no" not in normalized:
                fail(f"Question '{node_id}' must define BOTH 'yes' and 'no' answers")

            # Optional field visibility sanity
            sif = node.get("show_in_field")
            if sif is not None and not isinstance(sif, bool):
                fail(f"Node '{node_id}': 'show_in_field' must be boolean if present")

        if ntype == "result":
            if not (is_nonempty_str(node.get("outcome")) or is_nonempty_str(node.get("text"))):
                fail(f"Result '{node_id}' must contain 'outcome' (preferred) or 'text'")

            # Validate next menu links
            nxt = node.get("next")
            if nxt is not None:
                if not isinstance(nxt, list):
                    fail(f"Result '{node_id}': 'next' must be a list if present")
                for i, opt in enumerate(nxt, start=1):
                    if not isinstance(opt, dict):
                        fail(f"Result '{node_id}': next[{i}] must be an object")
                    dst = opt.get("node")
                    if not isinstance(dst, str) or not dst.strip():
                        fail(f"Result '{node_id}': next[{i}] missing valid 'node'")
                    if dst not in node_ids:
                        fail(f"Result '{node_id}': next[{i}] points to unknown node '{dst}'")

        # Validate visual_refs type if present
        if "visual_refs" in node:
            vr = node.get("visual_refs")
            if not isinstance(vr, list) or not all(isinstance(x, (str, int, float)) for x in vr):
                fail(f"Node '{node_id}': 'visual_refs' must be a list of simple values (strings preferred)")

        # Validate test_method type if present
        if "test_method" in node:
            tm = node.get("test_method")
            if not is_nonempty_str(tm):
                fail(f"Node '{node_id}': 'test_method' must be a non-empty string if present")

    # CHANGE: policy-aware lints (field/workshop leakage)
    field_reach, field_leaks = reachable_in_mode(spec, "field")
    wk_reach, wk_leaks = reachable_in_mode(spec, "workshop")

    # Workshop leaks are usually less risky, but we still surface them
    # Field leaks matter because they can expose workshop-only procedures
    if field_leaks:
        for m in field_leaks:
            (fail if policy_errors else warn)(m)

    if wk_leaks:
        for m in wk_leaks:
            warn(m)

    ok("YAML logic is valid")


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Validate troubleshooting YAML (supports field_prompt/workshop_prompt + policy-aware lints)."
    )
    parser.add_argument("yaml_file", help="Path to YAML file to validate")
    parser.add_argument(
        "--policy-errors",
        action="store_true",
        help="Treat field/workshop leakage as ERROR instead of WARN (strict mode)."
    )
    args = parser.parse_args()

    path = Path(args.yaml_file)
    if not path.exists():
        fail(f"File not found: {path}")

    spec = load_yaml(path)
    validate(spec, policy_errors=args.policy_errors)


if __name__ == "__main__":
    main()
