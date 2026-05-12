# /// script
# requires-python = ">=3.11"
# dependencies = [
#     "rich>=13",
#     "cowsay>=6",
# ]
# ///
"""A standalone script with inline dependency metadata (PEP 723).

Run it with:

    uv run greet.py "your name"

uv will read the metadata block above, build an ephemeral environment with
the listed dependencies, and execute the script — no pyproject.toml required.
"""

import sys

import cowsay
from rich import print


def main() -> None:
    name = sys.argv[1] if len(sys.argv) > 1 else "world"
    cowsay.cow(f"Hello, {name}!")
    print(f"[bold green]Greeted {name} via an ephemeral uv environment.[/bold green]")


if __name__ == "__main__":
    main()
