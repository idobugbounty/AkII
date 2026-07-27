from akii.ui.banner import get_banner


def banner():
    print(get_banner())


def display_http(config, response):
    if config.get("verbose"):
        print("=== Request ===")
        print(f"{response.request.method} {response.request.url}\n")

        for key, value in response.request.headers.items():
            print(f"{key}: {value}")

        print("\n=== Response ===")
        print(f"Status: {response.status_code}\n")

        for key, value in response.headers.items():
            print(f"{key}: {value}")

        print()
        return

    if config.get("request"):
        print("=== Request ===")
        print(f"{response.request.method} {response.request.url}\n")

        for key, value in response.request.headers.items():
            print(f"{key}: {value}")

        print()

    if config.get("response"):
        print("=== Response ===")
        print(f"Status: {response.status_code}\n")

        for key, value in response.headers.items():
            print(f"{key}: {value}")

        print()


def csp_result(results):
    print("=== CSP Analysis ===")

    if not results:
        print("No CSP issues found.\n")
        return

    for count, result in enumerate(results, start=1):
        print(f"({count}> [{result['severity'].upper()}] {result['header']}")

        if "value" in result:
            print(f"    Value   : {result['value']}")

        print(f"    Message : {result['message']}")

    print()


def cors_result(results):
    print("=== CORS Analysis ===")

    if not results:
        print("No CORS issues found.\n")
        return

    for count, result in enumerate(results, start=1):
        print(f"({count}> [{result['severity'].upper()}] {result['header']}")

        if "value" in result:
            print(f"    Value   : {result['value']}")

        print(f"    Message : {result['message']}")

    print()

def display_target(config):
    print(f"Target: {config['target']}\n")