from __future__ import annotations
import sys
from pathlib import Path

try:
    import yaml
except ImportError:
    print("Missing dependency: PyYAML\nInstall with: pip install pyyaml")
    sys.exit(1)


# -------------------------------
# Helpers
# -------------------------------

def read_yaml(path: Path) -> dict:
    with path.open("r", encoding="utf-8") as f:
        return yaml.safe_load(f)


def normalize_answer(raw: str) -> str | None:
    raw = raw.strip().lower()
    if raw in ("y", "yes", "true", "1"):
        return "yes"
    if raw in ("n", "no", "false", "0"):
        return "no"
    return None


def prompt_yes_no(prompt: str) -> str:
    while True:
        ans = input(f"{prompt} [y/n]: ")
        norm = normalize_answer(ans)
        if norm:
            return norm
        print("Please enter y / n / yes / no")


def prompt_menu(options: list[dict]) -> str:
    print("\nWhat would you like to do?")
    for i, opt in enumerate(options, 1):
        print(f"  {i}) {opt['label']}")
    while True:
        choice = input("Select option: ").strip()
        if choice.isdigit():
            i = int(choice)
            if 1 <= i <= len(options):
                return options[i - 1]["node"]
        print("Enter a valid number.")


# -------------------------------
# Main flow runner
# -------------------------------

def run_flow(spec: dict) -> None:
    nodes: dict = spec.get("nodes", {})
    node_id: str = spec.get("entry")

    print("\n========================================")
    print(f"{spec.get('title', spec.get('id'))}")
    print("========================================\n")

    # Display policy header
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

        if node.get("help_doc"):
            print(f"Reference: {node['help_doc']}")

        # -------------------------------
        # Question node
        # -------------------------------
        if ntype == "question":
            ans = prompt_yes_no(node.get("prompt", "Answer?"))
            answers = node.get("answers", {})

            # YAML 1.1 safety: True/False can appear
            next_id = answers.get(ans) or answers.get(True if ans == "yes" else False)

            if not next_id:
                print(f"ERROR: No transition for answer '{ans}' from node '{node_id}'.")
                return

            node_id = next_id
            continue

        # -------------------------------
        # Result node
        # -------------------------------
        if ntype == "result":
            print("\nRESULT:\n")
            print(node.get("outcome", "(no outcome text provided)"))

            next_options = node.get("next")
            if next_options:
                node_id = prompt_menu(next_options)
                visited.clear()  # allow re-entry / restart
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
