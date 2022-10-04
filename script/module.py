#!/usr/bin/env python
#
# access a function in a module using the syntax:
#
#     module_name.function_name
#

import maths

# https://note.nkmk.me/en/python-import-usage/
# import only one item and as an alias
from root import newtons_method as sqrt

print("2 + 2 =", maths.two_num(2, 2, '+'))

my_num = 8128
divisors = [1]
for i in range(2, my_num):
    if maths.two_num(my_num, i, '%') == 0:
        divisors.append(i)
print('Divisors of %d (apart from itself)' % my_num, 'are:', *divisors)

divisor_sum = 0
for n in divisors:
    divisor_sum += n
print('The sum of the divisors of %d is %d' % (my_num, divisor_sum))

# accessing a variable from the maths module
print("my_seed in the maths module is %d" % maths.my_seed)

print(f"the square root of {my_num} is {sqrt(my_num)}")

