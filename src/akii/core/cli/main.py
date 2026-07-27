from akii.core.cli.parser import build_parser
from akii.core.controller import run
from akii.ui.output import banner


def main():
    parser = build_parser()
    args = parser.parse_args()

    banner()

    config = vars(args)
    run(config)


if __name__ == "__main__":
    main()