#!/usr/bin/env python3
#
# Written by Dave Tang
# Year 2025
#

import sys
import argparse
import os
import scanpy as sc

ver = "0.1.0"
parser = argparse.ArgumentParser()

#
# positional arguments
#

# default type is string
parser.add_argument(
        "format",
        help = "Input format (10x_mtx, 10x_h5)",
)
parser.add_argument(
        "input",
        help = "Directory or file containing the input"
)
parser.add_argument(
        "name",
        help = "Output name (without the h5ad extension)"
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

if args.verbose:
    print("Verbose mode")

formats = ['10x_mtx', '10x_h5']
if args.format in formats:
    if args.format == '10x_mtx':
        if os.path.isdir(args.input):
            adata = sc.read_10x_mtx(args.input, var_names='gene_symbols', make_unique=True)
        else:
            print(f"{args.input} does not exist", file=sys.stderr)
            sys.exit(1)
    elif args.format == '10x_h5':
        if os.path.isfile(args.input):
            adata = sc.read_10x_h5(args.input)
        else:
            print(f"{args.input} does not exist", file=sys.stderr)
            sys.exit(1)
    adata.var_names_make_unique()
    adata.write(args.name + ".h5ad")
else:
    print(f"Unexpected format: {args.format}", file=sys.stderr)
    print(f"Expected: {', '.join(f'{x}' for x in formats)}", file=sys.stderr)
    sys.exit(1)
