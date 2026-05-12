# Exercise 6 — Standalone scripts and CLI tools

Not every Python task deserves a project. uv has two features for the "I just want to run something" case.

## Part A — Inline-metadata scripts (PEP 723)

Open `greet.py`. Notice the comment block at the top:

```python
# /// script
# requires-python = ">=3.11"
# dependencies = [
#     "rich>=13",
#     "cowsay>=6",
# ]
# ///
```

This is [PEP 723](https://peps.python.org/pep-0723/) inline metadata. uv reads it, builds an **ephemeral** environment that satisfies it, and runs the script — without you creating a venv, a `pyproject.toml`, or anything else.

Run it:

```console
cd 06_scripts_and_tools
uv run greet.py "uv"
```

Try changing the name:

```console
uv run greet.py "your name"
```

The first run installs `rich` and `cowsay` into a cached environment; subsequent runs reuse it and are effectively instant.

This is perfect for:

* One-off automation scripts you share over Slack or email.
* `~/bin/` scripts that need a couple of pinned dependencies.
* Replacing the "create a venv just to run this once" friction.

## Part B — Running CLI tools ephemerally with `uvx`

`uvx` is the rough equivalent of `pipx run`. It runs a CLI tool in an ephemeral environment without polluting your project or your global Python.

```console
uvx ruff --version
uvx ruff check .
uvx --from black==24.10.0 black --version
```

The `--from` flag lets you pin the tool's version (or specify a different package than the command name).

## Part C — Installing a tool persistently

If you use a tool often, install it globally so you don't pay the ephemeral-resolve cost each time. The tool's environment is still isolated; it's just kept around.

```console
uv tool install ruff
uv tool list
ruff --version       # now on your PATH directly
uv tool upgrade ruff
uv tool uninstall ruff
```

This is the `pipx install` analogue.

## What you should now understand

* **One-off script with deps?** PEP 723 inline metadata + `uv run script.py`.
* **One-off CLI tool?** `uvx <tool>` — no install.
* **Frequent CLI tool?** `uv tool install <tool>` — global, isolated.
* None of these require or interact with a project's `pyproject.toml` or `.venv/`.

## You're done

You now have hands-on experience with the full uv surface: projects, migrations, reproduction, and standalone scripts. From here, the [official docs](https://docs.astral.sh/uv/) are organized the same way and will feel familiar.
