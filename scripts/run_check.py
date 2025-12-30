from __future__ import annotations

import sys
import re
from pathlib import Path
from typing import Any

try:
    import yaml  # type: ignore
except ImportError:
    print("Missing dependency: PyYAML\nInstall with: pip install pyyaml")
    sys.exit(1)


YES = {"y", "yes"}
NO = {"n", "no"}

# -------------------------------
# Helpers
# -------------------------------


def read_yaml(path: Path) -> dict:
    with path.open("r", encoding="utf-8") as f:
        data = yaml.safe_load(f)
    if not isinstance(data, dict):
        raise ValueError("Top-level YAML must be a mapping/object")
    return data


def prompt_yes_no(prompt: str) -> str:
    while True:
        ans = input(f"{prompt} [y/n]: ").strip().lower()
        if ans in YES:
            return "yes"
        if ans in NO:
            return "no"
        print("Please enter y or n.")


def _format_test_methods(value: Any) -> str | None:
    """
    Accepts:
      - test_method: str (possibly multi-line)
      - test_methods: list[str]
    Returns a pretty formatted block (string) or None.
    """
    if isinstance(value, str) and value.strip():
        # If it's already bullet-y, keep it. Otherwise, indent it nicely.
        lines = [ln.rstrip() for ln in value.strip().splitlines()]
        return "\n".join(lines)

    if isinstance(value, list) and value:
        parts: list[str] = []
        for item in value:
            if isinstance(item, str) and item.strip():
                parts.append(f"- {item.strip()}")
        return "\n".join(parts) if parts else None

    return None


def extract_test_method_from_md(md_path: Path) -> str | None:
    """
    Attempts to extract a "Test Method(s)" section from markdown, like:

    ### Test Method
    ...content...

    Stops at the next heading of same or higher level.
    """
    if not md_path.exists():
        return None

    text = md_path.read_text(encoding="utf-8", errors="replace")

    # Match headings like "### Test Method" or "### Test Methods"
    # Capture content until next heading (## or ### or # etc).
    pattern = re.compile(
        r"(?im)^\s{0,3}#{2,6}\s+Test Method(?:s)?\s*$\n"  # heading line
        r"(.*?)"                                        # content
        r"(?=^\s{0,3}#{1,6}\s+|\Z)",                     # next heading or EOF
        re.DOTALL,
    )

    m = pattern.search(text)
    if not m:
        return None

    body = m.group(1).strip()
    if not body:
        return None

    # Clean up excessive blank lines
    body = re.sub(r"\n{3,}", "\n\n", body).strip()
    return body


def print_policy(spec: dict) -> None:
    policy = spec.get("policy", {})
    if not policy:
        return

    print("Policy:")
    if policy.get("supported_aircraft"):
        print(f"  - Supported aircraft: {', '.join(policy['supported_aircraft'])}")
    if policy.get("deprecated_components"):
        print(f"  - Deprecated components: {', '.join(policy['deprecated_components'])}")

    field = policy.get("field_procedure", {})
    if isinstance(field, dict) and field.get("cyclic_controller"):
        print(f"  - Field procedure: {field['cyclic_controller']}")

    print("")

# Helper to extract visual references (Pics/Diagrams) from markdown

def extract_visual_refs_from_md(md_path: Path) -> str | None:
    if not md_path.exists():
        return None
    text = md_path.read_text(encoding="utf-8", errors="replace")

    pics = sorted(set(re.findall(r"\bPic\s*\d+\b", text, flags=re.IGNORECASE)))
    diags = sorted(set(re.findall(r"\bDiagram\s*\d+(?:\.\d+)?\b", text, flags=re.IGNORECASE)))

    if not pics and not diags:
        return None

    parts = []
    if pics:
        parts.append("Pics: " + ", ".join(pics))
    if diags:
        parts.append("Diagrams: " + ", ".join(diags))
    return " | ".join(parts)



# -------------------------------
# Main flow runner
# -------------------------------

def run_flow(spec: dict) -> None:
    nodes: dict = spec.get("nodes", {})
    node_id: str = spec.get("entry")

    print("\n========================================")
    print(f"{spec.get('title', spec.get('id'))}")
    print("========================================\n")

    print_policy(spec)

    visited = set()

    while True:
        if node_id not in nodes:
            print(f"\nERROR: Node '{node_id}' not found in YAML.")
            return

        # NOTE: you *want* to allow intentional loops (Start Over).
        # So only block immediate infinite recursion due to bad wiring:
        # Allow revisits, but warn if it gets crazy (optional).
        # For now: do NOT hard-fail on revisits.
        visited.add(node_id)

        node = nodes[node_id]
        ntype = node.get("type")

        title = node.get("title", node_id)
        print(f"\n--- {title} ---")

        help_doc = node.get("help_doc")
        if help_doc:
            print(f"Reference: {help_doc}")

        #✅ Visual references extraction for future proofing GUI will work with CLI too

        vr = extract_visual_refs_from_md(Path(help_doc))
        if vr:
            print(f"Visual refs: {vr}")


        # ✅ Show test methods (YAML first, fallback to markdown extraction)
        test_block = None

        if "test_method" in node:
            test_block = _format_test_methods(node.get("test_method"))
        elif "test_methods" in node:
            test_block = _format_test_methods(node.get("test_methods"))

        if not test_block and help_doc:
            md_path = Path(help_doc)
            extracted = extract_test_method_from_md(md_path)
            if extracted:
                test_block = extracted

        if test_block:
            print("\nTest Method:")
            # If it already contains bullet lines, print as-is; otherwise indent slightly.
            print(test_block)

        # -------------------------------
        # Question node
        # -------------------------------

        if ntype == "question":
            ans = prompt_yes_no(node.get("prompt", "Answer?"))
            next_id = node.get("answers", {}).get(ans)
            if not next_id:
                print(f"ERROR: No transition for answer '{ans}' from node '{node_id}'.")
                return
            node_id = next_id
            continue

        # -------------------------------
        # Result node
        # -------------------------------

        if ntype == "result":
            print("\nRESULT:")
            print(node.get("outcome", node.get("text", "(no outcome text provided)")))

            # Optional menu-style "next" support (your YAML already uses this)
            next_opts = node.get("next")
            if isinstance(next_opts, list) and next_opts:
                print("\nWhat would you like to do?")
                for i, opt in enumerate(next_opts, start=1):
                    label = opt.get("label", f"Option {i}")
                    print(f"{i}) {label}")

                while True:
                    raw = input("Select option: ").strip()
                    if raw.isdigit():
                        idx = int(raw)
                        if 1 <= idx <= len(next_opts):
                            picked = next_opts[idx - 1]
                            target = picked.get("node")
                            if isinstance(target, str) and target in nodes:
                                node_id = target
                                break
                    print("Please enter a valid option number.")
                continue

            print("\nDone.\n")
            return

        print(f"ERROR: Unknown node type '{ntype}' in node '{node_id}'.")
        return
    
# -------------------------------
# Entrypoint
# -------------------------------

def main() -> None:
    yaml_path = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("docs/logic/snorkel_pump_wont_operate.yaml")
    if not yaml_path.exists():
        print(f"YAML not found: {yaml_path}")
        sys.exit(1)

    spec = read_yaml(yaml_path)
    run_flow(spec)


if __name__ == "__main__":
    main()
