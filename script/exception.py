#!/usr/bin/env python3
#
# https://docs.python.org/3/library/exceptions.html
#

# get class hierarchy
from inspect import getmro

# all exceptions in Python are instances of a class derived from BaseException
print(getmro(ValueError),"\n")

def as_int(x):
    # test code for errors
    try:
        int(x)
    # handle error
    except ValueError:
        return None
    # define as many exception blocks as necessary
    except:
        print("Another exception was raised")
    # this runs if no errors were raised
    else:
        return(int(x))
    # runs regardless of error or not
    finally:
        print("try except has finished for input [{}]".format(x))

print("Running as_int(10) returns {}\n".format(as_int(10)))
print("Running as_int('str') returns {}\n".format(as_int('str')))

# raise keyword to raise an exception
my_str = 8128
if not type(my_str) is str:
    raise TypeError("{} is not a string".format(my_str))

