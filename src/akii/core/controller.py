import re

from akii.output.reporter import json_output, txt_output
from akii.output.terminal import (
    display_findings,
    display_http,
)
from akii.scan.executor import execute


URL_RE = re.compile(r"https?://[^\s]+")


def extract_url(line):
    match = URL_RE.search(line)
    return match.group(0) if match else None


def load_input(config):
    if not config.get("wordlist"):
        return [config]

    configs = []

    with open(config["wordlist"], encoding="utf-8") as f:
        for line in f:
            url = extract_url(line)

            if not url:
                continue

            target_config = config.copy()
            target_config["target"] = url
            configs.append(target_config)

    return configs


def run(config):
    inputs = load_input(config)

    all_results = []

    for result in execute(
        inputs,
        max_workers=config.get("concurrency", 10),
    ):
        all_results.append(result)

        if result["error"]:
            print("=" * 60)
            print(f"Target: {result['config']['target']}")
            print(result["error"])
            print()
            continue

        display_findings(result)

        display_http(
            result["config"],
            result["response"],
        )

    if config.get("output"):
        if config.get("json"):
            json_output(all_results, config["output"])
        else:
            txt_output(all_results, config["output"])
