from collections import defaultdict

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


def display_findings(result):
    findings = []

    findings.extend(result.get("cors", []))
    findings.extend(result.get("csp", []))

    print("=" * 60)
    print(Fore.YELLOW + f"Target: {result['config']['target']}\n")

    if not findings:
        print(Fore.GREEN + "No issues found.\n")
        return

    grouped = defaultdict(list)

    for finding in findings:
        severity = finding.get("severity", "INFO").upper()
        grouped[severity].append(finding)

    print("Findings:")

    for severity, items in grouped.items():
        color = severity_color(severity)

        print(
            f"  {color}{severity:<8}{Style.RESET_ALL} [{len(items)}]"
        )

        for item in items:
            name = item.get("header") or item.get("title", "Unknown")
            print(f"      - {name}")

    print()


def display_target(config):
    print("=" * 60)
    print(Fore.YELLOW + f"Target: {config['target']}\n")
