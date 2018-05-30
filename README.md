# README

Python is a general-purpose programming language [that is very popular](https://madnight.github.io/githut/). In bioinformatics, Python has replaced Perl as the scripting language of choice, which means there's a lot more Python scripts in my area of work. I'd like to learn Python to help me better understand a lot of bioinformatic scripts/tools.

# The Jupyter Notebook

The notebook formerly known as the [IPython Notebook](https://ipython.org/notebook.html) has also been on my list of things to learn. It serves as an interactive session for interweaving code and plain text. After [installation](https://jupyter.readthedocs.io/en/latest/install.html), run `jupyter notebook` to host an interactive session. I will use Jupyter notebooks to keep track of my Python code.

# Reticulate

The [reticulate package](https://github.com/rstudio/reticulate) provides a comprehensive set of tools for interoperability between Python and R. Reticulate embeds a Python session within your R session, enabling seamless, high-performance interoperability.

    install.packages("reticulate")
    library(reticulate)
    use_python("/anaconda3/bin/python")

Using Python in R Markdown

    ```{python}
    import sys
    print(sys.version)
    ```

# Links

* Perl to Python [phrasebook](https://wiki.python.org/moin/PerlPhrasebook) for those coming from Perl and wanting to learn Python

