#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import sys, codecs
sys.stdout = codecs.getwriter('utf-8')(sys.stdout.detach())

from corpus import loadTextFromFile, tokenize, getNGrams

mytext = loadTextFromFile("cnn-1.txt")
mytokens = tokenize(mytext)
myngrams = getNGrams(mytokens, 2)

try:
   outputfile = open("sample-a1.dot", mode='w', encoding='utf-8')

   print("digraph test {", file=outputfile)
   for bigram in myngrams:
      lefttoken, righttoken = bigram.split()
      print('"' + lefttoken + '"' + " -> " + '"' + righttoken + '"' + ";", file=outputfile)
   print("}", file=outputfile)

   outputfile.close()
except IOError:
   print("Cannot open file...")

