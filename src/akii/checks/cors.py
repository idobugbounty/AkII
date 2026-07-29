from akii.templates.template_loader import load_template

RULE = load_template("cors")

def cors_detect(config, response):
    findings = {}

    for check in RULE["checks"]:
        header = check["header"]

        if header in response.headers:
            findings[header] = response.headers[header]
            
    return findings


def cors_analyze(findings):
    results = []

    for check in RULE["checks"]:
        header = check["header"]

        if header not in findings:
            continue

        value = findings[header]

        for rule in check.get("rules", []):
            if value == rule["value"]:
                results.append({
                    "header": header,
                    "value": value,
                    "severity": rule["severity"],
                    "message": rule["message"],
                })

    return results


def cors_runner(config, response):
    findings = cors_detect(config, response)
    return cors_analyze(findings)