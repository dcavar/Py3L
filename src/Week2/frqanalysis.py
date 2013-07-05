#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
frqanalysis.py
Open a text file, read text, tokenize it and generate a
frequency profile.
"""


from corpus import getTextFromFile, tokenize, makeFrequencyProfile, removeJunk


# mytext = getTextFromFile("pg873.txt")
# read text from file to memory and return a list of tokens
mytokens = tokenize( getTextFromFile("pg873.txt") )

mydict = makeFrequencyProfile(mytokens)

junk = " ,;:-+=()[]'\"?!$%.<>"

removeJunk(mydict, junk)

if "" in mydict:
   del mydict[""]

# generate a nice output
total = sum(mydict.values())
for token in mydict:
   print(token, mydict[token], mydict[token]/total, sep='\t')


