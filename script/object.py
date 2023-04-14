#!/usr/bin/env python3
#
# Python objects/instances introspection
#

# https://stackoverflow.com/questions/1006169/how-do-i-look-inside-a-python-object
def introspection(obj):
    print(f"type(obj) returns {type(obj)}\n")
    print(f"dir(obj) returns {dir(obj)}\n")
    print(f"id(obj) returns {id(obj)}\n")
    print(f"globals() returns {globals()}\n")
    print(f"locals() returns {locals()}\n")
    print(f"callable(obj) returns {callable(obj)}\n")
    print(f"obj.__dict__ returns {obj.__dict__}\n")
    print(f"vars(obj) returns {vars(obj)}\n")
    print(f"getattr(obj, 'allow_abbrev') returns {getattr(obj, 'allow_abbrev')}\n")
    print(f"hasattr(obj, 'allow_abbrev') returns {hasattr(obj, 'allow_abbrev')}\n")

import argparse
parser = argparse.ArgumentParser()
parser.add_argument(
        "-v",
        "--verbose",
        help = "verbose mode",
        action = "store_true"
)

introspection(parser)

# pretty print
from pprint import pprint
pprint(vars(parser))
