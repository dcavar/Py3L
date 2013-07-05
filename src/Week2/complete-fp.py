#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from operator import itemgetter
import re

mytext = ""

try:
    ofp = open("pg873.txt", mode='r', encoding='utf-8')
    # process the file content
    mytext = ofp.read()
    ofp.close()
except IOError:
    pass

#tokens = mytext.split()
tokens = re.split("(\W)", mytext)
#print(tokens)


mydict = {}
for token in tokens:
    if token in " \n,.?!()[];:`-":
        continue
    if token in mydict:
        mydict[token] = mydict[token] + 1
    else:
        mydict[token] = 1

myitems = mydict.items()
myitems = sorted(myitems, key=itemgetter(1), reverse=True)

for x in myitems:
    print(x[0], x[1], sep="\t")


