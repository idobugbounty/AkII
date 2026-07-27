import argparse

from akii import __version__
from akii.core.flags.general import (
    INPUT_FLAGS,
    REQUEST_FLAGS,
    #PERFORMANCE_FLAGS,
    OUTPUT_FLAGS,
)


FLAG_GROUPS = (
    ("Input", INPUT_FLAGS),
    ("Request", REQUEST_FLAGS),
    #("Performance", PERFORMANCE_FLAGS),
    ("Output", OUTPUT_FLAGS),
)


def build_parser():
    """Create and configure the CLI argument parser."""

    parser = argparse.ArgumentParser(
        prog="akii",
        description="HTTP header analyzer",
        formatter_class=lambda prog: argparse.HelpFormatter(
            prog,
            max_help_position=50,
            width=130,
        ),
    )

    parser.add_argument(
        "--version",
        action="version",
        version=f"AkII {__version__}",
    )

    # Create and register all argument groups.
    for title, flags in FLAG_GROUPS:
        group = parser.add_argument_group(title)
        register_flags(group, flags)

    return parser


def register_flags(group, flags):
    """Register a collection of CLI flags to an argument group."""

    for value in flags.values():
        kwargs = {
            "help": value["help"],
        }

        # Copy optional keyword arguments if present.
        for key in (
            "action",
            "type",
            "default",
            "choices",
            "nargs",
            "metavar",
            "required",
        ):
            if key in value:
                kwargs[key] = value[key]

        group.add_argument(
            *value["flags"],
            **kwargs,
        )