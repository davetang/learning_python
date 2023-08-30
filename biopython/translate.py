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
        "-s",
        "--skip",
        help = "skip sequences with partial codons",
        default = False,
        action = "store_true"
)
parser.add_argument(
        "-t",
        "--stop",
        help = "Stop translating on stop codon",
        default = False,
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

print(args.stop)

if os.path.exists(args.fasta):
    for seq in SeqIO.parse(args.fasta, "fasta"):
        if len(seq) % 3 and args.skip:
            if args.verbose:
                print(f"Skipping {seq.description} due to partial codon", file = sys.stderr)
        else:
            print(f">{seq.description}\n{seq.translate(to_stop=args.stop).seq}")
else:
    print(f"{args.fasta} does not exist")
    quit(1)
