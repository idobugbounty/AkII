from unittest.mock import patch

from akii.controller import run


class FakeResponse:
    def __init__(self, headers):
        self.headers = headers


class BrokenResponse:
    pass


def fake_scan_none(config):
    return {
        "error": None,
        "response": None,
        "cors": [],
        "csp": []
    }


def fake_scan_missing_headers(config):
    return {
        "error": None,
        "response": BrokenResponse(),
        "cors": [],
        "csp": []
    }


def fake_scan_invalid_headers(config):
    return {
        "error": None,
        "response": FakeResponse({
            "Access-Control-Allow-Origin": None,
            "Access-Control-Allow-Credentials": "",
            "Random": 123
        }),
        "cors": [],
        "csp": []
    }


def run_test(name, fake_scan):
    print(f"\n===== {name} =====")

    config = {
        "target": "https://example.com"
    }

    with patch("akii.controller.scan", fake_scan):
        try:
            run(config)
            print("PASS: no crash")

        except Exception as e:
            print("CRASH:")
            print(type(e).__name__, e)


run_test(
    "Test None response",
    fake_scan_none
)

run_test(
    "Test missing headers object",
    fake_scan_missing_headers
)

run_test(
    "Test invalid headers",
    fake_scan_invalid_headers
)
