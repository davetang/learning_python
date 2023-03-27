#!/usr/bin/env python3
#
# A simple script to output XML tag attributes regardless of the XML structure
#
# Written by Dave Tang
# Year 2023
#

from xml.dom.minidom import parse
import argparse
parser = argparse.ArgumentParser()

#
# positional arguments
#

# default type is string
parser.add_argument(
        "xml",
        help = "Input XML",
)
parser.add_argument(
        "tag",
        help = "Tag to extract"
)
parser.add_argument(
        "attribute",
        help = "Tag attribute to extract"
)

#
# optional arguments
#

# short and long options
# store True if specified
parser.add_argument(
        "-v",
        "--verbose",
        help = "verbose mode",
        action = "store_true"
)

args = parser.parse_args()

if args.verbose:
    print("Verbose mode")

document = parse(args.xml)

for element in document.getElementsByTagName(args.tag):
    if element.getAttribute(args.attribute):
        print(element.getAttribute(args.attribute))
