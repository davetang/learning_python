#!/usr/bin/env python
#
# Regular expressions in Python
#
# https://note.nkmk.me/en/python-re-match-object-span-group/
#
# In Python's re module, `match()` and `search()` return match objects when a
# string matches a regex; `match()` checks for a match only at the beginning
# and `search()` checks for a match anywhere. Use the methods provided by the
# match object to extract the matched string and its position.
#

import re
#      01234567890123456789012345678901234567890
#                    ||||||           ||||||
dna = "ATGACAGATAGACAGAATTCAGATAGACGATAAGCTTAGTA"

# returns None because only looks at the beginning
n = re.match(r'GAATTC', dna)
print(n)

m = re.search('GAATTC', dna)
print(m)

print(f"start of match (zero-based): {m.start()}")
print(f"end of match: {m.end()}")
print(f"span of match: {m.span()}")
print(f"match: {m.group()}")

# groups
g = re.search('(GAATTC)[ACGT]+(AAGCTT)', dna)
print(g)

print(f"first group (entire match): {g.group(0)}")
print(f"second group: {g.group(1)}")
print(f"third group: {g.group(2)}")

# named groups
g = re.search('(?P<EcoRI>GAATTC)[ACGT]+(?P<HindIII>AAGCTT)', dna)
print(f"EcoRI: {g.group('EcoRI')}")
print(f"HindIII: {g.group('HindIII')}")

# https://stackoverflow.com/questions/2241600/python-regex-r-prefix
#
# The r prefix indicates that the following is a raw string. When an "r" or "R"
# prefix is present, a character following a backslash is included in the
# string without change, and all backslashes are left in the string. For
# example, the string literal r"\n" consists of two characters: a backslash and
# a lowercase "n".
print("test\n")
print(r"test\n")
print(r"test\\n")

s = r'\\[ACGT]'
print(f"\nString to match: {s}\n")

regex = '\\[ACGT]'
print(f"Regex: {regex}")
m = re.search(regex, s)
print(f"Match\n{m}\n{m.group()}\n")

print(f"Regex: {s}")
mr = re.search(s, s)
print(mr)

# https://stackoverflow.com/questions/13902132/regex-deal-with-double-backslash
# the r prefix turns the double backslack into two double backslackes
print(list(r'\\['))
print(list('\\['))
print(list(r'\['))
print(list(r'\\\\\['))

s = r'\\[ACGT]'
# this is how I can get a match but it is confusing to me because I still need
# to escape with the r prefix?
print(re.search(r'\\\\\[ACGT\]', s).group())
print(re.search(r'\\{2}\[ACGT\]', s).group())

# Positive lookahead
# match "apple" that is followed by "pie":
text = "apple pie, apple tart, apple pied"
pattern = r"apple(?= pie)"

matches = re.findall(pattern, text)
print(matches)

# Negative lookahead
# match "apple" that is not followed by "pie":
text = "apple pie, apple tart, apple cider"
pattern = r"apple(?! pie)"

matches = re.findall(pattern, text)
print(matches)

# Positive lookbehind
# match "cake" only when it is preceded by "chocolate":
text = "chocolate cake, vanilla cake, mud cake"
pattern = r"(?<=chocolate )cake"

matches = re.findall(pattern, text)
print(matches)

# Negative lookbehind
# match "cake" that is not preceded by "chocolate":
pattern = r"(?<!chocolate )cake"

matches = re.findall(pattern, text)
print(matches)

# match a word that is preceded by "Mr." and followed by "Jr."
text = "Mr. Smith Jr., Dr. Jones Jr., Dr. Allen, Mr. Bob Sr."
pattern = r"(?<=Mr\. )\w+(?= Jr\.)"

matches = re.findall(pattern, text)
print(matches)
