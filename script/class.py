#!/usr/bin/env python
#
# A class is like a blueprint or definition for creating or rather instantiate an object
#

# it is not necesarry to include `object` after the name of the class in Python3
# if it is included, it reads as "class foobar is a class of type object"
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

#
# Inheritance
#
# package related code into modules
#

# implicit inheritance
class Parent(object):
    def implicit(self):
        print("PARENT's implicit()")

class Child(Parent):
    # the pass statement is used as a placeholder for future code
    pass

# implicit() function not defined in Child but inherited
child = Child()
child.implicit()

# override
class Child_override(Parent):
    def implicit(self):
        print("CHILD's implicit()")

child_override = Child_override()
child_override.implicit()

print("super() test")
# use super() to call parent's inheritance for an altered function
class Child_super(Parent):
    def implicit(self):
        print("CHILD, before super()")
        super(Child_super, self).implicit()
        print("CHILD, after super()")

child_super = Child_super()
child_super.implicit()

# one use case of super()
# use super() with __init__
class Child(Parent):
    def __init(self, var):
        # set variable and then initialise with Parent.__init__
        self.var = var
        super(Child, self).__init__()

#
# Composition
#
# package code into modules that are used in many unrelated places
#

class Friend(object):
    def spam(self):
        print("Friend's spam")

class Me(object):
    def __init__(self):
        self.friend = Friend()
    def spam(self):
        self.friend.spam()
    def mine(self):
        print("My spam")

me = Me()
me.spam()
me.mine()

