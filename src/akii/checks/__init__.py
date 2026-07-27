from .cors import cors_runner
from .csp import csp_runner

CHECKERS = [
    cors_runner,
    csp_runner,
]