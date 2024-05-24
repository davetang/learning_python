## Table of Contents

- [README](#readme)
  - [pip](#pip)
    - [Installing specific versions](#installing-specific-versions)
    - [Searching PyPi](#searching-pypi)
    - [Quickly check if module is installed](#quickly-check-if-module-is-installed)
  - [The Jupyter Notebook](#the-jupyter-notebook)
    - [Jupyter Notebook using Docker](#jupyter-notebook-using-docker)
    - [Jupyter Notebook shortcuts](#jupyter-notebook-shortcuts)
  - [Reticulate](#reticulate)
  - [Tools for finding coding errors](#tools-for-finding-coding-errors)
  - [Useful snippets](#useful-snippets)
  - [Links](#links)

# README

Python is a general-purpose programming language [that is very popular](https://madnight.github.io/githut/). I have wanted to learn Python for a long time but have put it off because I could get everything done using Bash, Perl, and R. However, recently I have been learning about deep learning and while I can use R and Keras, it is easier to use Python. I will keep test scripts in `script` and longer notes as Jupyter notebooks stored in `notebook`.

## pip

[pip](https://pypi.org/project/pip/) is the package installer for Python. You can use `pip` to install packages from the [Python Package Index](https://pypi.org/) (PyPI) and other indexes. The Python Package Index is a repository of software for the Python programming language and `pip` is the recommended tool for installing Python packages.

The [cookiecutter installation instructions](https://cookiecutter.readthedocs.io/en/stable/installation.html) shows the following command:

```console
python3 -m pip install --user cookiecutter
```

The documentation for `--user` from `pip install --help` is as follows:

```
  --user                      Install to the Python user install directory for
                              your platform. Typically ~/.local/, or
                              %APPDATA%\Python on Windows. (See the Python
                              documentation for site.USER_BASE for full
                              details.)
```

This is relevant for a system-wide installation of `pip`, where `pip` will install to `/usr/local/lib/`. Check which `pip` is used using `which pip`.

In addition it is [recommended](https://snarky.ca/why-you-should-use-python-m-pip/) that `python -m pip` be used over `pip` because it gives better control over which Python interpreter is used.

### Installing specific versions

```console
pip install numpy==1.26.4
```

### Searching PyPi

You could use `pip search` before but this has been deprecated and it is recommended that a web browser be used :(

```console
pip search some_package
```
```
ERROR: XMLRPC request failed [code: -32500]
RuntimeError: PyPI no longer supports 'pip search' (or XML-RPC search). Please use https://pypi.org/search (via a browser) instead. See https://warehouse.pypa.io/api-reference/xml-rpc.html#deprecated-methods for more information.
```

### Quickly check if module is installed

Pass program on command line.

```console
python -c 'print("Hi")'
```
```
Hi
```

Try to import.

```console
python -c 'import does_not_exist'
```
```
Traceback (most recent call last):
  File "<string>", line 1, in <module>
ModuleNotFoundError: No module named 'does_not_exist'
```

## The Jupyter Notebook

The notebook formerly known as the [IPython Notebook](https://ipython.org/notebook.html) has also been on my list of things to learn. It serves as an interactive session for interweaving code and plain text. Just install [Anaconda](https://www.continuum.io/downloads) for your operating system and that will install [Jupyter Notebook](https://jupyter.readthedocs.io/en/latest/install.html).

    wget -c https://repo.anaconda.com/archive/Anaconda3-5.2.0-Linux-x86_64.sh
    bash Anaconda3-5.2.0-Linux-x86_64.sh
    source ~/.bashrc

After installation, run `jupyter notebook` to host an interactive session. See the [Comprehensive Beginner’s Guide to Jupyter Notebooks for Data Science & Machine Learning](https://www.analyticsvidhya.com/blog/2018/05/starters-guide-jupyter-notebook/) for a nice introduction to Jupyter notebooks.

### Jupyter Notebook using Docker

[Jupyter Docker Stacks](https://jupyter-docker-stacks.readthedocs.io/en/latest/index.html) are a set of ready-to-run Docker images containing Jupyter applications and interactive computing tools. Use [jupyter/tensorflow-notebook](https://jupyter-docker-stacks.readthedocs.io/en/latest/using/selecting.html#jupyter-tensorflow-notebook), which includes popular packages from the scientific Python ecosystem and the `tensorflow` and `keras` machine learning libraries.

    docker pull jupyter/tensorflow-notebook:latest

The script `run_docker_tensorflow_notebook.sh` (shown below) will start a Docker container called `tensorflow-notebook` that mounts the current directory on the host machine to `/data/` in the Docker container and listens on port 10000. Run `docker exec tensorflow-notebook jupyter server list` after starting the container to obtain the token needed to log into the notebook server.

```bash
#!/usr/bin/env bash

set -euo pipefail

# JupyterLab is now the default for all the Jupyter Docker stack images
# the latest version as of 2022-08-25 is
# 9c23551dec7e6c93d2363e8a17307d0a8bb847471e2b2fe959dd019daa370178, which
# keeps crashing when I try to start or open a new notebook, so I am using the
# older ubuntu-20.04 image
# version=latest
version=ubuntu-20.04
image=jupyter/tensorflow-notebook:${version}
container_name=tensorflow-notebook
port=10000

start_container () {

   # If you change the notebook username using the following:
   #
   #     -e NB_USER="my-username" \
   #
   # You will not be able to list currently running servers to obtain a token.
   # Therefore just use the username jovyan
   #
   # In addition, you need to run as root (`--user root`)
   # or else you will not be able to edit mounted files

   docker run -d \
      --rm \
      -p ${port}:8888 \
      --user root \
      -e NB_UID=$(id -u) \
      -e NB_GID=$(id -g) \
      -v $(pwd):/home/jovyan/work \
      --name ${container_name} \
      ${image}

   >&2 echo ${container_name} listening on port ${port}
   >&2 echo -e "Run the following to get the token:\ndocker exec ${container_name} jupyter server list"

}

check_container () {

   docker container inspect ${container_name} > /dev/null 2>&1
   # $? == 0 if container exists
   if [[ $? > 0 ]]; then
      start_container
   else
      >&2 echo ${container_name} already exists
      exit 1
   fi

}

# the || is necessary for preventing `set -e` immediately exiting
# if the container already exists
check_container || true

>&2 echo Done
exit 0
```

See [Common Features](https://jupyter-docker-stacks.readthedocs.io/en/latest/using/common.html) for configurating the Jupyter Server with Docker.

### Jupyter Notebook shortcuts

Below are some shortcuts that I have found useful:

* Place the cursor inside the parenthesis of a function and press shift+tab to
  bring up the function's documentation
* The notebook has a command and edit mode; press `escape` to enter command
  mode and press `enter` to enter edit mode.
* In command mode, press `m` to change a cell to Markdown and `y` to change a
  cell to code
* Control+enter to execute code
* `a` and `b` to insert a cell above and below, respectively
* Vim shortcuts like `dd` and `hjkl` work in command mode
* Use `x`, `c`, `v` to cut, copy, and paste cells
* If you want to split a cell, enter edit mode in the cell and move the cursor
  to where you want the split, then press control+shift+- (hyphen)
* To merge a cell, select the cells in command mode (shift+ up/down arrows),
  and then press shift+m

See [Common Jupyter Lab Keyboard
Shortcuts](https://gist.github.com/discdiver/9e00618756d120a8c9fa344ac1c375ac)
for more.

## Reticulate

The [reticulate package](https://github.com/rstudio/reticulate) provides a
comprehensive set of tools for interoperability between Python and R.
Reticulate embeds a Python session within your R session, enabling seamless,
high-performance interoperability.

See `notebook/reticulate.Rmd`.

## Tools for finding coding errors

Linters are tools that check for program style and errors beyond bad syntax.
Two popular linters are [pylint](https://pylint.pycqa.org/en/latest/) and
[flake8](https://flake8.pycqa.org/en/latest/).

```bash
python3 -m pip install pylint
pylint script/root.py

python3 -m pip install flake8
flake8 script/root.py
```

The [mypy](https://github.com/python/mypy) tool is a static type checker and is
used to find mis-used types such as dividing a string by a number.

```bash
python3 -m pip install -U mypy
mypy script/root.py
```

## Useful snippets

Check if file exists and prompt before overwriting.

```python
import sys
import os.path

somefile = "blah.txt"

if os.path.isfile(somefile):
    print(f"Specified BAM output {somefile} already exists", file = sys.stderr)
    what_to_do = input("Continue y/N? ")
    if what_to_do == "y" or what_to_do == "Y":
        print("Continuing", file = sys.stderr)
    else:
        sys.exit()
```

Get the directory of a script.

```python
import os.path
print("dirname of script: {}".format(os.path.dirname(__file__)) )
```

Get environment variables.

```python
import os
user = os.environ['USER']
home = os.environ['HOME']
```

Print all (except internal use and magical) attributes of an instance.

```python
import re
import pprint
pp = pprint.PrettyPrinter(indent = 4)

for att in dir(elispot):
    if not re.match("^_", att):
        print(f"{att} attribute")
        pp.pprint(getattr(elispot, att))
```

## Links

* Blog post on [using underscores in Python](https://www.hacksoft.io/blog/underscores-dunders-and-everything-nice)
* [Article explaining](https://note.nkmk.me/en/python-if-name-main/) `if __name__ == '__main__'`
* Difference between [Jupyter Notebook and JupyterLab](https://stackoverflow.com/questions/50982686/what-is-the-difference-between-jupyter-notebook-and-jupyterlab)?
* Perl to Python [phrasebook](https://wiki.python.org/moin/PerlPhrasebook) for those coming from Perl and wanting to learn Python
* [Python tutorial by w3schools](https://www.w3schools.com/python/default.asp)
* [Biopython tutorial](https://biopython.org/DIST/docs/tutorial/Tutorial.html)
* [Installing Python Packages from a Jupyter Notebook](https://jakevdp.github.io/blog/2017/12/05/installing-python-packages-from-jupyter/)

