#!/usr/bin/env python
#
# https://bradmontgomery.net/blog/pythons-zip-map-and-lambda/
#

a = [1, 2, 3, 4, 5]
b = [2, 2, 9, 0, 9]

# merge a and b into one list, keeping whichever value is the largest at each
# index
def pick_the_largest(a, b):
    result = []
    for i in range(len(a)):
        result.append(max(a[i], b[i]))
    return result

print(pick_the_largest(a, b))

# zip takes two equal-length collections and merges them together in pairs
my_pair = zip(a, b)
print(list(my_pair))

# lambda is a shorthand for creating anonymous functions
# it can take a parameter and returns the value of an expression
# lambda <input>: <expression>
x = lambda a, b, c : a + b + c
print(x(1900, 80, 4))

# map takes a function and applies it to each item in an iterable
# map(func, iter)
print(list(map(lambda x: x + 10, a)))

# pick the largest using map lambda zip
print(list(map(lambda pair: max(pair), zip(a, b))))
