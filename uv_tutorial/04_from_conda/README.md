# Exercise 4 — Migrating from conda

The starting point is a typical bioinformatics-flavoured `environment.yml`:

```yaml
name: scrnaseq
channels: [conda-forge, bioconda]
dependencies:
  - python=3.12
  - pandas>=2,<3
  - numpy>=1.26
  - scanpy>=1.10
  - jupyterlab
  - samtools           # non-Python
  - bcftools           # non-Python
  - pip
  - pip:
    - anndata>=0.10
```

uv is **Python-only**. The migration is mechanical but you have to make one decision: what to do with the non-Python tools.

## Step 1 — Triage the dependency list

Split the entries into three groups:

| Group | Examples here | Where it goes |
|-------|---------------|---------------|
| Python interpreter | `python=3.12` | `uv python pin 3.12` |
| Python packages | `pandas`, `numpy`, `scanpy`, `jupyterlab`, `anndata` | `uv add ...` |
| Non-Python tools | `samtools`, `bcftools` | **Not** uv. Install via system package manager, a side conda env, or [`pixi`](https://pixi.sh/) |

The `pip:` block in `environment.yml` is just more Python packages; it folds in with the others.

## Step 2 — Scaffold the uv project

```console
cd 04_from_conda
uv init --no-readme uv_env
cd uv_env
uv python pin 3.12
```

## Step 3 — Add the Python packages

```console
uv add 'pandas>=2,<3' 'numpy>=1.26' 'scanpy>=1.10' jupyterlab 'anndata>=0.10'
```

Resolution will take a few seconds (scanpy has a deep dependency tree). When it finishes:

```console
uv tree
cat pyproject.toml
ls uv.lock
```

## Step 4 — Verify

```console
uv run python -c "import scanpy as sc; print(sc.__version__)"
uv run jupyter lab --version
```

## Step 5 — Handle the non-Python tools separately

uv will not install `samtools` or `bcftools`. Pick one strategy:

* **System package manager** — `sudo apt install samtools bcftools` (Debian/Ubuntu) or `brew install samtools bcftools` (macOS). Fine for stable tools, awkward to pin exact versions.
* **A small conda side-env** — `conda create -n bio-tools -c bioconda samtools bcftools` and put it on your `PATH`. Keeps the bioinformatics tools reproducible but pushes Python work into uv.
* **pixi** — [pixi](https://pixi.sh/) is conda-compatible and uses a lock-file model similar to uv, so you get one consistent philosophy across Python and non-Python tools.

There is no single right answer; the trade-off is between "fewer tools" (pure conda or pure pixi) and "best-in-class Python tooling" (uv for Python, something else for binaries).

## What you should now understand

* uv replaces the Python parts of a conda env, not the non-Python parts.
* The migration is: list deps → drop non-Python → `uv init` → `uv python pin` → `uv add`.
* Bioinformatics and ML projects that depend on compiled binaries usually end up with a two-tool setup (uv + conda or uv + system packages).

## Next

Go to [`../05_reproduce_env/`](../05_reproduce_env/) to see what it looks like to land on a colleague's uv project.
