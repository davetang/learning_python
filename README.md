# README

Python is a general-purpose programming language [that is very popular](https://madnight.github.io/githut/). I have wanted to learn Python for a long time but have put it off because I could get everything done in Perl and R. However, recently I've been working with [Snakemake](https://snakemake.readthedocs.io/en/stable/#), which is a workflow management system based on Python, and realised that knowing Python would help me use the tool better. In addition, a lot of my colleagues are using Python, so it helps to be able read and write Python.

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

Jupyter Docker Stacks are a set of ready-to-run Docker images containing Jupyter applications and interactive computing tools. Use [jupyter/scipy-notebook](https://jupyter-docker-stacks.readthedocs.io/en/latest/using/selecting.html#jupyter-scipy-notebook), which includes popular packages from the scientific Python ecosystem.

    docker pull jupyter/scipy-notebook:latest

Running a container from this GitHub repository to access the `notebook` directory.

    docker run -v "$PWD":/home/jovyan/work -p 8888:8888 jupyter/scipy-notebook:latest

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

