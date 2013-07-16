#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import sys, codecs
sys.stdout = codecs.getwriter('utf-8')(sys.stdout.detach())

from corpus import loadTextFromFile, tokenize, getNGrams

myngrams = getNGrams(tokenize( loadTextFromFile("bbc-1.txt") ))

try:
    outfile = open("test2.dot", mode="w", encoding="utf-8")
    print("digraph g {", file=outfile)
    for bigram in myngrams:
        tokens = bigram.split()
        print('"' + tokens[0] + "\" -> \"" + tokens[1] + "\";", file=outfile)
    print("}", file=outfile)
    outfile.close()
except IOError:
    pass

