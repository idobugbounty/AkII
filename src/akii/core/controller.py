import re
from concurrent.futures import ThreadPoolExecutor

from akii.http.client import request
from akii.output.terminal import display_http, csp_result, cors_result, display_target
from akii.checks.csp import csp_runner
from akii.checks.cors import cors_runner
from akii.output.reporter import txt_output, json_output
from akii.scan.scanner import scan


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

def process_target(config):
    result = scan(config)

    display_target(config)

    if result["error"]:
        print(result["error"])
        return result

    display_http(config, result["response"])
    cors_result(result["cors"])
    csp_result(result["csp"])

    return result


def run(config):
    inputs = load_input(config)

    all_results = []

    for target_config in inputs:
        all_results.append(process_target(target_config))

    if config.get("output"):
        if config.get("json"):
            json_output(all_results, config["output"])
        else:
            txt_output(all_results, config["output"])