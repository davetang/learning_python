#!/usr/bin/env python
#
# Regular expressions in Python
#
import re
#
# https://note.nkmk.me/en/python-re-match-object-span-group/
#
# In Python's re module, `match()` and `search()` return match objects when a
# string matches a regex; `match()` checks for a match only at the beginning
# and `search()` checks for a match anywhere. Use the methods provided by the
# match object to extract the matched string and its position.
#
# re.match(pattern, string)
#
# Match pattern from the beginning of the string and returns a match object if the pattern matches at the start of the string, otherwise None.
# Used to ensure that the pattern occurs only at the beginning of the string.
#
# re.search(pattern, string)
#
# Searches for the first occurrence of the pattern anywhere in the string.
# Returns a match object for the first occurrence of the pattern, or None if the pattern is not found.
# Used to find the first occurrence of the pattern anywhere in the string.
#
# re.findall(pattern, string)
#
# Finds all occurrences of the pattern in the string and returns them as a list or if no matches are found, an empty list is returned.
# Used when you want to find all occurrences of the pattern, not just the first one.

# use the re.VERBOSE flag to allow comments and whitespace in your regex for better readability.
# also use raw strings (r'') to avoid problems with Python escaping special characters like \.

pattern = re.compile(r"""
    \d+    # Match one or more digits
    [a-z]* # Match zero or more lowercase letters
""", re.VERBOSE)

result = pattern.search('123abc')

# use re.sub() to perform text replacements.
text = "Setting: {{something_to_change}}"
result = re.sub(r'{{something_to_change}}', 'new_setting', text)
print(result)

# re.findall() returns a list of all matches, while re.finditer() returns an iterator yielding match objects. The latter is more memory efficient, especially for large texts.
pattern = re.compile(r'\d+')
# Using finditer (returns iterator of match objects)
matches = pattern.finditer('123 abc 456 def 789')
print(type(matches))
for match in matches:
    print(match.group())

# Using Flags for Case-Insensitive and Multiline Matching
# use flags like re.IGNORECASE (or re.I) for case-insensitive matching and re.MULTILINE (or re.M) to allow ^ and $ to match the start and end of each line in multiline strings.
text = "First Line\nsecond line"

# Case-insensitive match
pattern = re.compile(r'second', re.IGNORECASE)
print(pattern.search(text))

# Multiline mode
pattern = re.compile(r'^second', re.MULTILINE)
print(pattern.search(text))

# Regular expressions are greedy by default, meaning they match as much text as possible. To make a pattern non-greedy, use the ? modifier after the quantifier (*, +, etc.).
text = "<html>content</html>"

# Greedy match (matches the whole string)
pattern = re.compile(r'<.*>')
print(f"Greedy: {pattern.search(text).group()}")

# Non-greedy match
pattern = re.compile(r'<.*?>')
print(f"Non-greedy: {pattern.search(text).group()}")

#      01234567890123456789012345678901234567890
#                    ||||||           ||||||
dna = "ATGACAGATAGACAGAATTCAGATAGACGATAAGCTTAGTA"

# returns None because only looks at the beginning
n = re.match(r'GAATTC', dna)
print(n)

# returns a Match object
n = re.match(r'ATGACA', dna)
print(n)

m = re.search('GAATTC', dna)
print(m)

# Match methods
# group(): Returns the matched string.
# start(), end(): Returns the start and end positions of the match.
# span(): Returns a tuple with the start and end positions.
print(f"start of match (zero-based): {m.start()}")
print(f"end of match: {m.end()}")
print(f"span of match: {m.span()}")
print(f"match: {m.group()}")

# groups
# Use Non-Capturing Groups (?:...) for Grouping Without Capturing
pattern = re.compile(r'(?:http|https)://')
result = pattern.search('https://davetang.org')
print(f"Non-capturing group: {result.group(0)}")

g = re.search('(GAATTC)[ACGT]+(AAGCTT)', dna)
print(f"group match: {g}")

print(f"first group (entire match): {g.group(0)}")
print(f"second group: {g.group(1)}")
print(f"third group: {g.group(2)}")

# Use Named Groups for Readability
# Instead of referring to captured groups by index (\1, \2, etc.), you can name your groups with (?P<name>...) and access them by name.
g = re.search('(?P<EcoRI>GAATTC)[ACGT]+(?P<HindIII>AAGCTT)', dna)
print(f"EcoRI: {g.group('EcoRI')}")
print(f"HindIII: {g.group('HindIII')}")

# https://stackoverflow.com/questions/2241600/python-regex-r-prefix
#
# The r prefix indicates that the following is a raw string.
#
# When an "r" or "R" prefix is present, a character following a backslash is included in the string without change, and all backslashes are left in the string.
#
# For example, the string literal r"\n" consists of two characters: a backslash and a lowercase "n".

print("test\n")
print(r"raw: test\n")
print(r"raw: test\\n")

s = r'\\[ACGT]'
print(f"\nSubject string used for matching (raw): {s}")

regex = '\\[ACGT]'
print(f"Regex (not raw): {regex}")
m = re.search(regex, s)
print(f"Match object:\n{m}\n{m.group()}\n")

print(f"Regex (raw): {s}")
mr = re.search(s, s)
# None
print(mr)

# https://stackoverflow.com/questions/13902132/regex-deal-with-double-backslash
# the r prefix turns the double backslack into two double backslackes
print(list(r'\\['))
print(list('\\['))
print(list(r'\['))
print(list(r'\\\\\['))

print("\nTesting the r prefix")
s = r'\\[ACGT]'
# this is how I can get a match but it is confusing to me because I still need to escape when using the r prefix?
print(re.search(r'\\\\\[ACGT\]', s).group())
print(re.search(r'\\{2}\[ACGT\]', s).group())

print("\nTesting lookahead and lookbehind")
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

print("\nCompiling a regex")
#
# It is not necessary to compile a pattern beforehand; `re.match()`, `re.search()`, and `re.findall()` will automatically compile the pattern internally.
#
# However, compiling the pattern using re.compile() offers some advantages such as efficiency and reuse.

# compile pattern
pattern = re.compile(r'\d+')

# reuse pattern
print(pattern.search('abc123'))

# call other methods on the same pattern
print(pattern.findall('abc123xyz456'))

# more efficient when pattern has already been compiled
strings = ['alskdjf', 'alksdj1242', 'l34j1lkj24jlk2', 'akls2111']
for string in strings:
    print(f'Searching string "{string}" with pattern "{pattern.pattern}": {pattern.findall(string)}')
