Table of Contents
=================

* [README](#readme)
   * [The Jupyter Notebook](#the-jupyter-notebook)
      * [Jupyter Notebook using Docker](#jupyter-notebook-using-docker)
      * [Jupyter Notebook shortcuts](#jupyter-notebook-shortcuts)
   * [Reticulate](#reticulate)
   * [Useful snippets](#useful-snippets)
   * [Links](#links)

Created by [gh-md-toc](https://github.com/ekalinin/github-markdown-toc)

# README

Python is a general-purpose programming language [that is very popular](https://madnight.github.io/githut/). I have wanted to learn Python for a long time but have put it off because I could get everything done using Bash, Perl, and R. However, recently I have been learning about deep learning and while I can use R and Keras, it is easier to use Python. I will keep test scripts in `script` and longer notes as Jupyter notebooks stored in `notebook`.

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

In your Jupyter notebook, click on `Help` and then select `Keyboard Shortcuts` to see a comprehensive list of shortcuts.

Below are some shortcuts that I have found useful:

* Place the cursor inside the parenthesis of a function and press shift+tab to bring up the function's documentation
* The notebook has a command and edit mode; press `escape` to enter command mode and press `enter` to enter edit mode.
* In command mode, press `m` to change a cell to Markdown and `y` to change a cell to code
* Control+enter to execute code
* `a` and `b` to insert a cell above and below, respectively
* Vim shortcuts like `dd` and `hjkl` work in command mode
* If you want to split a cell, enter edit mode in the cell and move the cursor to where you want the split, then press control+shift+- (hyphen)
* To merge a cell, select the cells in command mode (shift+ up/down arrows), and then press shift+m

## Reticulate

The [reticulate package](https://github.com/rstudio/reticulate) provides a comprehensive set of tools for interoperability between Python and R. Reticulate embeds a Python session within your R session, enabling seamless, high-performance interoperability.

    install.packages("reticulate")
    library(reticulate)
    use_python("/anaconda3/bin/python")

Check configurations

    # check if Python is available
    py_available()
    
    # check Python config
    py_config()
    
    # check if module is available
    py_module_available("umap")
    
    # check version of Python to use with reticulate
    # and location of module
    py_discover_config("umap")

Using Python in R Markdown

    ```{python}
    import sys
    print(sys.version)
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

## Links

* Difference between [Jupyter Notebook and JupyterLab](https://stackoverflow.com/questions/50982686/what-is-the-difference-between-jupyter-notebook-and-jupyterlab)?
* Perl to Python [phrasebook](https://wiki.python.org/moin/PerlPhrasebook) for those coming from Perl and wanting to learn Python
* [Python tutorial by w3schools](https://www.w3schools.com/python/default.asp)
* [Biopython tutorial](https://biopython.org/DIST/docs/tutorial/Tutorial.html)
* [Installing Python Packages from a Jupyter Notebook](https://jakevdp.github.io/blog/2017/12/05/installing-python-packages-from-jupyter/)

