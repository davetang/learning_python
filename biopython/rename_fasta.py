#!/usr/bin/env python3
#
# Written by Dave Tang
# Year 2023
#

import argparse
import sys
import re
import os.path
from Bio import SeqIO
ver = "0.1.0"
parser = argparse.ArgumentParser()

#
# positional arguments
#

# default type is string
parser.add_argument(
        "fasta",
        help = "FASTA file"
)

parser.add_argument(
        "regex",
        help = 'Regex for capturing ID, e.g. "transcript:(\w+)"'
)

#
# optional arguments
#

# short and long options
# store True if specified
parser.add_argument(
        "-b",
        "--verbose",
        help = "verbose mode",
        action = "store_true"
)
parser.add_argument(
        "-v",
        "--version",
        help = "show script version and exit",
        action = "version",
        version = ver
)

args = parser.parse_args()

if os.path.exists(args.fasta):
    for seq in SeqIO.parse(args.fasta, "fasta"):
        fid = seq.description
        if re.search(args.regex, seq.description):
            fid = re.sub(f".*{args.regex}.*", r'\1', seq.description)
        print(f">{fid}\n{seq.seq}")
else:
    print(f"{args.fasta} does not exist")
    quit(1)
