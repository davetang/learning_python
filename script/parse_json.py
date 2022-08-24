#!/usr/bin/env python3
#
# Load a JSON file into Python as a dictionary. Two ways of printing the
# dictionary: using a recursive function or using json.dumps().
#

# https://docs.python.org/3/library/json.html
import json
import argparse
import os

this_script = os.path.realpath(__file__)
eg_file = os.path.realpath(os.path.dirname(this_script) + "/../data/example.json")

parser = argparse.ArgumentParser()
# default type is string
parser.add_argument(
        "infile",
        help = "Input JSON file, e.g. {}".format(eg_file),
)
args = parser.parse_args()

with open(args.infile) as f:
    data = json.load(f)

# load into dict
print("json.load() returns {}".format(type(data)))

# recursively print out attribute-value pairs
# https://stackoverflow.com/a/10756547
def print_json(d):
    for k, v in d.items():
        # https://docs.python.org/3/library/functions.html#isinstance
        # isinstance(object, classinfo)
        # returns True if the object argument is an instance of the classinfo
        # argument. Therefore if the dictionary value is another dict, call the
        # recursive function
        if isinstance(v, dict):
            print_json(v)
        else:
            # A number in the brackets can be used to refer to the position of
            # the object passed into the str.format() method.
            print("{0} : {1}".format(k, v))

print_json(data)

# dumps into string
print("json.dumps() returns {}".format(type(json.dumps(data))))

# prettify dump
print(json.dumps(data, indent = 4, sort_keys = True))

