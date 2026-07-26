from akii.http.client import request
from akii.ui.output import display_http
from akii.checks.cors import cors_analyze

def run(config):
    response = request(config)
    
    display_http(config, response)

    cors_analyze(config, response)