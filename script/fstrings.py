#!/usr/bin/env python
#
# https://note.nkmk.me/en/python-f-strings/
#
# Python 3.6 introduced a new feature, known as formatted string literals, or
# f-strings, to simplify the use of the string method format().
#

# using format
a = 123
b = 'abc'
print('{} and {}'.format(a, b))
# use a placeholder
print('{first} and {second}'.format(first=a, second=b))

# f-string with different quotes but same output
print(f'{a} and {b}')
print(f"{a} and {b}")
print(f'''{a} and {b}''')
print(f"""{a} and {b}""")

# Formating occurs after the colon
## justify
print(f'right : {a:>13}')
print(f'right : {b:>13}')
print(f'center: {a:^13}')
print(f'center: {b:^13}')
print(f'left  : {a:<13}')
print(f'left  : {b:<13}')

## zero-padding
print(f'zero padding: {a:04}')

## separator
i = 1234567890

## comma
print(f'comma: {i:,}')

## convert to binary
c = 15
print(f'0b : {c:b}')

## rounding
f = 12.3456

print(f'original            : {f}')
print(f'3 decimal places    : {f:.3f}')
print(f'3 significant digits: {f:.3g}')
print(f'scientific          : {f:.3e}')
 
# From Python 3.8, f-strings support an = specifier, which prints both variable
# names and their corresponding values.
print(f'Using the = specifier : {a = }')

# works with format specification
print(f'Using the = specifier with format specification : {c = :b}')
