#!/usr/bin/env bash
#
# Written by Dave Tang
# Year 2023
#
set -euo pipefail

if [[ -x $(command -v python3) ]]; then
   >&2 echo python3 executable found
else
   >&2 echo Could not find python3
   exit 1
fi

# see https://docs.python.org/3/library/venv.html
python3 -m venv venv
source venv/bin/activate

python_bin=$(command -v python3)
pip_bin=$(command -v pip3)
>&2 echo Using Python in ${python_bin}
>&2 echo Using pip in ${pip_bin}

read -p "Continue y/[n]? " continue
if [[ ! ${continue} == "y" ]]; then
   >&2 echo Exiting...
   exit 1
fi

# upgrade pip
${pip_bin} install --upgrade pip

deactivate
>&2 echo Enter the following command to use the virtual environment:
>&2 echo source venv/bin/activate
>&2 echo Done
exit 0
