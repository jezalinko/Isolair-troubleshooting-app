from __future__ import annotations

import sys
from pathlib import Path
from typing import Any, Dict, Set, List

try:
    import yaml  # type: ignore
except ImportError:
    print("Missing dependency: PyYAML\nInstall with: pip install pyyaml")
    sys.exit(1)


def fail(msg: str) -> None:
    print(f"\n❌ ERROR: {msg}")
    sys.exit(1)


def load_yaml(path: Path) -> dict:
    try:
        return yaml.safe_load(path.read_text(encoding="utf-8"))
    except Exception as e:
        fail(f"Failed to load YAML: {e}")


def normalize_answer_key(k: Any) -> Any:
    # Handle YAML 1.1 weirdness: yes/no become True/False
    if k is True:
        return "yes"
    if k is False:
        return "no"
    if isinstance(k, str):
        return k.strip().lower()
    return k


def validate_entry(spec: dict, node_ids: Set[str]) -> None:
    entry = spec.get("entry")
    if not isinstance(entry, str) or not entry.strip():
        fail("Missing or invalid top-level 'entry' (must be a node id string)")
    if entry not in node_ids:
        fail(f"Top-level 'entry' points to unknown node '{entry}'")


def validate_question(node_id: str, node: dict, node_ids: Set[str]) -> None:
    if "prompt" not in node or not isinstance(node.get("prompt"), str) or not node["prompt"].strip():
        fail(f"Question '{node_id}' missing or invalid 'prompt'")

    answers = node.get("answers")
    if not isinstance(answers, dict):
        fail(f"Question '{node_id}' missing 'answers' or 'answers' is not a mapping")

    normalized: Dict[str, str] = {}
    for raw_k, target in answers.items():
        k = normalize_answer_key(raw_k)

        if k not in ("yes", "no"):
            fail(
                f"Invalid answer key '{raw_k}' in '{node_id}'. "
                "Only 'yes' or 'no' allowed (quote them in YAML: \"yes\" / \"no\")."
            )

        if not isinstance(target, str) or not target.strip():
            fail(f"Answer '{k}' in '{node_id}' must point to a node id string")

        if target not in node_ids:
            fail(f"'{node_id}' → '{k}' points to unknown node '{target}'")

        normalized[k] = target

    # Enforce both yes and no exist
    if "yes" not in normalized or "no" not in normalized:
        fail(f"Question '{node_id}' must define BOTH 'yes' and 'no' answers")


def validate_result(node_id: str, node: dict, node_ids: Set[str]) -> None:
    if "outcome" not in node and "text" not in node:
        fail(f"Result '{node_id}' must contain 'outcome' (preferred) or 'text'")

    nxt = node.get("next")
    if nxt is None:
        return

    if not isinstance(nxt, list):
        fail(f"Result '{node_id}' has 'next' but it is not a list")

    for i, item in enumerate(nxt, 1):
        if not isinstance(item, dict):
            fail(f"Result '{node_id}' next[{i}] must be a mapping with keys 'label' and 'node'")

        label = item.get("label")
        target = item.get("node")

        if not isinstance(label, str) or not label.strip():
            fail(f"Result '{node_id}' next[{i}] missing/invalid 'label'")

        if not isinstance(target, str) or not target.strip():
            fail(f"Result '{node_id}' next[{i}] missing/invalid 'node' target")

        if target not in node_ids:
            fail(f"Result '{node_id}' next[{i}] points to unknown node '{target}'")


def build_graph(spec: dict) -> Dict[str, Set[str]]:
    """Build adjacency list of node transitions for reachability checks."""
    nodes = spec["nodes"]
    graph: Dict[str, Set[str]] = {nid: set() for nid in nodes.keys()}

    for nid, node in nodes.items():
        ntype = node.get("type")
        if ntype == "question":
            answers = node.get("answers", {})
            for _, target in answers.items():
                if isinstance(target, str):
                    graph[nid].add(target)
        elif ntype == "result":
            nxt = node.get("next")
            if isinstance(nxt, list):
                for item in nxt:
                    if isinstance(item, dict) and isinstance(item.get("node"), str):
                        graph[nid].add(item["node"])

    return graph


def reachable_from(entry: str, graph: Dict[str, Set[str]]) -> Set[str]:
    seen: Set[str] = set()
    stack: List[str] = [entry]
    while stack:
        cur = stack.pop()
        if cur in seen:
            continue
        seen.add(cur)
        for nxt in graph.get(cur, set()):
            if nxt not in seen:
                stack.append(nxt)
    return seen


def validate(spec: dict) -> None:
    if not isinstance(spec, dict):
        fail("Top-level YAML must be a mapping/object")

    if "nodes" not in spec:
        fail("Missing top-level 'nodes' key")

    nodes = spec["nodes"]
    if not isinstance(nodes, dict):
        fail("'nodes' must be a mapping/object")

    node_ids = set(nodes.keys())
    validate_entry(spec, node_ids)

    # Per-node validation
    for node_id, node in nodes.items():
        if not isinstance(node, dict):
            fail(f"Node '{node_id}' must be a mapping/object")

        ntype = node.get("type")
        if ntype not in ("question", "result"):
            fail(f"Node '{node_id}' has invalid or missing type '{ntype}' (must be 'question' or 'result')")

        if ntype == "question":
            validate_question(node_id, node, node_ids)

        if ntype == "result":
            validate_result(node_id, node, node_ids)

    # Reachability check (warn or fail)
    entry = spec["entry"]
    graph = build_graph(spec)
    reachable = reachable_from(entry, graph)
    unreachable = sorted(node_ids - reachable)

    if unreachable:
        # I recommend failing to keep logic tidy early on.
        # If you want warnings only, change fail(...) to print(...)
        fail(
            "Unreachable node(s) detected from entry. Remove them or connect them:\n"
            + "\n".join(f"  - {nid}" for nid in unreachable)
        )

    print("✅ YAML logic is valid")


def main() -> None:
    if len(sys.argv) != 2:
        print("Usage: python scripts/validate_yaml.py <yaml-file>")
        sys.exit(1)

    path = Path(sys.argv[1])
    if not path.exists():
        fail(f"File not found: {path}")

    spec = load_yaml(path)
    validate(spec)


if __name__ == "__main__":
    main()
