#!/usr/bin/env python3
#
# https://docs.python.org/3/library/exceptions.html
#

# get class hierarchy
from inspect import getmro

# all exceptions in Python are instances of a class derived from BaseException
# https://docs.python.org/3/library/inspect.html#inspect.getmro
# Return a tuple of class cls’s base classes, including cls, in method
# resolution order.
print(f"Method resolution order of ValueError: {getmro(ValueError)}\n")

def as_int(x):
    # test code for errors
    try:
        print(f"Trying int({x})")
        int(x)
    # handle error
    except ValueError:
        return None
    # define as many exception blocks as necessary
    except:
        print("Another exception was raised")
    # this runs if no errors were raised
    else:
        print("No errors were raised")
        return(int(x))
    # runs regardless of error or not
    finally:
        print(f"try/except has finished for input [{x}]")

print(f"Running as_int(10) returns [{as_int(10)}]\n")
print(f"Running as_int('str') returns {as_int('std')}\n")

assert 2 + 2 == 4
try:
    assert 2 + 2 == 5
except:
    print("Keep going after assertion error\n")

# raise keyword to raise an exception
my_str = 8128
if not type(my_str) is str:
    raise TypeError("{} is not a string".format(my_str))
