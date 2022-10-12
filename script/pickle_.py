#!/usr/bin/env python
#
# Pickling is used to store Python objects.
#

import pickle
import os

my_dict = {
    "one"   : 1,
    "two"   : 2,
    "three" : 3,
    "four"  : 4
}

# export using dump
fn = "my_dict.pickle"
outfile = open(fn, "wb")
pickle.dump(my_dict, outfile)
outfile.close()

# import using load
infile = open(fn, "rb")
my_dict_imp = pickle.load(infile)
infile.close()

print(f"Original dictionary: {my_dict}")
print(f"Imported dictionary: {my_dict_imp}")

os.unlink(fn)
