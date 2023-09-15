#!/usr/bin/env python
#
# Directory stuff
#

import os

# recursive listing of files
# os.walk() returns:
# 1. path to the directory
# 2. list of sub-directories
# 3. list of files in the path
for root, dirs, files in os.walk('.'):
    for f in files:
        print(os.path.join(root, f))
