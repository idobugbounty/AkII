from pathlib import Path
import yaml

TEMPLATE_DIR = Path(__file__).parent.parent / "templates"

def load_template(name: str) -> dict:
    template_path = TEMPLATE_DIR / f"{name}.yaml"

    with template_path.open("r", encoding="utf-8") as f:
        return yaml.safe_load(f)
