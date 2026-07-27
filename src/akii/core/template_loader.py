from importlib.resources import files
import yaml


def load_template(name: str) -> dict:
    template = files("akii.templates").joinpath(f"{name}.yaml")
    return yaml.safe_load(template.read_text(encoding="utf-8"))