## reticulate

[reticulate](https://rstudio.github.io/reticulate/) is the R package that embeds a Python session inside R. You can `import("numpy")`, call Python functions, and pass R objects in and out — `reticulate` handles type conversion (R data frame ↔ pandas, R matrix ↔ numpy array, R list ↔ Python dict/list). It is the standard way to use Python from inside R or RStudio.

This guide focuses on the question that determines whether `reticulate` works smoothly: **how do you create the Python environment that `reticulate` calls into?**

### Mental model

`reticulate` does not manage Python on its own. It needs an existing Python interpreter — system Python, a virtualenv, or a conda env — and it loads that interpreter into the R process. Once loaded, the Python interpreter **cannot be changed without restarting R**.

That last point is the cause of most "reticulate didn't pick my env" headaches: if R or RStudio initialises Python (even implicitly, by loading a package that touches reticulate at startup) before your `use_*()` call runs, you get whatever interpreter was found first.

### Choosing where Python comes from

Several tools can create a reticulate-compatible env. The choice mostly depends on what's *in* the env:

| Source                          | Layout              | reticulate function          | When to pick                                                                 |
|---------------------------------|---------------------|------------------------------|------------------------------------------------------------------------------|
| `uv venv`                       | venv (`pyvenv.cfg`) | `use_virtualenv(".venv")`    | **Default for pure-Python.** See [uv.md](uv.md).                             |
| `python -m venv`                | venv                | `use_virtualenv(".venv")`    | Legacy/lightweight; prefer `uv venv` (10–100× faster).                       |
| `pixi`                          | conda env           | `use_condaenv(<abs path>)`   | Need non-Python deps (`samtools`, `gdal`, CUDA `pytorch`). See [pixi.md](pixi.md). |
| `conda` / `mamba`               | conda env           | `use_condaenv("name")`       | Existing named conda envs you don't want to migrate.                         |
| `reticulate::install_python()`  | uv-managed venv     | implicit                     | Quick start, no project; `reticulate` ≥ 1.41 uses `uv` under the hood.       |
| system Python                   | system              | `use_python("/usr/bin/python3")` | One-off scripts; avoid for projects (no reproducibility).                |

### Recommended: a uv-managed venv

For most R/Python projects this is the lightest setup with the fewest moving parts. `reticulate` ≥ 1.41 uses `uv` internally for its own env management, so the tools are aligned by design.

```console
uv init                  # scaffold pyproject.toml + .venv + uv.lock
uv python pin 3.12
uv add numpy pandas      # whatever you'll import from R
```

Then from R:

```r
reticulate::use_virtualenv(".venv", required = TRUE)
np <- reticulate::import("numpy")
np$array(c(1, 2, 3))
```

Full `uv` workflow (lock files, `uv sync` on other machines, `uv run`) is in [uv.md](uv.md).

### Alternative: pixi for non-Python deps

If the Python env you need from R also requires non-Python packages — `samtools`, `gdal`, CUDA `pytorch` from `conda-forge` — use `pixi` and point `reticulate` at the pixi env explicitly:

```r
reticulate::use_condaenv(
  condaenv = normalizePath(file.path(".pixi", "envs", "default")),
  required = TRUE
)
```

There are a few historical caveats (a `conda-meta/history` parsing bug; no auto-discovery in RStudio's Python pane). Details and the fix are in [pixi.md](pixi.md).

### Pointing reticulate at the env

Four mechanisms, in order of precedence:

1. **`RETICULATE_PYTHON` environment variable.** Overrides everything else. Most reliable when RStudio initialises Python early.
2. **`reticulate::use_*()` functions called before Python loads.** `use_python()`, `use_virtualenv()`, `use_condaenv()`. Always pass `required = TRUE` so it errors loudly on a miss instead of silently falling back to system Python.
3. **RStudio's Python pane** (Tools → Global/Project Options → Python). Persists the chosen interpreter path in project or user settings.
4. **Auto-detection.** First Python on `PATH`. Fine for quick experiments; never rely on it for projects.

For projects, the cleanest pattern is to set `RETICULATE_PYTHON` in a project-level `.Rprofile`:

```r
# .Rprofile
Sys.setenv(RETICULATE_PYTHON = normalizePath(
  file.path(".venv", "bin", "python")    # ".venv/Scripts/python.exe" on Windows
))
```

Commit `.Rprofile` alongside `pyproject.toml` / `uv.lock`. Anyone cloning the repo gets the right interpreter on the first R session, before any package that touches `reticulate` is loaded.

### RStudio specifics

* The **Python pane** (Tools → Global/Project Options → Python) lists discovered virtualenvs and conda envs and writes the chosen path into `.Rproj` (project) or user settings. It does **not** discover `.pixi/envs/*` — point it at the binary manually for pixi envs.
* The pane setting is roughly equivalent to setting `RETICULATE_PYTHON`; it takes effect at session start.
* `reticulate::repl_python()` opens a Python prompt inside the R console; type `exit` to return. Any Python globals are accessible from R via `py$x`.
* The **Environment pane** shows Python objects you create via `reticulate`.
* Python chunks in Quarto / R Markdown automatically use the same interpreter `reticulate` is configured with — there is one thing to pin, not two.

### Using Python from R

The most useful entry points:

```r
library(reticulate)

# Import a module as if it were an R list
np <- import("numpy")
np$mean(c(1, 2, 3))

# Run a Python file; its functions become available as R functions
source_python("helpers.py")

# Run an inline Python string
py_run_string("import pandas as pd; df = pd.DataFrame({'x': [1,2,3]})")
py$df            # access Python globals from R

# Drop into a Python REPL inside the R session
repl_python()
```

Type conversion happens automatically:

| R                  | Python              |
|--------------------|---------------------|
| `data.frame`       | `pandas.DataFrame`  |
| `matrix` / `array` | `numpy.ndarray`     |
| named `list`       | `dict`              |
| unnamed `list`     | `list`              |
| `NULL`             | `None`              |
| `NA` (numeric)     | `numpy.nan`         |
| `TRUE` / `FALSE`   | `True` / `False`    |

Use `r_to_py()` / `py_to_r()` to force conversion explicitly, or `dict()` / `tuple()` for Python-specific types.

### Quarto and R Markdown

R and Python chunks coexist in `.qmd` / `.Rmd` and share state. Configure once in a setup chunk:

````
```{r setup}
library(reticulate)
use_virtualenv(".venv", required = TRUE)
```

```{r}
df <- data.frame(x = 1:3, y = letters[1:3])
```

```{python}
# df is available as r.df, converted to a pandas DataFrame
r.df.head()
```
````

From the Python side, R objects appear under `r.`; from the R side, Python objects appear under `py$`.

### Common pitfalls

1. **"`reticulate` ignored my `use_python()` call."** Python was already initialised when `use_python()` ran. Check `reticulate::py_config()` — if it shows a different interpreter than you asked for, set `RETICULATE_PYTHON` in `.Rprofile` so it is in place before R loads anything that touches Python.
2. **Silent fallback to system Python.** Always pass `required = TRUE` to `use_*()`.
3. **Paths with spaces break conda-env detection** ([rstudio/reticulate#1149](https://github.com/rstudio/reticulate/issues/1149)). Avoid spaces in project paths.
4. **Pixi env not picked up.** Use `use_condaenv()` with an absolute path, not `use_virtualenv()` — pixi envs are conda envs and lack `pyvenv.cfg`. See [pixi.md](pixi.md).
5. **Wrong Python on Windows.** The interpreter lives at `.venv/Scripts/python.exe`, not `.venv/bin/python`.
6. **Multiple envs across projects.** Use project-local `.Rprofile` per project rather than a single global `RETICULATE_PYTHON`, so switching projects switches Python.

### Cheat sheet

```r
library(reticulate)

# --- configure (do this once, before any other Python use) ---
use_virtualenv(".venv", required = TRUE)                              # uv / venv
use_condaenv("envname", required = TRUE)                              # conda by name
use_condaenv(normalizePath(".pixi/envs/default"), required = TRUE)    # pixi
use_python("/abs/path/to/python", required = TRUE)                    # any binary

# --- inspect ---
py_config()                       # which interpreter is loaded
py_module_available("numpy")      # is a module importable?
py_list_packages()                # installed packages in the env

# --- run Python ---
np <- import("numpy")             # import a module
source_python("script.py")        # source a file into R
py_run_string("x = 42")           # inline string
repl_python()                     # interactive REPL

# --- convert ---
r_to_py(x)
py_to_r(x)
```
