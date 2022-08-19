#!/usr/bin/env python
#
# A class is like a blueprint or definition for creating or rather instantiate an object
#

class foobar(object):
    # __init__ is called to initialise an empty object
    # self is a variable for the object being accessed
    def __init__(self, passed):
        self.passed = passed

    def echo(self):
        print(self.passed)

# call a class like a function to instantiate an object
# the object is assigned to a variable for working with
my_obj = foobar("wind")

# the dir() function will return all functions and properties of a class
print("\n".join(dir(my_obj)), "\n")

print("type(my_obj) returns {}".format(type(my_obj)))
my_obj.echo()

