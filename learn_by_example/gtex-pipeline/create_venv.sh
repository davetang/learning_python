#!/usr/bin/env bash

set -euo pipefail

venv=my_venv

if [[ -d ${venv} ]]; then
   >&2 echo ${venv} already exists
else
   # see https://docs.python.org/3/library/venv.html
   python3 -m venv ${venv}
fi

source ${venv}/bin/activate
python_used=$(command -v python3)
python_expected=$(pwd)/${venv}/bin/python3
pip_used=$(command -v pip)
pip_expected=$(pwd)/${venv}/bin/pip

if [[ ${python_used} != ${python_expected} ]]; then
   >&2 echo python3 used is not the one in ${venv}/bin
   >&2 echo Used: ${python_used}
   >&2 echo Expected: ${python_expected}
fi

if [[ ${pip_used} != ${pip_expected} ]]; then
   >&2 echo pip used is not the one in ${venv}/bin
   >&2 echo Used: ${pip_used}
   >&2 echo Expected: ${pip_expected}
fi

pip install --upgrade pip

# https://github.com/bxlab/bx-python
packages=(
   bx-python
   pandas
)

for package in ${packages[@]}; do
   pip install ${package}
done

deactivate

>&2 echo Done
exit 0

