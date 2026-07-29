from colorama import Fore, Style, init

from akii.output.banner import get_banner

init(autoreset=True)


def severity_color(severity):
    severity = severity.upper()

    if severity == "CRITICAL":
        return Fore.LIGHTRED_EX
    if severity == "HIGH":
        return Fore.RED
    if severity == "MEDIUM":
        return Fore.YELLOW
    if severity == "LOW":
        return Fore.GREEN
    if severity == "INFO":
        return Fore.BLUE

    return Fore.WHITE


def banner():
    print(get_banner())


def display_http(config, response):
    if config.get("verbose"):
        print(Fore.CYAN + "=== Request ===")
        print(f"{response.request.method} {response.request.url}\n")

        for key, value in response.request.headers.items():
            print(f"{Fore.GREEN}{key}{Style.RESET_ALL}: {value}")

        print(Fore.CYAN + "\n=== Response ===")
        print(f"Status: {response.status_code}\n")

        for key, value in response.headers.items():
            print(f"{Fore.GREEN}{key}{Style.RESET_ALL}: {value}")

        print()
        return

    if config.get("request"):
        print(Fore.CYAN + "=== Request ===")
        print(f"{response.request.method} {response.request.url}\n")

        for key, value in response.request.headers.items():
            print(f"{Fore.GREEN}{key}{Style.RESET_ALL}: {value}")

        print()

    if config.get("response"):
        print(Fore.CYAN + "=== Response ===")
        print(f"Status: {response.status_code}\n")

        for key, value in response.headers.items():
            print(f"{Fore.GREEN}{key}{Style.RESET_ALL}: {value}")

        print()


def csp_result(results):
    print(Fore.CYAN + "=== CSP Analysis ===")

    if not results:
        print(Fore.GREEN + "No CSP issues found.\n")
        return

    for count, result in enumerate(results, start=1):
        color = severity_color(result["severity"])

        print(f"({count}> {color}[{result['severity'].upper()}]{Style.RESET_ALL} {result['header']}")

        if "value" in result:
            print(f"    {Fore.GREEN}Value{Style.RESET_ALL}   : {result['value']}")

        print(f"    {Fore.GREEN}Message{Style.RESET_ALL} : {result['message']}")

    print()


def cors_result(results):
    print(Fore.CYAN + "=== CORS Analysis ===")

    if not results:
        print(Fore.GREEN + "No CORS issues found.\n")
        return

    for count, result in enumerate(results, start=1):
        color = severity_color(result["severity"])

        print(f"({count}> {color}[{result['severity'].upper()}]{Style.RESET_ALL} {result['header']}")

        if "value" in result:
            print(f"    {Fore.GREEN}Value{Style.RESET_ALL}   : {result['value']}")

        print(f"    {Fore.GREEN}Message{Style.RESET_ALL} : {result['message']}")

    print()


def display_target(config):
    print("=" * 60)
    print(Fore.YELLOW + f"Target: {config['target']}\n")