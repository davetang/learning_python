#!/usr/bin/env python
#
# working with loops
#

from random import shuffle, seed

sentence = "the quick brown fox jumps over the lazy dog"
words = sentence.split(' ')

# default starts at 0 but you can specify at which index to start
for i in range(1, len(words)):
    print(i)
print()

def isort(my_list):
    print("Starting insertion sort")
    total = 0
    for i in range(1, len(my_list)):
        input("Press Enter to continue for loop at index {}...".format(i))
        value = my_list[i]
        print("value is set at {}".format(value))
        while i > 0 and my_list[i-1] > value:
            input("Press Enter to continue while loop at index {}...".format(i))
            print("Setting index {} to {}".format(i, my_list[i-1]))
            my_list[i] = my_list[i-1]
            i -= 1
            print("Status: {}".format(my_list))
        input("Press Enter to continue at index {}...".format(i))
        print("Setting index {} to {}".format(i, value))
        my_list[i] = value
        print("Status: {}\n".format(my_list))
    return my_list

my_num = list(range(1, 11))
seed(1984)
shuffle(my_num)
my_num_sorted = isort(my_num)

