# Exercise 5 — Reproducing an existing uv project

This directory simulates landing on a colleague's project: a `pyproject.toml` and a script (`hello.py`), and your job is to get the environment running. This is the moment where uv's reproducibility story pays off.

## What's here

* `pyproject.toml` — declares `requests`, `rich`, and a dev-only `pytest`. Requires Python 3.11+.
* `hello.py` — a small script that uses both dependencies.

No `.venv/` and no `uv.lock` yet — those are deliberately omitted so you can generate them.

## Step 1 — Sync

```console
cd 05_reproduce_env
uv sync
```

That single command:

1. Picks (or installs) a compatible Python interpreter.
2. Creates `.venv/` in this directory.
3. Resolves dependencies from `pyproject.toml`.
4. Writes `uv.lock`.
5. Installs everything.

Inspect what was produced:

```console
ls -A
cat uv.lock | head -40
uv tree
```

## Step 2 — Run the script

```console
uv run python hello.py
```

You should see a coloured table printed to the terminal.

## Step 3 — Simulate "another machine"

The whole point of the lock file is that someone else gets bit-for-bit the same environment. To simulate that:

```console
rm -rf .venv          # destroy the env, keep pyproject.toml and uv.lock
uv sync               # rebuild — should be nearly instant
uv run python hello.py
```

This second `uv sync` does **not** re-resolve. It reads `uv.lock` and installs exactly those versions, which is why it's so fast.

## Step 4 — See what `uv sync --frozen` does

`--frozen` refuses to update the lock file under any circumstance — a strong guarantee in CI.

```console
uv sync --frozen
```

Try it after intentionally bumping a constraint in `pyproject.toml` (e.g. `requests>=99`) and watch it fail fast. Revert the change afterwards.

## What you should now understand

* `uv sync` is the one command a new developer needs to fully reproduce the environment.
* On the **first** sync, uv resolves and writes `uv.lock`. On every sync after that, the lock file is the source of truth.
* `uv sync --frozen` is the CI-friendly variant: deterministic or bust.
* Commit both `pyproject.toml` **and** `uv.lock`. Without the lock, you're back to "works on my machine".

## Next

Go to [`../06_scripts_and_tools/`](../06_scripts_and_tools/) for the one-off-script and CLI-tool features that don't need a project at all.
