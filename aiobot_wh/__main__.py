"""The main entry point used for CLI."""
import sys
from typing import Sequence


def main(args: Sequence[str] | None = None) -> None:
    """CLI - The main function called as entry point."""
    return print('args:', args)


if __name__ == "__main__":
    sys.exit(main())
