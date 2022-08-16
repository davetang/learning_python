#!/usr/bin/env python
#
# an unnecessary module created for testing purposes
#

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

