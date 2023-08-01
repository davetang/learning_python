#!/usr/bin/env python3
#
# Template script containing commonly used code snippets
#

import os
# https://stackoverflow.com/a/2725195
from os.path import dirname,basename,splitext
import sys
import re

print(f"Script using {sys.executable}", file = sys.stderr)
script_dir = dirname(__file__)

# File IO

## By far the most common task: read (CSV) file, perform some task, write out
my_csv = script_dir + '/../data/iris.csv'
my_outfile = basename(my_csv).replace('.csv', '_mod.txt')
with open(my_csv, 'r', encoding='utf8') as fi, open(my_outfile, 'w') as fo:
    # a file object is an iterable object
    for line in fi:
        # skip header
        if bool(re.search("^[a-zA-Z]", line)):
            continue
        # remove trailing whitespace
        # print(line.rstrip())
        # split into list
        var = line.split(',')
        fo.write(f"{var[0]}\n")
os.unlink(my_outfile)

# Pythonesque stuff

## list comprehension
## newlist = [expression for item in iterable if condition == True]
even_num = [x for x in range(1,11) if x % 2 == 0]
print(even_num)

# Regex

## back references, greedy and non-greedy
my_str = 'no no 2 + 2 = 4 no no'
my_sub_greedy = re.sub(r'.*(\d+).*(\d+).*', r'\1 \2', my_str)
print(my_sub_greedy)

my_sub_nongreedy = re.sub(r'.*?(\d+).*?(\d+).*', r'\1 \2', my_str)
print(my_sub_nongreedy)

# Functions

## anonymous functions
print(list(map(lambda x: x ** 2, range(11))))
