# uv tutorial

A hands-on walkthrough of [uv](https://docs.astral.sh/uv/), the Python package and project manager from [Astral](https://astral.sh/). The tutorial is aimed at people who already use `conda` or `venv` + `pip` and want to try uv on real commands rather than just read about it.

If you want the conceptual background before diving in, read [`../uv.md`](../uv.md) first. This directory is the practical companion.

## Prerequisites

* A Unix-like shell (Linux, macOS, or WSL on Windows). The commands also work in PowerShell with minor adjustments.
* Internet access (uv downloads Python interpreters and packages).
* About 200 MB of free disk for the cached interpreter and packages.

You do **not** need an existing Python installation; uv will install one for you in exercise 2.

## Install uv

Recommended way to install on macOS / Linux; note that it will install to `${HOME}/.local/bin`.

```console
curl -LsSf https://astral.sh/uv/install.sh | sh
```
```
curl -LsSf https://astral.sh/uv/install.sh | sh
downloading uv 0.11.13 x86_64-unknown-linux-gnu
installing to ${HOME}/.local/bin
  uv
  uvx
everything's installed!
```

Confirm it works:

```console
uv --version
```
```
uv 0.11.13 (x86_64-unknown-linux-gnu)
```

Any recent release (0.5 or later) covers every command used in this tutorial.

## How to use this tutorial

Work through the exercises in order. Each subdirectory has its own `README.md` with step-by-step commands and "what to look for" notes. Run the commands yourself — copying and pasting is the point.

| # | Directory | What you'll learn |
|---|-----------|-------------------|
| 2 | [`02_first_project/`](02_first_project/) | `uv init`, `uv python pin`, `uv add`, `uv run`, `uv tree` |
| 3 | [`03_from_venv/`](03_from_venv/) | Migrating a `requirements.txt` project to uv |
| 4 | [`04_from_conda/`](04_from_conda/) | Migrating an `environment.yml` project to uv |
| 5 | [`05_reproduce_env/`](05_reproduce_env/) | Reproducing an existing uv project with `uv sync` |
| 6 | [`06_scripts_and_tools/`](06_scripts_and_tools/) | Inline-metadata scripts and CLI tools (`uvx`) |

(Exercise 1 is the install step above, so there is no `01_` directory.)

## Cleanup

Everything uv creates inside an exercise directory (`.venv/`, `uv.lock`, generated `pyproject.toml`) is local to that directory and safe to delete. If you also want to remove uv's global caches and any Python interpreters it installed:

```console
uv cache clean         # delete the package cache
uv python uninstall --all   # remove uv-managed Python interpreters
```

To uninstall uv itself, follow [the official uninstall guide](https://docs.astral.sh/uv/getting-started/installation/#uninstallation).
