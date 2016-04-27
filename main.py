#!/usr/bin/env python3

"""TODO:
 * more flexible sorting options
 * use -o to specify output file
 * check more explicitly for errors in JSON files
"""

import json, sys

if len(sys.argv) > 1:
    inFn = sys.argv[1]

with open(inFn, 'r') as f:
    try:
        defs = json.load(f)
    except:
        sys.exit('{} has a syntax error'.format(inFn))

sort = sorted(defs)

print('# Definitions')
for k in sort:
    print('* {}: {}'.format(k, defs[k]))
