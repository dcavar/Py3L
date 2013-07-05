#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
(C) 2013 by Damir Cavar

Reading remot texts from URL.
"""


import urllib.request, ngrams
from operator import itemgetter


response = urllib.request.urlopen("http://www.gutenberg.org/cache/epub/873/pg873.txt")
text = response.read()

text = str(text).replace("\\r\\n", "\n")

myitems = ngrams.makeNgramModel(text.split(), 3).items()
# myitems = sorted(myitems, key=lambda element: element[1], reverse=True)
myitems = sorted(myitems, key=itemgetter(1), reverse=False)
for key, value in myitems:
   print(key, value)




