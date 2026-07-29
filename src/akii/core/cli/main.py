import sys

from akii.core.cli.parser import build_parser
from akii.core.controller import run
from akii.output.terminal import banner


def main():
    if len(sys.argv) == 1:
        banner()
        return

    parser = build_parser()
    args = parser.parse_args()

    banner()

    try:
        run(vars(args))
    except KeyboardInterrupt:
        print("\nScan interrupted by user.")
        sys.exit(130)


if __name__ == "__main__":
    main()