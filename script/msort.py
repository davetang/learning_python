#!/usr/bin/env python
#
# An implementation of a merge sort using recursion (with a lot of print
# statements to figure out what is going on). The function will recursively
# split a list down until there are n lists with only one item; a list of one
# is sorted. Then the function will rewind (I do not know the proper term for
# when a recursive function returns to the previous call), merging and sorting
# each of the individual lists together, until there is one final sorted list.
#

from random import shuffle, seed

def msort(my_list, name):
    global counter
    counter += 1
    name = " ".join([name, str(counter)])
    print("[ Call {} ] Running msort with {}: {}".format(counter, name, my_list))
    if len(my_list) > 1:
        print("\t--- Splitting ---")
        mid = len(my_list) // 2
        left_half = my_list[:mid]
        right_half = my_list[mid:]
        print("\tLeft half before msort: {}".format(left_half))
        print("\tRight half before msort: {}".format(right_half))
        msort(left_half, "left half")
        print("\tLeft half after msort: {}".format(left_half))
        msort(right_half, "right half")
        print("\tRight half after msort: {}".format(right_half))

        left_ind = 0
        right_ind = 0
        my_list_ind = 0

        print("\t### Sorting ###")
        print("\tName status: {}".format(name))
        while left_ind < len(left_half) and right_ind < len(right_half):
            if left_half[left_ind] <= right_half[right_ind]:
                my_list[my_list_ind] = left_half[left_ind]
                left_ind += 1
            else:
                my_list[my_list_ind] = right_half[right_ind]
                right_ind += 1
            my_list_ind += 1

        while left_ind < len(left_half):
            my_list[my_list_ind] = left_half[left_ind]
            left_ind += 1
            my_list_ind += 1

        while right_ind < len(right_half):
            my_list[my_list_ind] = right_half[right_ind]
            right_ind += 1
            my_list_ind += 1

        print("\tLeft status: {}".format(left_half))
        print("\tRight status: {}".format(right_half))
        print("\tList status: {}".format(my_list))
    print("\t$$$ {} sorted $$$".format(name))

my_num = list(range(1, 11))
seed(1984)
shuffle(my_num)
print("Original: {}".format(my_num))
counter = 0
msort(my_num, "full list")
print("Sorted: {}".format(my_num))

