INPUT_FLAGS = {
    "Target": {
        "flags": ["-T", "--target"],
        "type": str,
        "default": None,
        "help": "Target URL or host to analyze.",
        "metavar": "",
    },

    "Wordlist": {
        "flags": ["-w", "--wordlist"],
        "type": str,
        "default": None,
        "help": "Read targets from a wordlist file.",
        "metavar": "",
    }
}

REQUEST_FLAGS = {
    "Method": {
        "flags": ["-X", "--method"],
        "type": str,
        "default": "GET",
        "help": "HTTP request method (default: GET).",
        "metavar": "",
    },

    "Header": {
        "flags": ["-H", "--header"],
        "type": str,
        "default": None,
        "help": "Add a custom HTTP header (e.g. 'Authorization: Bearer <token>').",
        "metavar": "",
    },

# Disabled until implemented.
#   "Cookie": {
#       "flags": ["-C", "--cookie"],
#       "type": str,
#       "default": None,
#       "help": "Send cookies with the request (e.g. 'session=abc123').",
#       "metavar": "",
#   },

# Disabled until implemented.
#    "Data": {
#        "flags": ["-D", "--data"],
#        "type": str,
#        "default": None,
#        "help": "Send data in the request body.",
#        "metavar": "",
#    },
}

# Disabled until thread-safe output is implemented.
PERFORMANCE_FLAGS = {
    # "Concurrency": {
    #     "flags": ["-c", "--concurrency"],
    #     "type": int,
    #     "default": 1,
    #     "help": "Number of concurrent requests.",
    #     "metavar": "",
    # },
}

OUTPUT_FLAGS = {
    "Output": {
        "flags": ["-o", "--output"],
        "type": str,
        "default": None,
        "help": "Write results to the specified file.",
        "metavar": "",
    },

    "JSON": {
        "flags": ["-j", "--json"],
        "action": "store_true",
        "help": "Output results in JSON format.",
    },

    "Request_Header": {
        "flags": ["--request"],
        "action": "store_true",
        "help": "Display the HTTP request headers.",
    },

    "Response_Header": {
        "flags": ["--response"],
        "action": "store_true",
        "help": "Display the HTTP response headers.",
    },

    "Verbose": {
        "flags": ["--verbose"],
        "action": "store_true",
        "help": "Display both the HTTP request and response.",
    },
}
