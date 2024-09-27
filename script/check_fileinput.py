#!/usr/bin/env python3

from pathlib import Path
import os.path

script_dir = os.path.dirname(__file__)

file = Path(script_dir + '/../README.md')
if file.is_file() and file.exists():
    print(f"{file} exists")

directory = Path(script_dir + '/../something_that_does_not_exist')
if directory.is_dir() and directory.exists():
    print(f"{directory} exists")
else:
    print(f"{directory} does not exist")
