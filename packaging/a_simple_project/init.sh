#!/usr/bin/env bash
#
# https://packaging.python.org/en/latest/tutorials/packaging-projects/
#
# Project name: example_package_${username}

set -euo pipefail

username=davetang
name="Dave Tang"
email='me@davetang.org'
year=2023

mkdir -p packaging_tutorial/{tests,src/example_package_${username}}

touch packaging_tutorial/src/example_package_${username}/__init__.py
touch packaging_tutorial/{LICENSE,pyproject.toml,README.md}

# create example module
cat <<EOF > packaging_tutorial/src/example_package_${username}/example.py
def add_one(number):
    return number + 1
EOF

# populate pyproject.toml
#
# requires is a list of packages that are needed to build the package
# build-backend is the name of the Python object that frontends will use to
# perform the build
#
# For the project metadata specification, see:
#
#     https://packaging.python.org/en/latest/specifications/declaring-project-metadata/#declaring-project-metadata
#
cat <<EOF > packaging_tutorial/pyproject.toml
[build-system]
requires = ["hatchling"]
build-backend = "hatchling.build"

[project]
name = "example_package_${username}"
version = "0.0.1"
authors = [
  { name="${name}", email="${email}" },
]
description = "A small example package"
readme = "README.md"
requires-python = ">=3.7"
classifiers = [
    "Programming Language :: Python :: 3",
    "License :: OSI Approved :: MIT License",
    "Operating System :: OS Independent",
]

[project.urls]
"Homepage" = "https://github.com/pypa/sampleproject"
"Bug Tracker" = "https://github.com/pypa/sampleproject/issues"
EOF

cat <<EOF > packaging_tutorial/README.md
# Example Package

This is a simple example package. You can use
[Github-flavored Markdown](https://guides.github.com/features/mastering-markdown/)
to write your content.
EOF

cat <<EOF > packaging_tutorial/LICENSE
MIT License

Copyright (c) ${year} ${name}

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
EOF

>&2 echo Done
exit 0
