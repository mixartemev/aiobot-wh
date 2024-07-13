"""The main entry point used for CLI."""
import sys


def main(args: list[str] = sys.argv) -> None:
    """CLI - The main function called as entry point."""
    return print('args:', args)


if __name__ == "__main__":
    main()
