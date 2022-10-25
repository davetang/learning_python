#!/usr/bin/env python
#
# Set operations https://note.nkmk.me/en/python-set/
#
# In Python, `set` is a collection of unique elements and can be used to
# perform set operations.
#
# Union: `|` or union()
# Intersection: `&` or intersection()
# Difference: `-` or difference()
# Symmetric difference: `^` or symmetric_difference()
# Test if A is a subset of B: `<=` or issubset()
# Test if A is a superset of B: `>=` or issuperset()
# Test if A and B are disjoint: isdisjoint()
#

# initialise with set() and not {}, which is for dictionaries
my_set = set()

# convert list to set
l = [1, 2, 2, 3, 1, 4]
s1 = set(l)
print(s1)

# set comprehension
s2 = {i**2 for i in s1}
print(s2)

s3 = {3, 4, 5, 6, 7}

# union
print(s1 | s2 | s3)
print(s1.union(s2, s3))

# intersection
print("Intersection between {} and {}: {}".format(s1, s3, s1 & s3))
print("Intersection between {}, {}, and {}: {}".format(s1, s2, s3, s1 & s2 & s3))

# difference
print("Difference between {} and {}: {}".format(s1, s3, s1 - s3))
print("Difference between {} and {}: {}".format(s3, s1, s3 - s1))
# from left to right
print("Difference between {}, {}, and {}: {}".format(s1, s2, s3, s1 - s2 - s3))

# symmetric difference
print("Symmetric difference between {} and {}: {}".format(s1, s3, s1 ^ s3))
print("Symmetric difference between {} and {}: {}".format(s3, s1, s3 ^ s1))
# from left to right
print("Symmetric difference between {}, {}, and {}: {}".format(s1, s2, s3, s1 ^ s2 ^ s3))

A = {0, 1}
B = {0, 1, 2, 3}

print("Is {} a subset of {}? {}".format(A, B, A <= B))
print("Is {} a superset of {}? {}".format(B, A, B >= A))

# contain no common elements
print("Are {} a and {} disjoint? {}".format(A, B, A.isdisjoint(B)))
