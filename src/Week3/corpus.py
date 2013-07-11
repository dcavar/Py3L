#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re


def getTextFromFile(filename):
   """Reads content from filename and returns the text as a string."""
   # we need a text variable to store the content
   # of the file
   mytext = ""

   # open a file and read the text into memory
   try:
      myfile = open(filename, mode='r', encoding='utf-8')
      mytext = myfile.read()
      myfile.close()
   except IOError:
      pass
   except FileNotFoundError:
      pass
   return mytext


def tokenize(sometext):
   """Returns a list of tokens generated using re.split() and
   the regular expression (\W)"""

   # return re.split("(\W)", sometext)
   return re.split("\W", sometext)


def relativizeFP(fp):
   total = sum(fp.values())
   for key in fp:
      fp[key] = fp[key] / total


def getNGramModel(tokens, n):
   mydict = {}
   position = 0
   for x in tokens[0:-(n-1)]:
      ngram = " ".join( tokens[ position : position + n ] )
      mydict[ngram] = mydict.get(ngram, 0) + 1
      #print( ngram )
      position += 1
   relativizeFP(mydict)
   return mydict


def makeFrequencyProfile(tokenlist):
   """Count elements in the tokenlist"""
   # count tokens and generate a frequency profile
   mydict = {}
   for token in tokenlist:
      #if token in mydict:
      #   mydict[token] = mydict[token] + 1
      #else:
      #   mydict[token] = 1
      mydict[token] = mydict.get(token, 0) + 1
   return mydict


def prettyPrintFRP(fp, byfrequency=True, reverse=False):
   myitems = sorted( fp.items() )
   for x in myitems:
      print(x)
   




def removeJunk(somedict, junksymbols):
   """ """
   for token in junksymbols:
      if token in somedict:
         del somedict[token]


