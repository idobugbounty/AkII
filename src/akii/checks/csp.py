from akii.templates.template_loader import load_template

RULE = load_template("csp")

def csp_detect(config, response):
    findings = {}

    for check in RULE["checks"]:
        header = check["header"]

        if header in response.headers:
            findings[header] = response.headers[header]

    return findings


def csp_analyze(findings):
    results = []

    for check in RULE["checks"]:
        header = check["header"]

        if header not in findings:
            if check.get("required", False):
                results.append({
                    "header": header,
                    "severity": "info",
                    "message": f"Missing required header: {header}",
                })
            continue

        value = findings[header]

        for rule in check.get("rules", []):
            if rule["value"] in value:
                results.append({
                    "header": header,
                    "value": rule["value"],
                    "severity": rule["severity"],
                    "message": rule["message"],
                })

    return results


def csp_runner(config, response):
    findings = csp_detect(config, response)
    return csp_analyze(findings)