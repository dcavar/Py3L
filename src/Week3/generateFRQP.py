#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

from math import log


#import corpus
from corpus import getTextFromFile, makeFrequencyProfile, tokenize, relativizeFP

mydict = makeFrequencyProfile( tokenize( getTextFromFile("pg873.txt") ) )   
relativizeFP(mydict)

#for key in mydict:
#   print(key, mydict[key], sep="\t")

mysportsdict = makeFrequencyProfile( tokenize( getTextFromFile("sports.txt") ) )
relativizeFP(mysportsdict)

unktokens = tokenize("""
The young King was eating pomegranates and talking about his soul and other emotional issues.
""")

probpomeg = 0.0
probsports = 0.0
for token in unktokens:
   probpomeg += log(mydict.get(token, 0.00000000000001))
   probsports += log(mysportsdict.get(token, 0.00000000000001))

if probpomeg > probsports:
   print("This text is probably House of Pomeg.")
else:
   print("This text is probably a sports article.")
