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
    # CHANGE: Enhanced yes/no prompt for user flow
    """
    Accepts y/n PLUS:
      - 'b' = go back to previous question
      - 'c' = change context (Field <-> Workshop)
      - 'q' = quit
    Returns: 'yes' | 'no' | 'back' | 'change_context' | 'quit'
    """
    while True:
        ans = input(f"{prompt} [y/n, b=back, c=change, q=quit]: ").strip().lower()

        if ans in YES:
            return "yes"
        if ans in NO:
            return "no"
        if ans in ("b", "back"):
            return "back"
        if ans in ("c", "ctx", "context", "change"):
            return "change_context"
        if ans in ("q", "quit", "exit"):
            return "quit"

        print("Please enter y, n, b, c, or q.")


def choose_mode() -> str:
    # CHANGE: Select Field vs Workshop at start
    while True:
        print("Select context:")
        print("  1) Field (fireground)")
        print("  2) Workshop (base/maintenance)")
        choice = input("Choose 1 or 2: ").strip()
        if choice == "1":
            return "field"
        if choice == "2":
            return "workshop"
        print("Please enter 1 or 2.\n")


def _format_test_methods(value: Any) -> str | None:
    """
    Accepts:
      - test_method: str (possibly multi-line)
      - test_methods: list[str]
    Returns a pretty formatted block (string) or None.
    """
    if isinstance(value, str) and value.strip():
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
    Attempts to extract a "Test Method(s)" section from markdown.

    ### Test Method
    ...content...

    Stops at the next heading of same or higher level.
    """
    if not md_path.exists():
        return None

    text = md_path.read_text(encoding="utf-8", errors="replace")

    pattern = re.compile(
        r"(?im)^\s{0,3}#{2,6}\s+Test Method(?:s)?\s*$\n"
        r"(.*?)"
        r"(?=^\s{0,3}#{1,6}\s+|\Z)",
        re.DOTALL,
    )

    m = pattern.search(text)
    if not m:
        return None

    body = m.group(1).strip()
    if not body:
        return None

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


def extract_visual_refs_from_md(md_path: Path) -> str | None:
    if not md_path.exists():
        return None
    text = md_path.read_text(encoding="utf-8", errors="replace")

    pics = sorted(set(re.findall(r"\bPic\s*\d+(?:\.\d+)?\b", text, flags=re.IGNORECASE)))
    diags = sorted(set(re.findall(r"\bDiagram\s*\d+(?:\.\d+)?\b", text, flags=re.IGNORECASE)))

    if not pics and not diags:
        return None

    parts = []
    if pics:
        parts.append("Pics: " + ", ".join(pics))
    if diags:
        parts.append("Diagrams: " + ", ".join(diags))
    return " | ".join(parts)


def get_prompt_for_mode(node: dict, mode: str) -> str:
    # CHANGE: supports field_prompt/workshop_prompt
    if mode == "field":
        return node.get("field_prompt") or node.get("prompt") or "Answer?"
    return node.get("workshop_prompt") or node.get("prompt") or "Answer?"


def should_show_hf_details(node: dict, mode: str) -> bool:
    """
    Human factors gating.
    - Workshop: show details by default
    - Field: hide by default unless node explicitly opts in
    """
    if mode == "workshop":
        return True
    return bool(node.get("show_in_field", False))


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

    # CHANGE: choose global context once at start
    mode = choose_mode()
    print(f"\nContext set to: {mode.upper()}\n")

    # CHANGE: history stack for back navigation
    history: list[str] = []

    while True:
        if node_id not in nodes:
            print(f"\nERROR: Node '{node_id}' not found in YAML.")
            return

        node = nodes[node_id]
        ntype = node.get("type")

        title = node.get("title", node_id)
        print(f"\n--- {title} ---")

        help_doc = node.get("help_doc")
        if help_doc:
            print(f"Reference: {help_doc}")

        # CHANGE: only show test methods / visuals when appropriate
        if help_doc and should_show_hf_details(node, mode):
            md_path = Path(help_doc)

            vr = None
            yaml_vr = node.get("visual_refs")
            if isinstance(yaml_vr, list) and yaml_vr:
                vr = " | ".join(str(x) for x in yaml_vr if str(x).strip())
            else:
                vr = extract_visual_refs_from_md(md_path)

            if vr:
                print(f"Visual refs: {vr}")

        if should_show_hf_details(node, mode):
            test_block = None

            # YAML first, fallback to markdown extraction
            if "test_method" in node:
                test_block = _format_test_methods(node.get("test_method"))
            elif "test_methods" in node:
                test_block = _format_test_methods(node.get("test_methods"))

            if not test_block and help_doc:
                extracted = extract_test_method_from_md(Path(help_doc))
                if extracted:
                    test_block = extracted

            if test_block:
                print("\nTest Method:")
                print(test_block)

        # -------------------------------
        # Question node
        # -------------------------------
        if ntype == "question":
            while True:
                prompt = get_prompt_for_mode(node, mode)
                ans = prompt_yes_no(prompt)

                # CHANGE: runtime controls
                if ans == "quit":
                    print("\nExiting.\n")
                    return

                if ans == "change_context":
                    mode = "workshop" if mode == "field" else "field"
                    print(f"\nContext changed to: {mode.upper()}\n")
                    # Re-render same node with new prompt/details
                    continue

                if ans == "back":
                    if history:
                        node_id = history.pop()
                        print("\n↩ Back\n")
                        break
                    print("No previous step to go back to.")
                    continue

                # Normal yes/no flow
                next_id = node.get("answers", {}).get(ans)
                if not next_id:
                    print(f"ERROR: No transition for answer '{ans}' from node '{node_id}'.")
                    return

                history.append(node_id)  # CHANGE: record where we came from
                node_id = next_id
                break

            continue

        # -------------------------------
        # Result node
        # -------------------------------
        if ntype == "result":
            print("\nRESULT:")
            print(node.get("outcome", node.get("text", "(no outcome text provided)")))

            next_opts = node.get("next")
            if isinstance(next_opts, list) and next_opts:
                while True:
                    print("\nWhat would you like to do?")
                    for i, opt in enumerate(next_opts, start=1):
                        label = opt.get("label", f"Option {i}")
                        print(f"{i}) {label}")
                    raw = input("Select option [number, b=back, c=change, q=quit]: ").strip().lower()

                    # CHANGE: quit / change / back also work in results
                    if raw in ("q", "quit", "exit"):
                        print("\nExiting.\n")
                        return

                    if raw in ("c", "ctx", "context", "change"):
                        mode = "workshop" if mode == "field" else "field"
                        print(f"\nContext changed to: {mode.upper()}\n")
                        # Stay on this result, re-display menu
                        continue

                    if raw in ("b", "back"):
                        if history:
                            node_id = history.pop()
                            print("\n↩ Back\n")
                            break  # break menu loop, continue main loop
                        print("No previous step to go back to.")
                        continue

                    if raw.isdigit():
                        idx = int(raw)
                        if 1 <= idx <= len(next_opts):
                            picked = next_opts[idx - 1]
                            target = picked.get("node")
                            if isinstance(target, str) and target in nodes:
                                history.append(node_id)  # CHANGE: record where we came from
                                node_id = target
                                break
                        print("Invalid option number.")
                        continue

                    print("Please enter a valid option number, b, c, or q.")

                continue  # CHANGE: go back to main loop after result navigation

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
