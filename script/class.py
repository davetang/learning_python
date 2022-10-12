#!/usr/bin/env python
#
# https://docs.python.org/3/tutorial/classes.html
#
# A class is like a blueprint or definition for creating or rather
# instantiating an object. Python classes provide a means of bundling data and
# functionality together. Creating a new class creates a new type of object,
# allowing new instances of that type to be made.
#
# https://docs.python.org/3/tutorial/classes.html#a-first-look-at-classes
#
# the simplest form of a class definition:
#
# class ClassName:
#     <statement-1>
#     ...
#     <statement-N>
#
# https://docs.python.org/3/tutorial/classes.html#class-objects
#
# Class objects support two kinds of operations: attribute references and
# instantiation. Attribute references use the standard syntax used for all
# attribute references in Python: `obj.name`. Valid attribute names are all the
# names that were in the class's namespace when the class object was created.
# The only operations understood by instance objects are attribute references.
# There are two kinds of valid attribute names: data attributes and methods. A
# method is a function that belongs to an object.
# 
# The special thing about methods is that the instance object is passed as the
# first argument of the function. If x is an instance of MyClass, then x.f() is
# exactly equivalent to MyClass.f(x).
#
# class MyClass:
#     """A simple example class"""
#     i = 12345
#
#     def __init__(self, name):
#         self.name = name
#
#     def f(self):
#         return 'hello world'
#
# With the class definition above, MyClass.i and MyClass.f are valid attribute
# references, returning an integer and a function object, respectively. When a
# class defines the special method named `__init__()`, class instantiation
# automatically invokes __init__() for the newly created class instance.
#
# https://docs.python.org/3/tutorial/classes.html#private-variables
#
# There is a convention in Python that a name prefixed with an underscore (e.g.
# _spam) should be treated as a non-public part of the API.
#

# It is not necesarry to include `object` in Python3. If it is included, it
# reads as "class foobar is a class of type object".
class foobar(object):
    # self is a variable for the object being accessed
    def __init__(self, passed):
        self.passed = passed

    def echo(self):
        print(self.passed)

# Class instantiation uses function notation but is a parameterless function
# that returns a new instance of the class. The code below creates a new
# instance of foobar and assigns this object to the local variable my_obj.
my_obj = foobar("wind")

print(type(my_obj))

# add a new data attribute not defined in the class
my_obj.counter = 1
while my_obj.counter < 10:
    my_obj.counter = my_obj.counter * 2
print(my_obj.counter)

# the dir() function will return all functions and properties of a class
print("\n".join(dir(my_obj)), "\n")

print("type(my_obj) returns {}".format(type(my_obj)))
my_obj.echo()

#
# Inheritance
#
# https://docs.python.org/3/tutorial/classes.html#inheritance
#
# The syntax for a derived class definition:
#
# class DerivedClassName(BaseClassName):
#     <statement-1>
#     ...
#     <statement-N>
#
# The syntax for multiple inheritance:
#
# class DerivedClassName(Base1, Base2, Base3):
#     <statement-1>
#     ...
#     <statement-N>
#
# The search for attributes occurs depth-first, left-to-right, and not
# searching twice in the same class when there is an overlap in the hierarchy.
# But it is slightly more complex with the method resolution order changing
# dynamically to support cooperative calls to super().
#

# implicit inheritance
class Parent(object):
    def implicit(self):
        print(f"{self} PARENT's implicit()")

class Child(Parent):
    # the pass statement is used as a placeholder for future code
    pass

print("Override example")
# implicit() function not defined in Child but inherited
child = Child()
child.implicit()

# override
class Child_override(Parent):
    def implicit(self):
        print(f"{self} CHILD's implicit()")

child_override = Child_override()
child_override.implicit()

print("Using super() example")
# use super() to call parent's inheritance for an altered function
class Child_super(Parent):
    def implicit(self):
        print(f"{self} CHILD, before super()")
        # this will call Parent.implicit
        super(Child_super, self).implicit()
        print(f"{self} CHILD, after super()")

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

print("Composition example")
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

#
# __init__ is executed last!
#

class Spam:
    print("Before __init__")
    def __init__(self):
        print("Inside __init__")
    def ham(self):
        print("In ham method")
    print("After __init__")

Spam()

#
# if __init__ is overriden in a subclass, is super __init__ called?
# The answer is no, which I had suspected but wanted to check.
#

class BaseSpam:
    def __init__(self):
        self.x = 1984

class SubSpam:
    x = 1985
    def __init__(self):
        self.y = 2020
        # variables declared in the class are accessed by prefixing with self
        # NameError: name 'x' is not defined
        # print(x)
        print(self.x)
        # variables declared in the method, can be accessed as is
        z = 2022
        print(z)

ss = SubSpam()
print(ss.x)
print(ss.y)
