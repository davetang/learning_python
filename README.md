# README

Python is a general-purpose programming language [that is very popular](https://madnight.github.io/githut/). I have wanted to learn Python for a long time but have put it off because I could get everything done in Perl and R. However, recently I've been working with [Snakemake](https://snakemake.readthedocs.io/en/stable/#), which is a workflow management system based on Python, and realised that knowing Python would help me use the tool better. In addition, a lot of my colleagues are using Python, so it helps to be able read and write Python.

# Conda environment

Create a new Conda environment for learning Python.

    conda env create -f learning_python.yml
    conda activate learning_python
    which python
    # ~/miniconda3/envs/learning_python/bin/python
    which pip
    # ~/miniconda3/envs/learning_python/bin/pip

# The Jupyter Notebook

The notebook formerly known as the [IPython Notebook](https://ipython.org/notebook.html) has also been on my list of things to learn. It serves as an interactive session for interweaving code and plain text. Just install [Anaconda](https://www.continuum.io/downloads) for your operating system and that will install [Jupyter Notebook](https://jupyter.readthedocs.io/en/latest/install.html).

    wget -c https://repo.anaconda.com/archive/Anaconda3-5.2.0-Linux-x86_64.sh
    bash Anaconda3-5.2.0-Linux-x86_64.sh
    source ~/.bashrc

After installation, run `jupyter notebook` to host an interactive session. I will use Jupyter notebooks to keep track of my Python code. Below are some useful links:

* [Comprehensive Beginner’s Guide to Jupyter Notebooks for Data Science & Machine Learning](https://www.analyticsvidhya.com/blog/2018/05/starters-guide-jupyter-notebook/)

## Shortcuts

Some shortcuts:

* The notebook has a command and edit mode; press `escape` to enter command mode and press `enter` to enter edit mode.
* In command mode, press `m` to change a cell to Markdown and `y` to change a cell to code
* Control+enter to execute code
* `a` and `b` to insert a cell above and below, respectively
* Vim shortcuts like `dd` and `hjkl` work in command mode

## Docker

Jupyter Docker Stacks are a set of ready-to-run Docker images containing Jupyter applications and interactive computing tools. Use [jupyter/tensorflow-notebook](https://jupyter-docker-stacks.readthedocs.io/en/latest/using/selecting.html#jupyter-tensorflow-notebook), which includes popular packages from the scientific Python ecosystem and the `tensorflow` and `keras` machine learning libraries.

    docker pull jupyter/tensorflow-notebook:latest

The script `docker_run.sh` (shown below) will start a Docker container called `tensorflow-notebook` that mounts the current directory on the host machine to `/data/` in the Docker container and listens on port 10000. Run `docker exec tensorflow-notebook jupyter notebook list` after starting the container to obtain the token needed to log into the notebook server.

```bash
#!/usr/bin/env bash

set -euo pipefail

version=latest
image=jupyter/tensorflow-notebook:${version}
container_name=tensorflow-notebook
port=10000

docker run -d \
   --rm \
   -p ${port}:8888 \
   --name ${container_name} \
   -v $(pwd):/data \
   ${image}

>&2 echo ${container_name} listening on port ${port}
>&2 echo Run the following to get the token: docker exec ${container_name} jupyter notebook list

>&2 echo Done
exit 0
```

See [Common Features](https://jupyter-docker-stacks.readthedocs.io/en/latest/using/common.html) for configurating the Jupyter Server with Docker.

# Reticulate

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

# Links

* Perl to Python [phrasebook](https://wiki.python.org/moin/PerlPhrasebook) for those coming from Perl and wanting to learn Python
* [Python tutorial by w3schools](https://www.w3schools.com/python/default.asp)

