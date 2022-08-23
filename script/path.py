#!/usr/bin/env python
#
# working with paths
#

# https://docs.python.org/3/library/os.path.html
import os

# https://docs.python.org/3/library/sys.html
import sys

# PYTHONPATH (akin to PERL5LIB) is an environment variable set to
# add additional directories where Python will look for modules
# use `sys.path` to show directories (and order) where Python looks for modules
# this includes PYTHONPATH

# first looks in current directory, then PYTHONPATH, then system-wide
print(sys.path)

# get environment variable
home = os.environ['HOME']

# add another module directory but to the end of the list
sys.path.append(f'{home}/my_python_modules_last')
print(sys.path)

# add another module directory but to the start of the list by using index 0
# sys.path.insert = insert(index, object, /) method of builtins.list instance
sys.path.insert(0, f'{home}/my_python_modules_first')
print(sys.path)

# depending on how this script is run, __file__ will return different values
print("printing __file__ returns: [{}]".format(__file__))

# saw this in someone's code
print('/'.join(os.path.realpath(__file__).split('/')[:-1]))

# like realpath in coreutils; symlinks will return their real path
realpath = os.path.realpath(__file__)
print("realpath = {}".format(realpath))

# same as dirname but here I included trailing /
print("dirname = {}".format(os.path.dirname(realpath) + '/'))

# same as basename
print("basename = {}".format(os.path.basename(__file__)))

