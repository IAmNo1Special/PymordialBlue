"""Command-line entry point and runtime bootstrap for PymordialBlue."""

import argparse
import logging
import sys

from rich.logging import RichHandler

from pymordialblue.bluestacks_controller import BluestacksController


def setup_logging(verbose: bool = False) -> None:
    """Configures rich console logging handler."""
    logging.basicConfig(
        level="DEBUG" if verbose else "INFO",
        format="%(message)s",
        datefmt="[%X]",
        handlers=[RichHandler(rich_tracebacks=True)],
    )


def main() -> None:
    """Main CLI entry point for pymordialblue."""
    parser = argparse.ArgumentParser(
        prog="pymordialblue",
        description="PymordialBlue: Advanced Automation for BlueStacks using Pymordial",
    )
    parser.add_argument(
        "-v",
        "--verbose",
        action="store_true",
        help="Enable verbose debug logging",
    )
    args = parser.parse_args()

    setup_logging(verbose=args.verbose)

    try:
        controller = BluestacksController()
        logging.info(
            "PymordialBlue controller initialized successfully: %s", controller
        )
    except KeyboardInterrupt:
        print("\nGoodbye.")
        sys.exit(0)


if __name__ == "__main__":
    main()
