#!/usr/bin/env python
#
# File input and output
#

import os

sentence = "the quick brown fox jumps over the lazy dog"
outfile = 'fileio_output.txt'
with open(outfile, 'w') as f:
    for word in sentence.split(' '):
        f.write(f"{word}\n")

text_block = """\
---- start heredoc ----
multiline that doesn't need escaping
another line
    but spaces    at the start are removed when writing out
      output redirection preserves the spacing
use .format() for variable interpolation
output file is: {}
---- end heredoc ----""".format(outfile)

print(text_block)

# print or write to file
with open(outfile, 'a') as f:
    print(text_block, file = f)
    f.write(text_block)

print(f"\n=== Reading contents of {outfile} ===")
with open(outfile, 'r', encoding='utf8') as f:
    # a file object is an iterable object
    for line in f:
        print(line.strip())
print(f"=== Finished reading contents of {outfile} ===")

os.unlink(outfile)
