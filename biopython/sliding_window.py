#!/usr/bin/env python3
#
# Written by Dave Tang
# Year 2023
#

import argparse
import sys
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
        help = "FASTA file",
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
        "-w",
        "--window",
        help = "window size",
        default = 15,
        type = int
)
parser.add_argument(
        "-s",
        "--stepsize",
        help = "window size",
        default = 1,
        type = int
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
        for i in range(0, len(seq)-args.window+1, args.stepsize):
            print(f">{seq.description} {i}\n{seq.seq[i:i+args.window]}")
else:
    print(f"{args.fasta} does not exist")
    quit(1)
