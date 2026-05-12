## pixi

[pixi](https://pixi.sh/) is a cross-platform package and project manager from [prefix.dev](https://prefix.dev/) (the team behind the [rattler](https://github.com/conda/rattler) conda implementation and [`rattler-build`](https://prefix.dev/docs/rattler-build/)). Like [uv](uv.md), it is written in Rust and ships as a single static binary, but unlike `uv` it speaks the **conda ecosystem** natively — it resolves and installs packages from `conda-forge`, `bioconda`, and any other conda channel, while still being able to mix in PyPI packages on top.

If you have ever wanted `conda`'s ability to install `samtools`, `R`, or `gcc` alongside Python, but with `cargo`/`uv`-style lock files, fast resolution, and no `base` environment to worry about, `pixi` is the tool aimed at that gap.

### Why bother?

* **Speed.** Resolution and installation are dramatically faster than `conda` or `mamba`, since `pixi` uses `rattler` to parse channel metadata and resolve in parallel.
* **Reproducibility built in.** Every project has a multi-platform `pixi.lock` recording exact package versions and hashes for every target platform (`linux-64`, `osx-arm64`, `win-64`, …). `pixi install` reproduces the same environment everywhere.
* **Non-Python packages too.** `pixi add samtools bwa r-base gcc` works the same as `pixi add numpy`. This is the headline difference from `uv`.
* **Mix conda and PyPI.** When a package only exists on PyPI (or is newer there), `pixi add --pypi <pkg>` pulls it in alongside conda dependencies, all resolved together.
* **Per-project, no activation needed.** Environments live in `.pixi/envs/` in the project directory. `pixi run <cmd>` executes inside the env without a global `conda activate`.
* **Tasks.** Project-scoped commands (`pixi run test`, `pixi run lint`) defined in `pixi.toml`, similar to `npm run` or `cargo run`.
* **Multi-environment.** A single project can declare several named environments (e.g. `default`, `test`, `gpu`) sharing common dependencies, instead of juggling separate `environment.yml` files.

### Mental model: conda, venv, uv vs pixi

| Concern              | conda                                | venv + pip                              | uv                                          | pixi                                                 |
|----------------------|--------------------------------------|-----------------------------------------|---------------------------------------------|------------------------------------------------------|
| Install Python       | `conda create -n env python=3.12`    | install system Python or use `pyenv`    | `uv python install 3.12`                    | `pixi add python=3.12` (per project)                 |
| Non-Python packages  | yes (`samtools`, `R`, `gcc`)         | no                                      | no                                          | yes (any conda package)                              |
| Create environment   | `conda create -n env ...`            | `python -m venv .venv`                  | `uv venv` (or implicit via `uv sync`)       | `pixi init` (env created on first `pixi install`)    |
| Activate             | `conda activate env`                 | `source .venv/bin/activate`             | optional, use `uv run <cmd>`                | optional, use `pixi run <cmd>` or `pixi shell`       |
| Declare deps         | `environment.yml`                    | `requirements.in` / `requirements.txt`  | `pyproject.toml`                            | `pixi.toml` (or `[tool.pixi]` in `pyproject.toml`)   |
| Pin deps             | `conda env export > environment.yml` | `pip-compile` -> `requirements.txt`     | `uv.lock` (auto-generated)                  | `pixi.lock` (auto-generated, multi-platform)         |
| Reproduce env        | `conda env create -f environment.yml`| `pip install -r requirements.txt`       | `uv sync`                                   | `pixi install`                                       |
| Add a package        | `conda install pkg` then re-export   | edit `requirements.in`, re-compile      | `uv add pkg`                                | `pixi add pkg`                                       |
| Add a PyPI-only pkg  | `pip install` inside the env (fragile)| `pip install pkg`                      | `uv add pkg` (PyPI is the default)          | `pixi add --pypi pkg`                                |
| Run a CLI tool       | install into env                     | `pipx install tool`                     | `uvx tool` / `uv tool install tool`         | `pixi exec tool` / `pixi global install tool`        |
| Project tasks        | none                                 | none                                    | none                                        | `[tasks]` in `pixi.toml`, run with `pixi run <task>` |

Two important differences from `uv`:

1. `pixi` covers the **whole conda ecosystem**, so it can replace `conda`/`mamba` for bioinformatics, ML, and scientific stacks that depend on compiled non-Python tools. `uv` cannot.
2. `pixi` resolves **conda + PyPI together**. You can pin `pytorch` from `conda-forge` (with CUDA) and a small PyPI-only helper in the same lock, and the resolver guarantees they are compatible.

Two important differences from `conda`:

1. `pixi` is **project-first**, not environment-first. There is no `base` env, no global registry of named envs; the env lives next to the code in `.pixi/`. This is closer to the `cargo`/`uv`/`poetry` model.
2. `pixi.lock` is **multi-platform by default**. One lock file pins exact versions for every platform listed under `[project] platforms = [...]`, so a Linux teammate and a macOS-arm64 teammate get bit-identical envs without re-resolving.

### Fixing an environment with pixi

Two layers control reproducibility, both written into the project directory:

* `pixi.toml` declares the **constraints** (e.g. `python = ">=3.12,<3.13"`, `samtools = "*"`, the list of supported platforms, channels, and tasks). This is what you edit.
* `pixi.lock` records the **exact resolved versions** for every platform, including hashes. This is what guarantees reproducibility. Commit both files to git.

A typical fix-and-share workflow:

```console
# Start a new project (creates pixi.toml, .gitignore, .pixi/, pixi.lock on first install)
pixi init myproj && cd myproj

# Add channels and platforms if the defaults don't match (edit pixi.toml), e.g.
#   channels = ["conda-forge", "bioconda"]
#   platforms = ["linux-64", "osx-arm64"]

# Add dependencies (resolved, installed, and locked in one step)
pixi add python=3.12 'pandas>=2,<3' scanpy samtools

# A PyPI-only package alongside the conda ones
pixi add --pypi some-pypi-only-pkg

# Run code inside the project env without activating
pixi run python -c "import scanpy; print(scanpy.__version__)"

# Or drop into an activated subshell
pixi shell
```

On another machine, the entire environment is reconstructed with:

```console
git clone <repo> && cd <repo>
pixi install   # installs the exact versions from pixi.lock for this platform
```

`pixi install` is the analogue of `conda env create -f environment.yml` or `uv sync`, except the resolution work was already done when the lock file was generated, so it is both faster and bit-for-bit identical across machines.

### Tasks

`pixi.toml` can declare named tasks that run inside the project env:

```toml
[tasks]
test = "pytest -q"
lint = "ruff check ."
fetch = { cmd = "curl -O https://example.com/data.tsv", cwd = "data" }
pipeline = { depends-on = ["fetch", "test"] }
```

Then `pixi run test`, `pixi run lint`, or `pixi run pipeline`. This is roughly what `make`, `just`, or `npm run` would give you, but without an extra tool and with the env automatically active.

### Multiple environments

A project can declare several feature sets that combine into named environments:

```toml
[feature.test.dependencies]
pytest = "*"

[feature.gpu.dependencies]
pytorch-gpu = "*"

[environments]
default = { solve-group = "default" }
test    = { features = ["test"], solve-group = "default" }
gpu     = { features = ["gpu"] }
```

`pixi run -e test pytest` runs in the `test` env; `pixi run -e gpu python train.py` runs in the GPU env. This replaces the common conda pattern of keeping `environment.yml` and `environment-gpu.yml` in parallel and trying to keep them in sync.

### Coming from conda

If you already have an `environment.yml`, the migration looks like:

1. `pixi init` in the project directory.
2. Open `pixi.toml`, set `channels` (often `["conda-forge", "bioconda"]`) and `platforms` (the OS/arch combos you support).
3. For each dependency in `environment.yml`, run `pixi add <pkg>` (conda) or `pixi add --pypi <pkg>` (the `- pip:` block of `environment.yml`).
4. Replace `conda activate myenv && python script.py` with `pixi run python script.py`.
5. Commit `pixi.toml` and `pixi.lock`.

There is also `pixi init --import environment.yml`, which scaffolds the project from an existing conda env file as a starting point.

A useful sanity check: `pixi list` shows resolved packages for the current env, similar to `conda list`.

### Coming from uv

If you already have a `pyproject.toml` driven by `uv`, you can keep `pyproject.toml` and add a `[tool.pixi]` table to it instead of using a separate `pixi.toml`. The motivation is usually one of:

* You need a non-Python tool (`samtools`, `gdal`, `r-base`, system `ffmpeg`) and don't want to install it separately.
* You need a specific build of a Python package (CUDA `pytorch`, MKL `numpy`) that conda-forge packages more cleanly than PyPI wheels.

`pixi` will then manage the conda parts and can also install your `[project.dependencies]` from PyPI in the same resolve.

If your project is pure Python and you don't need anything outside PyPI, `uv` is the simpler choice and `pixi` is overkill.

### Using a pixi env with R's `reticulate`

`reticulate` is happy to use any Python interpreter you point it at, so a pixi env works fine — you just have to tell `reticulate` where it lives, because pixi envs are not registered in a global conda registry (no `conda env list` to discover them).

A pixi env is laid out like a conda env: `.pixi/envs/<env-name>/bin/python` on Linux/macOS, `.pixi\envs\<env-name>\python.exe` on Windows. The default env is named `default`.

Make sure the env actually contains the Python bits `reticulate` needs:

```console
pixi add python numpy   # plus whatever else you'll import from R
pixi install
```

Then from R, pick one of:

```r
# Most explicit — point at the interpreter directly
reticulate::use_python(
  file.path(".pixi", "envs", "default", "bin", "python"),
  required = TRUE
)

# Or treat the pixi env as a conda env (it is one, on disk)
reticulate::use_condaenv(
  condaenv = normalizePath(file.path(".pixi", "envs", "default")),
  required = TRUE
)
```

Or set it once for the session via an environment variable, which is convenient in `.Rprofile`, RStudio project options, or a Quarto/Rmd `setup` chunk:

```r
Sys.setenv(RETICULATE_PYTHON = normalizePath(
  file.path(".pixi", "envs", "default", "bin", "python")
))
library(reticulate)
```

`required = TRUE` is worth keeping — without it, `reticulate` may silently fall back to a different Python it finds on `PATH`, which defeats the point of pinning the env.

A common ergonomic pattern is to wrap R itself in `pixi run` so the env is already active when R starts. Add an `r-base` dependency and a task in `pixi.toml`:

```toml
[dependencies]
python = ">=3.12,<3.13"
r-base = "*"
numpy  = "*"

[tasks]
r       = "R --no-save"
rstudio = "rstudio"   # if rstudio-desktop is in the env
render  = "quarto render"
```

Then `pixi run r` (or `pixi run render` for a Quarto doc) launches R with `RETICULATE_PYTHON` effectively resolved to the pixi env's Python, and `reticulate` will pick it up without any extra configuration in your `.R`/`.Rmd` files. This is the closest pixi equivalent to the `uv run` + `.venv` workflow you get with `reticulate::use_virtualenv(".venv")`.

One caveat: `reticulate::use_virtualenv()` expects a *venv* layout (a `pyvenv.cfg` file at the root), and a pixi env is a *conda* env, so `use_virtualenv()` is not the right function — use `use_python()` or `use_condaenv()` as shown above.

### Cheat sheet

```console
pixi init                       # scaffold pixi.toml in the current directory
pixi init --import env.yml      # scaffold from an existing conda environment.yml
pixi add pkg                    # add and lock a conda dep
pixi add --pypi pkg             # add and lock a PyPI dep
pixi add --feature test pytest  # add to a named feature
pixi remove pkg                 # drop a dep
pixi install                    # reproduce env from pixi.lock
pixi update                     # bump deps within constraints, refresh lock
pixi run <cmd>                  # run a command inside the project env
pixi run <task>                 # run a task defined in [tasks]
pixi run -e <env> <cmd>         # run in a named environment
pixi shell                      # activated subshell in the project env
pixi list                       # list installed packages
pixi exec <tool>                # run a tool ephemerally (like uvx / pipx run)
pixi global install <tool>      # install a CLI tool globally
pixi search <pkg>               # search configured channels
```

### When to pick which

* **Pure-Python project, PyPI only.** Use `uv`. Smaller surface, faster to learn, lock files are simpler.
* **Python + compiled non-Python deps (bioinformatics, geospatial, ML with CUDA, R interop).** Use `pixi`. You get conda's package coverage with a real lock file.
* **Legacy `environment.yml` you want to make reproducible.** Use `pixi` and `pixi init --import environment.yml` as the migration path.
* **System-wide CLI tools written in Python.** Either `uv tool install` or `pixi global install` works; pick whichever ecosystem the tool comes from.
* **You only ever need pip-style installs and a `requirements.txt`.** Plain `uv pip` is the lightest option; `pixi` is overkill.
