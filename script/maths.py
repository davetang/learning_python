#!/usr/bin/env python
#
# an unnecessary module created for testing purposes
#

# https://docs.python.org/3/library/operator.html
import operator

# define a function
def two_num(x, y, o):
    if o == '+':
        return(operator.add(x,y))
    elif o == '-':
        return(operator.sub(x,y))
    elif o == '*':
        return(operator.mul(x,y))
    elif o == '/':
        return(operator.truediv(x,y))
    elif o == '%':
        return(operator.mod(x,y))
    else:
        return(None)

# define a variable
my_seed = 1984

# if executed as a script
if __name__ == '__main__':
    print("two_num(8000, 128, '+') returns {}".format(two_num(8000, 128, '+')))
    print("two_num(64, 127, '*') returns {}".format(two_num(64, 127, '*')))

