from akii.http.client import request
from akii.checks.cors import cors_runner
from akii.checks.csp import csp_runner

def scan(config):
    response = request(config)

    if response is None:
        return {
            "target": config["target"],
            "error": "Request failed",
            "response": None,
            "cors": [],
            "csp": [],
        }

    return {
        "target": config["target"],
        "response": response,
        "cors": cors_runner(config, response),
        "csp": csp_runner(config, response),
        "error": None,
    }