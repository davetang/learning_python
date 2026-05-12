## uv

[uv](https://docs.astral.sh/uv/) is a Python package and project manager from [Astral](https://astral.sh/) (the team behind [Ruff](https://docs.astral.sh/ruff/)). It is written in Rust and bundles the jobs that previously required `pip`, `pip-tools`, `pipx`, `virtualenv`, `pyenv`, and a project manager such as `poetry` or `hatch` into a single static binary.

If you already pin Python environments with `conda` or `venv`, the mental model below should be enough to get you fixing environments with `uv` the same way.

### Why bother?

* **Speed.** Resolution and installation are 10-100x faster than `pip`, since `uv` resolves dependencies in parallel and caches aggressively. Re-creating an environment from a lock file feels instantaneous compared to `conda env create`.
* **One tool.** No more deciding between `pip` + `venv` + `pip-tools` + `pyenv`; `uv` covers all of these.
* **Reproducibility built in.** `uv` writes a cross-platform `uv.lock` automatically, similar to `poetry.lock` or `Cargo.lock`, so `uv sync` reproduces the same environment everywhere.
* **Manages Python itself.** `uv python install 3.12` downloads a standalone interpreter without touching the system Python, the way `pyenv` or `conda` would.

### Mental model: conda and venv vs uv

| Concern              | conda                              | venv + pip                                  | uv                                          |
|----------------------|------------------------------------|---------------------------------------------|---------------------------------------------|
| Install Python       | `conda create -n env python=3.12`  | install system Python or use `pyenv`        | `uv python install 3.12`                    |
| Create environment   | `conda create -n env ...`          | `python -m venv .venv`                      | `uv venv` (or implicit via `uv sync`)       |
| Activate             | `conda activate env`               | `source .venv/bin/activate`                 | activation optional, use `uv run <cmd>`     |
| Declare deps         | `environment.yml`                  | `requirements.in` / `requirements.txt`      | `pyproject.toml` (`[project.dependencies]`) |
| Pin deps             | `conda env export > environment.yml` | `pip-compile` -> `requirements.txt`       | `uv.lock` (auto-generated)                  |
| Reproduce env        | `conda env create -f environment.yml` | `pip install -r requirements.txt`        | `uv sync`                                   |
| Add a package        | `conda install pkg` then re-export | edit `requirements.in`, re-compile          | `uv add pkg` (updates `pyproject.toml` + `uv.lock`) |
| Run a CLI tool       | install into env                   | `pipx install tool`                         | `uvx tool` or `uv tool install tool`        |

Two important differences:

1. `uv` is **Python-only**. `conda` can install non-Python software (`samtools`, `R`, `gcc`); `uv` cannot. For bioinformatics work where you need both Python and a compiled binary, you may still want `conda` (or `pixi`) for the surrounding stack and `uv` for the Python parts.
2. `uv` does not require activation. `uv run python script.py` and `uv run pytest` execute inside the project's environment directly, which makes scripts and CI configs cleaner.

### Fixing an environment with uv

Two layers control reproducibility, both written into the project directory:

* `pyproject.toml` declares the **constraints** (e.g. `pandas>=2,<3`, `requires-python = ">=3.12"`). This is what you edit.
* `uv.lock` records the **exact resolved versions** for every platform, including hashes. This is what guarantees reproducibility. Commit both files to git.

A typical fix-and-share workflow:

```console
# Start a new project (creates pyproject.toml, .venv, uv.lock)
uv init myproj && cd myproj

# Pin Python version
uv python pin 3.12

# Add dependencies (resolved, installed, and locked in one step)
uv add 'pandas>=2,<3' scanpy

# Run code inside the project env without activating
uv run python -c "import scanpy; print(scanpy.__version__)"
```

On another machine, the entire environment is reconstructed with:

```console
git clone <repo> && cd <repo>
uv sync   # installs the exact versions from uv.lock
```

`uv sync` is the analogue of `conda env create -f environment.yml` or `pip install -r requirements.txt`, except the resolution work was already done when the lock file was generated, so it is both faster and bit-for-bit identical across machines.

### Coming from venv

If you already have a `requirements.txt`, you can keep using it; `uv` is a drop-in replacement for `pip`:

```console
uv venv                                   # like python -m venv .venv
uv pip install -r requirements.txt        # like pip install -r ...
uv pip compile requirements.in -o requirements.txt  # like pip-compile
```

This is the path of least resistance: faster installs, no lock file, no `pyproject.toml`. You only need to graduate to `uv add` / `uv sync` when you want the lock-file guarantees.

### Coming from conda

There is no direct equivalent of `environment.yml`, so the migration is:

1. List the Python packages from your `environment.yml` (drop anything non-Python, e.g. `samtools`).
2. `uv init` in the project directory.
3. `uv python pin <version>` to match the Python version you used.
4. `uv add` each package, using version constraints where you had them.
5. Commit `pyproject.toml` and `uv.lock`.

For non-Python tools that used to live in the conda env, install them separately (system package manager, `conda` in a side env, or [`pixi`](https://pixi.sh/) which is conda-compatible but uses the same lock-file philosophy as uv).

### Using a uv env with R's `reticulate`

`uv` is the most frictionless way to manage the Python environment that R's [`reticulate`](https://rstudio.github.io/reticulate/) calls into:

* `uv venv` produces a standard virtual environment (`.venv/` with a `pyvenv.cfg`), which is exactly what `reticulate::use_virtualenv()` expects.
* `reticulate` ≥ 1.41 actually uses `uv` internally for its own package and environment management ([reticulate changelog](https://rstudio.github.io/reticulate/news/)), so the two tools are aligned by design.
* There are none of the `conda-meta/history` parsing quirks that affect conda-style envs (see the corresponding section in [pixi.md](pixi.md)).

A typical setup:

```console
uv init myproj && cd myproj
uv python pin 3.12
uv add numpy pandas      # whatever you'll import from R
```

Then from R, any of the following work — `use_virtualenv()` is the most idiomatic:

```r
# Idiomatic — uv produces a real venv, so this just works
reticulate::use_virtualenv(".venv", required = TRUE)

# Equivalent, more explicit
reticulate::use_python(
  file.path(".venv", "bin", "python"),   # ".venv/Scripts/python.exe" on Windows
  required = TRUE
)
```

Or set it once for the session — convenient in `.Rprofile`, RStudio project options (Tools → Project Options → Python), or a Quarto/Rmd `setup` chunk:

```r
Sys.setenv(RETICULATE_PYTHON = normalizePath(
  file.path(".venv", "bin", "python")
))
library(reticulate)
```

`RETICULATE_PYTHON` overrides every other `use_*()` call, which is what you want when RStudio initialises Python before your code runs. Keep `required = TRUE` on the `use_*()` variants so `reticulate` errors loudly instead of silently falling back to a system Python on `PATH`.

To launch R with the env already on `PATH`, wrap it with `uv run`. Note that `uv` itself only manages Python — R has to come from somewhere else (system, [`rig`](https://github.com/r-lib/rig), or conda/pixi in a side env):

```console
uv run R --no-save                    # if R is on the system PATH
uv run quarto render report.qmd       # Quarto picks up the venv's Python
```

This is the closest equivalent to `pixi run r` for the Python side, without `pixi`'s ability to pin R itself.

When **not** to pick `uv` for `reticulate`: if the Python env you need from R requires non-Python conda packages (e.g. Python code that shells out to `samtools`, or a specific CUDA `pytorch` build from `conda-forge`), `uv` cannot install those — use `pixi` for that env and accept the small amount of extra wiring documented in [pixi.md](pixi.md). For pure-Python use, `uv` is the cleaner choice.

### Cheat sheet

```console
uv python install 3.12         # install a Python interpreter
uv python pin 3.12             # pin this project's Python
uv init                        # scaffold pyproject.toml + .venv + uv.lock
uv add pkg                     # add and lock a runtime dep
uv add --dev pytest            # add a dev-only dep
uv remove pkg                  # drop a dep
uv sync                        # reproduce env from uv.lock
uv lock --upgrade              # bump deps within constraints
uv run <cmd>                   # run a command inside the project env
uvx <tool>                     # run a tool ephemerally (like pipx run)
uv tool install <tool>         # install a CLI tool globally
uv pip install <pkg>           # pip-compatible escape hatch
```
