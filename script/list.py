#!/usr/bin/env python
#
# working with lists
#

sentence = "the quick brown fox jumps over the lazy dog"
words = sentence.split(' ')

# printing a list
print("Different ways to print a list\n")
print("print(words) = ", words)

# read as join(' ', words)
print("print(' '.join(words)) = ", ' '.join(words))
print("print('#'.join(words)) = ", '#'.join(words))

# the * operator can be used to unpack an iterable when calling a function
print("print(*words) = ", *words, "\n")

print("Different methods for lists\n")
# remove last item and save in variable
last_word = words.pop()
print("Using pop() removed %s from words:" %last_word)
print("\t", *words)

animal = 'cat'
words.append(animal)
print("Using append() added %s to words:" %animal)
print("\t", *words)

print("Slicing with words[3:5] does not include the end index =", words[3:5])

# https://www.w3schools.com/python/python_lists_comprehension.asp
# list comprehension is used to create a new list based on an existing list
#
# the syntax is:
#     newlist = [expression for item in iterable if condition == True]

# create new list of words that contain the letter "o"
has_o = [x for x in words if "o" in x]
print(f'Within the list {words}, the following contain the letter "o":', *has_o)

# create a list of nine zeros
print([0 for i in range(9)])

# create a list of list
print("A list of list")
nrow, ncol = [9, 9]
m = [[0 for i in range(ncol)] for j in range(nrow)]
m[4][4] = 5
for i in m:
    print(i)
