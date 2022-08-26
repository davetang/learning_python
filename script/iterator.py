#!/usr/bin/env python3
#
# https://dbader.org/blog/python-iterators
#

# an object is iterable if it supports the `iter` call
# support for `iter` comes from the __iter__ dunder method
class Repeater:
    def __init__(self, value):
        self.value = value

    def __iter__(self):
        return RepeaterIterator(self)

# an object is an iterator if it supports the `next` call
# support for `next` comes from the __next__ dunder method
class RepeaterIterator:
    def __init__(self, source):
        self.source = source

    def __next__(self):
        return self.source.value

repeater = Repeater('Hello')
iterator = repeater.__iter__()
print(iterator.__next__())

# iteration protocol
# any object with a __next__ method to advance to a next result, which raises
# StopIteration at the end of the series of results, is considered an iterator
class BoundedRepeater:
    def __init__(self, value, max_repeats):
        self.value = value
        self.max_repeats = max_repeats
        self.count = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.count >= self.max_repeats:
            raise StopIteration
        self.count += 1
        return self.value

repeater = BoundedRepeater('Bounded', 3)
for item in repeater:
    print(item)

