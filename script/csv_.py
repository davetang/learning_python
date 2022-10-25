#!/usr/bin/env python3
#
# Read and write CSV
#
# https://docs.python.org/3/library/csv.html#dialects-and-formatting-parameters
#
# Points to note are the use of a "unix" dialect, which will terminate each
# line with a newline character instead of a return carriage AND a newline
# character, which seems to be the default.
#
# In addition, QUOTE_MINIMAL is used, which will only quote fields that contain
# special characters such as the comma delimiter.
#

import sys
import csv
from os.path import dirname,basename,splitext

script_dir = dirname(__file__)

fn = "iris.csv"
bn = splitext(basename(fn))[0]

in_csv = script_dir + "/../data/" + fn
out_csv = script_dir + "/../data/" + bn + "_out.csv"

with open(in_csv) as csvfile:
    reader = csv.reader(csvfile)
    with open(out_csv, 'w', newline = '', encoding = 'utf-8') as outfile:
        writer = csv.writer(outfile, dialect = 'unix', quoting = csv.QUOTE_MINIMAL)
        for row in reader:
            # row is a list
            # print(type(row))
            writer.writerow(row)

sys.exit()
