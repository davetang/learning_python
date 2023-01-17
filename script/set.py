#!/usr/bin/env python3
#
# Working with sets
#
# [Set methods](https://www.w3schools.com/python/python_ref_set.asp)
# Method Description
# add()   Adds an element to the set
# clear() Removes all the elements from the set
# copy()  Returns a copy of the set
# difference()    Returns a set containing the difference between two or more sets
# difference_update()    Removes the items in this set that are also included in another, specified set
# discard()   Remove the specified item
# intersection()  Returns a set, that is the intersection of two or more sets
# intersection_update()   Removes the items in this set that are not present in other, specified set(s)
# isdisjoint()    Returns whether two sets have a intersection or not
# issubset()  Returns whether another set contains this set or not
# issuperset()    Returns whether this set contains another set or not
# pop()   Removes an element from the set
# remove()    Removes the specified element
# symmetric_difference()  Returns a set with the symmetric differences of two sets
# symmetric_difference_update()   inserts the symmetric differences from this set and another
# union() Return a set containing the union of sets
# update()    Update the set with another set, or any other iterable

sentence = "the quick brown fox jumps over the lazy dog"
words = sentence.split(' ')
words_set = set(words)

# enumerate over a list
for i, s in enumerate(words):
    print(f"List: {i} {s}")

# you can enumerate a set in the same manner as a list
# but the order is not preserved
for i, s in enumerate(words_set):
    print(f"Set: {i} {s}")

# sets are useful for determining if a list if unique
if len(words) > len(set(words)):
    print("words is not unique")
