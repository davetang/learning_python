#!/usr/bin/env python
#
# https://realpython.com/python-bitwise-operators/
#
# Most of the bitwise operators are binary, which means that they expect two
# operands to work with, typically referred to as the left and right operand.
# Bitwise NOT is the only unary bitwise operator.
#
# https://en.wikipedia.org/wiki/Bit_field
#
# A bit field is a data structure that consists of one or more adjacent bits
# which have been allocated for specific purposes, so that any single bit or
# group of bits (called a flag) within the structure can be set or inspected. A
# bit field is most commonly used to represent integral types of known, fixed
# bit-width, such as single-bit Booleans.
#
# The meaning of the individual bits within the field is determined by the
# programmer; for example, the first bit in a bit field (located at the field's
# base address) is sometimes used to determine the state of a particular
# attribute associated with the bit field.
#
# The [BAM file](https://github.com/davetang/learning_bam_file) is the de facto
# file format for storing high-throughput sequencing results. The second column
# of a BAM file specifies a bit field, which is defined below as a dictionary.
#

# store values as hexadecimal just because they are provided that way by
# samtools flag
my_field = {
    "PAIRED"         :    0x1,
    "PROPER_PAIR"    :    0x2,
    "UNMAP"          :    0x4,
    "MUNMAP"         :    0x8,
    "REVERSE"        :   0x10,
    "MREVERSE"       :   0x20,
    "READ1"          :   0x40,
    "READ2"          :   0x80,
    "SECONDARY"      :  0x100,
    "QCFAIL"         :  0x200,
    "DUP"            :  0x400,
    "SUPPLEMENTARY"  :  0x800
}

# example and expected output
# 0xa3 163 PAIRED,PROPER_PAIR,MREVERSE,READ2
my_flag = 163

# print(f"flag in decimal: {my_flag}")
# print(f"flag in binary: {my_flag:b}")
# print(f"flag in hexademical: {my_flag:x}")

my_fields = []
for field, value in my_field.items():
    # this performs a "bitwise and", which returns true when the pair of bits
    # occupying the same position in the two numbers are 1
    if my_flag & value:
        my_fields.append(field)

# mimic samtools flag 163 output
print("{}\t{}\t{}".format(hex(my_flag), my_flag, ",".join(my_fields)))

