"""Hello World CLI — demo project for agentic-workstation.

This is a deliberately simple project designed to demonstrate how
agentic-workstation skills and sub-agents work with a real codebase.
Each feature is added via AI-assisted PRs following the conventions
in AGENTS.md.
"""

import argparse


def create_parser() -> argparse.ArgumentParser:
    """Create the argument parser with all CLI options."""
    parser = argparse.ArgumentParser(
        description="Hello World CLI — agentic-workstation demo",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    parser.add_argument(
        "--name",
        default="World",
        help="Name to greet",
    )
    parser.add_argument(
        "--greeting",
        default="Hello",
        help="Custom greeting word or phrase",
    )
    return parser


def main() -> None:
    """Main entry point: parse arguments and print greeting."""
    parser = create_parser()
    args = parser.parse_args()

    if not args.name.strip():
        parser.error("--name cannot be empty")

    print(f"{args.greeting}, {args.name}!")


if __name__ == "__main__":
    main()
