# Exercise 3 — Migrating from venv + pip

You inherit a project that ships a `requirements.txt`. This directory contains a small example:

```
requests>=2.31
rich>=13
python-dateutil>=2.8
```

There are two reasonable migration paths. Try both.

## Path A — Drop-in pip replacement (lowest effort)

Keep `requirements.txt`, just install faster.

```console
cd 03_from_venv
uv venv                                   # like python -m venv .venv (uses the pinned Python if set)
uv pip install -r requirements.txt        # like pip install -r ...
```

Notice:

* `uv venv` created `.venv/` in this directory.
* Installation is dramatically faster than `pip` (try it again after `rm -rf .venv` to feel the cached re-install).
* No `pyproject.toml`, no `uv.lock`. You have not changed the project's shape, only the tool that materializes the environment.

To run code:

```console
uv run python -c "import requests, rich, dateutil; print('ok')"
```

If you want to regenerate a pinned `requirements.txt` from a looser `requirements.in`, this is the `pip-compile` analogue:

```console
echo "requests>=2.31" > requirements.in
uv pip compile requirements.in -o requirements.txt
```

This path is great for CI and legacy projects. You get speed and that's it.

## Path B — Graduate to a uv-native project (recommended for new work)

Now convert the same dependencies into a real uv project so you get the lock file too. We scaffold into a subdirectory (`uv_project`) because Python package names can't start with a digit, so `uv init .` inside `03_from_venv/` would reject the dir name.

```console
rm -rf .venv                              # start clean
uv init --no-readme uv_project            # scaffold pyproject.toml in uv_project/
cd uv_project
uv python pin 3.12
uv add requests 'rich>=13' python-dateutil
```

Compare:

```console
cat pyproject.toml
ls uv.lock
```

You now have:

* `pyproject.toml` — single source of truth for declared deps.
* `uv.lock` — cross-platform resolved versions with hashes.

You can delete `requirements.txt` once you're satisfied. Anyone else can reproduce the env with a single `uv sync` (you'll do this in exercise 5).

## What you should now understand

* If you only want speed, `uv venv` + `uv pip install -r requirements.txt` is enough.
* If you want reproducibility guarantees, the migration to `pyproject.toml` + `uv.lock` takes about three commands.
* `uv pip` is a compatibility shim. Use it for legacy workflows; use `uv add` / `uv sync` for new work.

## Next

Go to [`../04_from_conda/`](../04_from_conda/) to see the conda → uv migration.
