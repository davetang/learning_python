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
```
main.py
pyproject.toml
.python-version
README.md
```

```console
cat .python-version
```
```
3.10
```

* `pyproject.toml` — project metadata and (so far empty) dependency list
* `.python-version` — the pinned Python version
* `README.md` — a stub
* `main.py` — a one-line example script (older uv versions called this `hello.py`)

No virtual environment yet. uv creates `.venv/` on the first action that needs it.

## Step 2 — Pin a Python version

```console
uv python pin 3.12
```
```
Updated `.python-version` from `3.10` -> `3.12`
```

If 3.12 is not yet on your system, uv downloads a standalone build (this is the equivalent of `conda create -n env python=3.12` or `pyenv install 3.12`).

Inspect:

```console
cat .python-version
```
```
3.12
```

Show what is installed and available.

```console
uv python list
```

## Step 3 — Add dependencies

```console
uv add requests 'rich>=13'
```
```
Using CPython 3.12.13
Creating virtual environment at: .venv
Resolved 10 packages in 163ms
Prepared 9 packages in 107ms
Installed 9 packages in 8ms
 + certifi==2026.4.22
 + charset-normalizer==3.4.7
 + idna==3.14
 + markdown-it-py==4.2.0
 + mdurl==0.1.2
 + pygments==2.20.0
 + requests==2.34.0
 + rich==15.0.0
 + urllib3==2.7.0
```

`uv` resolves, downloads, installs, and locks all in one step. After it returns:

```console
cat pyproject.toml      # requests and rich now under [project.dependencies]
```
```
[project]
name = "demo"
version = "0.1.0"
description = "Add your description here"
readme = "README.md"
requires-python = ">=3.10"
dependencies = [
    "requests>=2.34.0",
    "rich>=13",
]
```

.venv/ and uv.lock now exist.

```console
ls -A
```
```
main.py  pyproject.toml  .python-version  README.md  uv.lock  .venv
```

Add a dev-only dependency (won't ship to runtime users):

```console
uv add --dev pytest
```
```
Resolved 18 packages in 162ms
Prepared 4 packages in 67ms
Installed 4 packages in 6ms
 + iniconfig==2.3.0
 + packaging==26.2
 + pluggy==1.6.0
 + pytest==9.0.3
```

Inspect `pyproject.toml` — pytest appears under a dev dependency group, separate from runtime deps.


```console
cat pyproject.toml
```
```
[project]
name = "demo"
version = "0.1.0"
description = "Add your description here"
readme = "README.md"
requires-python = ">=3.10"
dependencies = [
    "requests>=2.34.0",
    "rich>=13",
]

[dependency-groups]
dev = [
    "pytest>=9.0.3",
]
```

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
```
uv run python main.py
{
    'slideshow': {
        'author': 'Yours Truly',
        'date': 'date of publication',
        'slides': [
            {'title': 'Wake up to WonderWidgets!', 'type': 'all'},
            {'items': ['Why <em>WonderWidgets</em> are great', 'Who <em>buys</em> WonderWidgets'], 'title': 'Overview', 'type': 'all'}
        ],
        'title': 'Sample Slide Show'
    }
}
```

That's the workflow you'll use forever: `uv run <command>`. No `source .venv/bin/activate` needed. It works for any executable installed in the env:

```console
uv run python -c "import sys; print(sys.executable)"
```
```
${HOME}/github/learning_python/uv_tutorial/02_first_project/demo/.venv/bin/python3
```

```console
uv run pytest --version
```
```
pytest 9.0.3
```

## Step 5 — Inspect the dependency tree

```console
uv tree
```
```
Resolved 18 packages in 1ms
demo v0.1.0
├── requests v2.34.0
│   ├── certifi v2026.4.22
│   ├── charset-normalizer v3.4.7
│   ├── idna v3.14
│   └── urllib3 v2.7.0
├── rich v15.0.0
│   ├── markdown-it-py v4.2.0
│   │   └── mdurl v0.1.2
│   └── pygments v2.20.0
└── pytest v9.0.3 (group: dev)
    ├── iniconfig v2.3.0
    ├── packaging v26.2
    ├── pluggy v1.6.0
    └── pygments v2.20.0
```

This prints the full resolved graph including transitive deps; closer to `pipdeptree` than to `pip list`.

## Step 6 — Remove a dependency

```console
uv remove rich
cat pyproject.toml
```
```
[project]
name = "demo"
version = "0.1.0"
description = "Add your description here"
readme = "README.md"
requires-python = ">=3.10"
dependencies = [
    "requests>=2.34.0",
]

[dependency-groups]
dev = [
    "pytest>=9.0.3",
]
```

```console
uv tree
```
```
Resolved 15 packages in 0.85ms
demo v0.1.0
├── requests v2.34.0
│   ├── certifi v2026.4.22
│   ├── charset-normalizer v3.4.7
│   ├── idna v3.14
│   └── urllib3 v2.7.0
└── pytest v9.0.3 (group: dev)
    ├── iniconfig v2.3.0
    ├── packaging v26.2
    ├── pluggy v1.6.0
    └── pygments v2.20.0
```

Both `pyproject.toml` and `uv.lock` are updated atomically.

## Step 7 — Upgrade within constraints

```console
uv lock --upgrade
```
```
Resolved 15 packages in 69ms
```

This re-resolves dependencies, pulling newer versions that still satisfy the constraints in `pyproject.toml`. Compare `uv.lock` before and after with `git diff` (if you initialized git).

## What you should now understand

* `pyproject.toml` holds constraints; `uv.lock` holds exact pinned versions including hashes.
* `uv add` / `uv remove` are the supported way to change dependencies — editing `pyproject.toml` by hand and re-running `uv sync` works too, but you lose the resolver feedback.
* You never activate the venv; `uv run` is the entry point.
* The whole project is self-contained in this directory and safe to delete.

## Next

Go to [`../03_from_venv/`](../03_from_venv/) to see how to migrate an existing `requirements.txt`-based project.
