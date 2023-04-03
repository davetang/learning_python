#!/usr/bin/env python3
#
# Working with dictionaries with the items(), keys(), and values() methods
#

# Japanese prefecture codes
codes = {
    'Tokyo' : 520,
    'Kanagawa': 530,
    'Osaka' : 840,
    'Chiba' : 510,
    'Saitama' : 430
}

# Dictionaries are ordered as of Python version 3.7
# convert codes into strings using str() for printing purposes
# since the join method is only for the string class
print("Printing codes in the original order\n")
for pref, code in codes.items():
    print(' -> '.join(str(x) for x in [pref, code]))
print()

print("Printing codes sorted by code value\n")
# https://stackoverflow.com/questions/674509/how-do-i-iterate-over-a-python-dictionary-ordered-by-values
for pref, code in sorted(codes.items(), key = lambda x: x[1]):
    print(pref, ":", code)
print()

# get value or assign None
tokyo_code = codes.get('Tokyo', None)
if tokyo_code:
    print("Tokyo has the prefecture code %d" % tokyo_code)
else:
    print("Tokyo is not in the codes dictionary")

kyoto_code = codes.get('Kyoto', None)
if kyoto_code:
    print("Kyoto is abbreviated as %d" % kyoto_code)
else:
    print("Kyoto is not in the codes dictionary")
print()

# storing keys and values as lists
print("The list of cities:")
cities = list(codes.keys())
print(cities)
print("The list of prefecture codes:")
pcodes = list(codes.values())
print(pcodes)

# keys are iterable
for city in codes.keys():
    print(city)
