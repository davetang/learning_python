# A simple project

Following the [packaging Python projects
tutorial](https://packaging.python.org/en/latest/tutorials/packaging-projects/).

Use `create_venv.sh` to create an environment to work in; then activate the
environment.

```console
source venv/bin/activate
```

`init.sh` will create all the directories and files.

`pyproject.toml` tells frontend build tools like `pip` and `build` what backend
tool to use to create distribution packages for your project. You can choose
from a number of backends; the tutorial uses
[Hatchling](https://packaging.python.org/en/latest/key_projects/#hatch) by
default, but it will work identically with setuptools, Flit, PDM, and others
that support the `[project]` table for metadata.

After running `init.sh`, the next step is to generate [distribution
packages](https://packaging.python.org/en/latest/glossary/#term-Distribution-Package)
for the package. These are archives that are uploaded to the Python Package
  Index and can be installed by `pip`.

```console
# activate environment, if you haven't already
source venv/bin/activate

python3 -m pip install --upgrade build
```

Run the following command in `packaging_tutorial/`.

```console
cd packaging_tutorial/
python3 -m build

tree --charset ascii dist
```

There should be two files in the `dist` directory.

```
dist
|-- example_package_davetang-0.0.1-py3-none-any.whl
`-- example_package_davetang-0.0.1.tar.gz
```

The `tar.gz` file is a [source
distribution](https://packaging.python.org/en/latest/glossary/#term-Source-Distribution-or-sdist)
whereas the `.whl` file is a [built
distribution](https://packaging.python.org/en/latest/glossary/#term-Built-Distribution).
Newer pip versions preferentially install built distributions, but will fall
back to source distributions if needed. You should always upload a source
distribution and provide built distributions for the platforms your project is
compatible with.

First register an account on
[TestPyPI](https://test.pypi.org/account/register/), which is a separate
instance of the package index intended for testing and experimentation. Then
verify your email address and then [generate a PyPI API
token](https://test.pypi.org/manage/account/#api-tokens). You will need to
setup two-factor authentication first; just follow the account instructions.

Install Twine.

```console
# activate environment, if you haven't already
source venv/bin/activate
python3 -m pip install --upgrade twine
```

Run Twine to upload all of the archives under `dist`. You will be prompted for
a username and password. For the username, use `__token__`. For the password, use
the token value, including the pypi- prefix.

```console
cd packaging_tutorial/
python3 -m twine upload --repository testpypi dist/*

# Uploading example_package_davetang-0.0.1-py3-none-any.whl
# Uploading example_package_davetang-0.0.1.tar.gz
#
# View at:
# https://test.pypi.org/project/example-package-davetang/0.0.1/
```

Now to install your package!

```console
python3 -m pip install --index-url https://test.pypi.org/simple/ --no-deps example-package-davetang
# Looking in indexes: https://test.pypi.org/simple/
# Collecting example-package-davetang
#   Obtaining dependency information for example-package-davetang from https://test-files.pythonhosted.org/packages/b4/55/780e7cc89dafbd024fe744f865f23f25694b43c6ddc42d72ae310d5acc1a/example_package_davetang-0.0.1-py3-none-any.whl.metadata
#   Downloading https://test-files.pythonhosted.org/packages/b4/55/780e7cc89dafbd024fe744f865f23f25694b43c6ddc42d72ae310d5acc1a/example_package_davetang-0.0.1-py3-none-any.whl.metadata (678 bytes)
# Downloading https://test-files.pythonhosted.org/packages/b4/55/780e7cc89dafbd024fe744f865f23f25694b43c6ddc42d72ae310d5acc1a/example_package_davetang-0.0.1-py3-none-any.whl (2.5 kB)
# Installing collected packages: example-package-davetang
# Successfully installed example-package-davetang-0.0.1
```

And finally to test it.

```console
./test.py
# 1984
```

That's it!

```console
deactivate
```
