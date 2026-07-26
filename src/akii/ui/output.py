from akii.ui.banner import get_banner

def banner():
	print(get_banner())
	print("""
- Author: MintTester-IO
- Version: v0.1.0
""")

def display_http(config, response):
	if config.get("request"):
		print("=== Request ===")
		print(f"{response.request.method} {response.request.url}\n")

		for key, value in response.request.headers.items():
			print(f"{key}: {value}")

	if config.get("response"):
		print("\n=== Response ===")
		print(f"Status: {response.status_code}\n")

		for key, value in response.headers.items():
			print(f"{key}: {value}")

	if config.get("verbose"):
		print("=== Request ===")
		print(f"{response.request.method} {response.request.url}\n")

		for key, value in response.request.headers.items():
			print(f"{key}: {value}")

		print("\n=== Response ===")
		print(f"Status: {response.status_code}\n")

		for key, value in response.headers.items():
			print(f"{key}: {value}")