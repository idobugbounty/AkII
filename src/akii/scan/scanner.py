from akii.http.client import request
from akii.checks.cors import cors_runner
from akii.checks.csp import csp_runner

def scan(config):
    response = request(config)

    if response is None:
        return {
            "config": config,
            "error": "Failed to receive HTTP response.",
            "response": None,
            "cors": [],
            "csp": [],
        }

    return {
        "config": config,
        "error": None,
        "response": response,
        "cors": cors_runner(config, response),
        "csp": csp_runner(config, response),
    }
