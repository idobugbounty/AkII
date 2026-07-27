from akii.http.client import request
from akii.ui.output import display_http, csp_result, cors_result, display_target
from akii.checks.csp import csp_runner
from akii.checks.cors import cors_runner
from akii.core.reporter import txt_output


def load_input(config):
    if config.get("wordlist"):
        configs = []

        with open(config["wordlist"], encoding="utf-8") as f:
            for line in f:
                target = line.strip()

                if not target:
                    continue

                target_config = config.copy()
                target_config["target"] = target
                configs.append(target_config)

        return configs

    return [config]

def process_target(config):
    display_target(config)

    response = request(config)

    display_http(config, response)

    cors_results = cors_runner(config, response)
    cors_result(cors_results)

    csp_results = csp_runner(config, response)
    csp_result(csp_results)

    return {
        "target": config["target"],
        "cors": cors_results,
        "csp": csp_results,
    }

def run(config):
    inputs = load_input(config)

    all_results = []

    for target_config in inputs:
        all_results.append(process_target(target_config))

    if config.get("output"):
        txt_output(all_results, config["output"])