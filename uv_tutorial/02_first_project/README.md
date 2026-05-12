# Exercise 2 — Your first uv project

Goal: build a small project from scratch using only uv. By the end you'll have a `pyproject.toml`, a `uv.lock`, and a working virtual environment, without ever activating it.

> Work inside this directory. Nothing is pre-populated — you create everything yourself.

## Step 1 — Initialize the project

```console
cd 02_first_project
uv init demo
cd demo
ls -A
```

You should see:

* `pyproject.toml` — project metadata and (so far empty) dependency list
* `.python-version` — the pinned Python version
* `README.md` — a stub
* `main.py` — a one-line example script (older uv versions called this `hello.py`)
* `.gitignore`

No virtual environment yet. uv creates `.venv/` on the first action that needs it.

## Step 2 — Pin a Python version

```console
uv python pin 3.12
```

If 3.12 is not yet on your system, uv downloads a standalone build (this is the equivalent of `conda create -n env python=3.12` or `pyenv install 3.12`).

Inspect:

```console
cat .python-version
uv python list   # shows what's installed and available
```

## Step 3 — Add dependencies

```console
uv add requests 'rich>=13'
```

Watch the output: uv resolves, downloads, installs, and locks all in one step. After it returns:

```console
cat pyproject.toml      # requests and rich now under [project.dependencies]
ls -A                   # .venv/ and uv.lock now exist
```

Add a dev-only dependency (won't ship to runtime users):

```console
uv add --dev pytest
```

Inspect `pyproject.toml` — pytest appears under a dev dependency group, separate from runtime deps.

## Step 4 — Run code inside the env

Replace the contents of `main.py` (or `hello.py` if your uv generated that name) with something that uses the new packages:

```python
import requests
from rich import print

resp = requests.get("https://httpbin.org/json", timeout=10)
print(resp.json())
```

Run it **without activating** the environment:

```console
uv run python main.py
```

That's the workflow you'll use forever: `uv run <command>`. No `source .venv/bin/activate` needed. It works for any executable installed in the env:

```console
uv run python -c "import sys; print(sys.executable)"
uv run pytest --version
```

## Step 5 — Inspect the dependency tree

```console
uv tree
```

This prints the full resolved graph including transitive deps — closer to `pipdeptree` than to `pip list`.

## Step 6 — Remove a dependency

```console
uv remove rich
cat pyproject.toml
uv tree
```

Both `pyproject.toml` and `uv.lock` are updated atomically.

## Step 7 — Upgrade within constraints

```console
uv lock --upgrade
```

This re-resolves dependencies, pulling newer versions that still satisfy the constraints in `pyproject.toml`. Compare `uv.lock` before and after with `git diff` (if you initialized git).

## What you should now understand

* `pyproject.toml` holds constraints; `uv.lock` holds exact pinned versions including hashes.
* `uv add` / `uv remove` are the supported way to change dependencies — editing `pyproject.toml` by hand and re-running `uv sync` works too, but you lose the resolver feedback.
* You never activate the venv; `uv run` is the entry point.
* The whole project is self-contained in this directory and safe to delete.

## Next

Go to [`../03_from_venv/`](../03_from_venv/) to see how to migrate an existing `requirements.txt`-based project.
