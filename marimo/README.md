## Table of Contents

- [README](#readme)
  - [Installing](#installing)
  - [Deploying](#deploying)
    - [Docker](#docker)

# README

[marimo](https://marimo.io/) is an open-source reactive notebook for Python — reproducible, Git-friendly, AI-native, SQL built-in, executable as a script, shareable as an app.

## Installing

Create virtual environment in a specific directory.

```console
python -m venv marimo_env
source ./marimo_env/bin/activate
```

Then install.

```console
pip install marimo
marimo tutorial intro
```

## Deploying

You can [deploy](https://docs.marimo.io/guides/deploying/) marimo in three ways:

1. via an edit server, which allows you to create and edit notebooks. On the CLI, this is launched with marimo edit, and is similar to jupyter notebook.
2. via a run server, which allows you serve marimo notebooks as read-only web apps. On the CLI, this is launched with marimo run notebook.py
3. programmatically, which allows you serve read-only marimo apps as part of other ASGI applications, for example using FastAPI.

### Docker

Find tags at <https://github.com/marimo-team/marimo/pkgs/container/marimo/>

```console
docker run --rm -p 8080:8080 -it ghcr.io/marimo-team/marimo:0.14.14-data
```

Then head to http://0.0.0.0:8080.
