from pathlib import Path
import json

def txt_output(results, output):
    output_path = Path(output).resolve(strict=False)

    with output_path.open("w", encoding="utf-8") as f:
        for target in results:
            f.write("=" * 60)
            f.write(f"\nTarget: {target['target']}\n\n")

            # CORS
            f.write("=== CORS Analysis ===\n")

            if not target["cors"]:
                f.write("No CORS issues found.\n\n")
            else:
                for count, result in enumerate(target["cors"], start=1):
                    f.write(f"({count}> [{result['severity'].upper()}] {result['header']}\n")

                    if "value" in result:
                        f.write(f"    Value   : {result['value']}\n")

                    f.write(f"    Message : {result['message']}\n")

                f.write("\n")

            # CSP
            f.write("=== CSP Analysis ===\n")

            if not target["csp"]:
                f.write("No CSP issues found.\n\n")
            else:
                for count, result in enumerate(target["csp"], start=1):
                    f.write(f"({count}> [{result['severity'].upper()}] {result['header']}\n")

                    if "value" in result:
                        f.write(f"    Value   : {result['value']}\n")

                    f.write(f"    Message : {result['message']}\n")

                f.write("\n")

def json_output(results, output):
    output_path = Path(output).resolve(strict=False)

    with output_path.open("w", encoding="utf-8") as f:
        json.dump(results, f, indent=4, ensure_ascii=False)