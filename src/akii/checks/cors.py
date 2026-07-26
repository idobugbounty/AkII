from pathlib import Path
import yaml

template_path = (
    Path(__file__).parent.parent / "templates" / "cors.yaml"
)

with template_path.open("r", encoding="utf-8") as f:
    RULE = yaml.safe_load(f)


def cors_analyze(config, response):
    print("=== CORS Analysis ===")
    print("*** We found something interesting for you! ***")

    count = 0

    for header in RULE["headers"]:
        if header in response.headers:
            count += 1
            print(f"({count}) {header}: {response.headers[header]}")

    if count == 0:
        print("No CORS headers found.")

    if config.get("output"):
        output_path = Path(config["output"]).resolve(strict=False)
        print(f"\n*** The results have been saved to: {output_path}***")