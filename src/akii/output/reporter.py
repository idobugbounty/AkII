from collections import defaultdict
from pathlib import Path
import json


def format_findings(target):
    findings = []

    findings.extend(target.get("cors", []))
    findings.extend(target.get("csp", []))

    if not findings:
        return "No issues found.\n"

    grouped = defaultdict(list)

    for finding in findings:
        severity = finding.get("severity", "INFO").upper()
        grouped[severity].append(finding)

    output = []

    output.append("Findings:\n")

    for severity, items in grouped.items():
        output.append(
            f"  {severity:<8} [{len(items)}]\n"
        )

        for item in items:
            name = item.get("header") or item.get("title", "Unknown")
            output.append(f"      - {name}\n")

        output.append("\n")

    return "".join(output)


def txt_output(results, output):
    output_path = Path(output).resolve(strict=False)

    with output_path.open("w", encoding="utf-8") as f:
        for target in results:
            f.write("=" * 60)
            f.write(f"\nTarget: {target['config']['target']}\n\n")

            f.write(format_findings(target))

def serialize_result(result):
    data = {
        "target": result["config"]["target"],
        "error": result.get("error"),
        "cors": result.get("cors", []),
        "csp": result.get("csp", []),
    }

    response = result.get("response")

    if response:
        data["response"] = {
            "status_code": response.status_code,
            "headers": dict(response.headers),
            "url": response.url,
        }
    else:
        data["response"] = None

    return data


def json_output(results, output):
    output_path = Path(output).resolve(strict=False)

    serialized = [
        serialize_result(result)
        for result in results
    ]

    with output_path.open("w", encoding="utf-8") as f:
        json.dump(
            serialized,
            f,
            indent=4,
            ensure_ascii=False
        )
