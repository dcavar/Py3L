#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
(C) 2013 by Damir Cavar, Lwin Moe

N-gram model from text and generation of DOT-representation (Graphviz).
"""


from ngrams import makeNgramModel
from operator import itemgetter
import urllib.request, re

req = urllib.request.Request('http://www.gutenberg.org/cache/epub/873/pg873.txt')
response = urllib.request.urlopen(req)
the_page = response.read()
# convert the bytearray to a string object
the_page = the_page.decode('utf-8')
the_page = re.sub("[\"\';:,.<>?!()-_*+=\/\[\]\{\}]", " ", the_page)

fp = makeNgramModel(the_page.lower().split(), 2)

tuplelist = fp.items()

print("digraph X {")
for token, frq in sorted(tuplelist, key=itemgetter(1), reverse=True):
   tokens = token.split()
   if len(tokens[0]) == 0:
      continue
   if len(tokens[1]) == 0:
      continue
   print(tokens[0] + ' -> ' + tokens[1] + ' ;')
print("}")

