import requests
from concurrent.futures import ThreadPoolExecutor

from akii import __version__

def request(config):
    headers = {
    "User-Agent": f"AkII/{__version__}",
    }

    cookies = {}

    if config.get("header"):
        name, value = config["header"].split(":", 1)
        headers[name.strip()] = value.strip()

    if config.get("cookie"):
        name, value = config["cookie"].split("=", 1)
        cookies[name.strip()] = value.strip()

    
    try:
        r = requests.request(
            method=config["method"],
            url=config["target"],
            headers=headers or None,
            cookies=cookies or None,
            data=config.get("data"),
            timeout=config.get("timeout"),
        )
    except requests.RequestException:
        return None

    return r