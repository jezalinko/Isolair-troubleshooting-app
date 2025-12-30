from __future__ import annotations

import sys
from pathlib import Path

try:
    import yaml  # type: ignore
except ImportError:
    print("Missing dependency: PyYAML\nInstall with: pip install pyyaml")
    sys.exit(1)


def read_yaml(path: Path) -> dict:
    with path.open("r", encoding="utf-8") as f:
        return yaml.safe_load(f)


def prompt_yes_no(prompt: str) -> str:
    while True:
        ans = input(f"{prompt} [y/n]: ").strip().lower()
        if ans in ("y", "yes"):
            return "yes"
        if ans in ("n", "no"):
            return "no"
        print("Please enter y or n.")


def run_flow(spec: dict) -> None:
    nodes: dict = spec.get("nodes", {})
    node_id: str = spec.get("entry")

    print("\n========================================")
    print(f"{spec.get('title', spec.get('id'))}")
    print("========================================\n")

    policy = spec.get("policy", {})
    if policy:
        print("Policy:")
        if policy.get("supported_aircraft"):
            print(f"  - Supported aircraft: {', '.join(policy['supported_aircraft'])}")
        if policy.get("deprecated_components"):
            print(f"  - Deprecated components: {', '.join(policy['deprecated_components'])}")
        field = policy.get("field_procedure", {})
        if field.get("cyclic_controller"):
            print(f"  - Field procedure: {field['cyclic_controller']}")
        print("")

    visited = set()

    while True:
        if node_id not in nodes:
            print(f"\nERROR: Node '{node_id}' not found in YAML.")
            return

        if node_id in visited:
            print(f"\nERROR: Detected loop at node '{node_id}'. Check YAML transitions.")
            return
        visited.add(node_id)

        node = nodes[node_id]
        ntype = node.get("type")

        title = node.get("title", node_id)
        print(f"\n--- {title} ---")

        help_doc = node.get("help_doc")
        if help_doc:
            print(f"Reference: {help_doc}")

        if ntype == "question":
            ans = prompt_yes_no(node.get("prompt", "Answer?"))
            next_id = node.get("answers", {}).get(ans)
            if not next_id:
                print(f"ERROR: No transition for answer '{ans}' from node '{node_id}'.")
                return
            node_id = next_id
            continue

        if ntype == "result":
            print("\nRESULT:")
            print(node.get("outcome", "(no outcome text provided)"))
            print("\nDone.\n")
            return

        print(f"ERROR: Unknown node type '{ntype}' in node '{node_id}'.")
        return


def main() -> None:
    # Default path; can override with CLI arg.
    yaml_path = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("docs/logic/snorkel_pump_wont_operate.yaml")
    if not yaml_path.exists():
        print(f"YAML not found: {yaml_path}")
        sys.exit(1)

    spec = read_yaml(yaml_path)
    run_flow(spec)


if __name__ == "__main__":
    main()
