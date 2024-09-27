#!/usr/bin/env python3

from pathlib import Path
import os.path
import yaml

script_dir = os.path.dirname(__file__)

yml_file = script_dir + '/../data/simple.yml'
file = Path(yml_file)
if file.is_file() == False or file.exists() == False:
    print(f"{file} does not exist")

# https://stackoverflow.com/questions/1773805/how-can-i-parse-a-yaml-file-in-python
with open(yml_file) as stream:
    try:
        data = yaml.safe_load(stream)
    except yaml.YAMLError as exc:
        print(exc)

print(f"data is stored as {type(data)}")

if 'name' in data:
    print(f"My name is {data['name']}")
else:
    print(f"'name' does not exist in {yml_file}")
