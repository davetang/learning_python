#!/usr/bin/env python
#
# Calculate the square root of a number using Newton's method
# https://en.wikipedia.org/wiki/Newton%27s_method#Square_root
#

import math

def f(c, x):
    return x**2 - c

def f_prime(x):
	return 2*x

def newtons_method(n, verbose = 0, f = f, f_prime = f_prime, tolerance = 0.00000001,
    max_iterations = 1000):

    """Calculate the square root of a number.

    Args:
        n: the number to get the square root of.
        verbose: verbosity.
        f: the function whose root we are trying to find.
        f_prime: the derivative of the function.
        tolerance: tolerance required.
        max_iterations: the maximum number of iterations to execute.
    Returns:
        the square root of n.
    Raises:
        TypeError: if n is not a number.
        ValueError: if n is negative.

    """

    if type(n) != int and type(n) != float:
        raise TypeError(f"must be either int or float, not {type(n).__name__}")

    if n < 0:
        raise ValueError("must not be negative")

    # initial guess
    x0 = n // 2
    # do not divide by a number smaller than this
    epsilon = 0.01

    for i in range(max_iterations):
        if verbose: print(f"iteration: {i}")
        if verbose: print(f"initial guess is {x0}")
        y = f(n, x0)
        if verbose: print(f"y is {y}")

        yprime = f_prime(x0)
        if verbose: print(f"yprime is {yprime}")

        # stop if denominator is too small
        if abs(yprime) < epsilon:
            if verbose: print("Denominator too small")
            break

        # Newton's computation
        x1 = x0 - y / yprime

        # stop when result is within desired tolerance
        if abs(x1 - x0) <= tolerance:
            if verbose: print("Tolerance met")
            return x1

        # update x0 to start the process again
        x0 = x1
        if verbose: print(f"updating guess to {x0}\n")

    # Newton's method did not converge
    return None

if __name__ == '__main__':
    num = 8128
    print(f"The square root of {num} using newtons_method() is {newtons_method(num, 1)}")
    print(f"The square root of {num} using math.sqrt() is {math.sqrt(num)}")

