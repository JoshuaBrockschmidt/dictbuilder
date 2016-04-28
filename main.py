#!/usr/bin/env python3

"""TODO:
 * more flexible sorting options
 * make help
"""

import getopt, json, sys

def usage():
    print("usage: TODO")#TODO

# Parse command-line arguments
try:
    opts, args = getopt.getopt(sys.argv[1:], 'hi:o:', ['help', 'input=', 'output='])
except getopt.GetoptError as e:
    print('GetoptError while parsing command-line argument: {}'.format(e))
    usage()
    sys.exit(2)

outFn = None
inFn = []
for o, arg in opts:
    if o in ('-h', '--help'):
        usage()
        sys.exit(0)
    elif o in ('-i', '--input'):
        inFn.append(arg)
    elif o in ('-o', '--output'):
        outFn = arg
    else:
        print('Unrecognized argument {}'.format(o))
        sys.exit(2)

if len(inFn) <= 0:
    print('No input file/s specified')
    sys.exit(2)

# Parse file/s
defs = {}
for fn in inFn:
    with open(fn, 'r') as f:
        try:
            newDefs = json.load(f)
        except ValueError as e:
            print('ValueError in {}: {}'.format(inFn, e))
            sys.exit(1)
        defs.update(newDefs)

# Sort words
sort = sorted(defs, key=str.lower)

# Print or write file
def outputDict(stream=sys.stdout):
    print('# My Dictionary', file=stream)
    print('\n## Definitions', file=stream)
    curLetter = None
    for k in sort:
        l = k[0].upper()
        if curLetter != l:
            curLetter = l
            print('\n### {}'.format(curLetter), file=stream)
        word = k[0].upper() + k[1:]
        print('* *{}* - {}'.format(word, defs[k]), file=stream)

if outFn == None:
    outputDict()
else:
    with open(outFn, 'w') as f:
        outputDict(f)
