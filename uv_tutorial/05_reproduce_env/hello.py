"""Tiny demo script that exercises the project's dependencies."""

import requests
from rich import print
from rich.table import Table


def main() -> None:
    resp = requests.get("https://httpbin.org/json", timeout=10)
    payload = resp.json()

    table = Table(title="httpbin /json response")
    table.add_column("key", style="cyan")
    table.add_column("value", style="magenta")
    for key, value in payload.get("slideshow", {}).items():
        table.add_row(str(key), str(value))
    print(table)


if __name__ == "__main__":
    main()
