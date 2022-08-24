#!/usr/bin/env python3

# https://docs.python.org/3/library/collections.html
from collections import defaultdict

# https://stackoverflow.com/questions/5900578/how-does-collections-defaultdict-work
# Usually, a Python dictionary throws a KeyError if you try to get an item with
# a key that is not currently in the dictionary. The defaultdict in contrast
# will simply create any items that you try to access (provided of course they
# do not exist yet). To create such a "default" item, it calls the function
# object that you pass to the constructor (more precisely, it's an arbitrary
# "callable" object, which includes function and type objects).

# this following code would fail if a "normal" dictionary was used because the
# first time a letter is encountered, a key does not exist. By using
# `defaultdict` and `int`, an integer object 0 is assigned for keys that do not
# exist yet.
s = 'mississippi'
d = defaultdict(int)
# iterate through each letter in s
for k in s:
    d[k] += 1

# count of each letter
print(d.items())

