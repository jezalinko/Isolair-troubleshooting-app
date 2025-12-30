import sys
from pathlib import Path
import yaml

def fail(msg: str) -> None:
    print(f"\n❌ ERROR: {msg}")
    sys.exit(1)

def load_yaml(path: Path) -> dict:
    try:
        return yaml.safe_load(path.read_text(encoding="utf-8"))
    except Exception as e:
        fail(f"Failed to load YAML: {e}")

def normalize_answer_key(k):
    # Handle YAML 1.1 weirdness: yes/no become True/False
    if k is True:
        return "yes"
    if k is False:
        return "no"
    if isinstance(k, str):
        return k.strip().lower()
    return k

def validate(spec: dict) -> None:
    if not isinstance(spec, dict):
        fail("Top-level YAML must be a mapping/object")

    if "nodes" not in spec:
        fail("Missing top-level 'nodes' key")

    nodes = spec["nodes"]
    if not isinstance(nodes, dict):
        fail("'nodes' must be a mapping/object")

    node_ids = set(nodes.keys())

    for node_id, node in nodes.items():
        if not isinstance(node, dict):
            fail(f"Node '{node_id}' must be a mapping/object")

        ntype = node.get("type")
        if ntype not in ("question", "result"):
            fail(f"Node '{node_id}' has invalid or missing type '{ntype}' (must be 'question' or 'result')")

        if ntype == "question":
            if "prompt" not in node:
                fail(f"Question '{node_id}' missing 'prompt'")

            answers = node.get("answers")
            if not isinstance(answers, dict):
                fail(f"Question '{node_id}' missing 'answers' or 'answers' is not a mapping")

            normalized = {}
            for raw_k, target in answers.items():
                k = normalize_answer_key(raw_k)

                if k not in ("yes", "no"):
                    fail(f"Invalid answer '{raw_k}' in '{node_id}'. Only 'yes' or 'no' allowed (quote them in YAML).")

                if not isinstance(target, str) or not target.strip():
                    fail(f"Answer '{k}' in '{node_id}' must point to a node id string")

                if target not in node_ids:
                    fail(f"'{node_id}' → '{k}' points to unknown node '{target}'")

                normalized[k] = target

            # Optional: enforce both yes and no exist
            if "yes" not in normalized or "no" not in normalized:
                fail(f"Question '{node_id}' must define BOTH 'yes' and 'no' answers")

        if ntype == "result":
            # accept either outcome or text
            if "outcome" not in node and "text" not in node:
                fail(f"Result '{node_id}' must contain 'outcome' (preferred) or 'text'")

    print("✅ YAML logic is valid")

def main():
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
