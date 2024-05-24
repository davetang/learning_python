#!/usr/bin/env python3
#
# Check whether a module is installed
#

import sys
import importlib

def is_installed(module_name):
    try:
        module = importlib.import_module(module_name, package=None)
        print(f"{module_name} is installed", file = sys.stderr)
    except:
        print(f"Please install {module_name}", file = sys.stderr)

modules_to_check = ['sys', 'does_not_exist', 'numpy', 'pickle']

for module in modules_to_check:
    is_installed(module)
