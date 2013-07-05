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

   return re.split("(\W)", sometext)



def makeFrequencyProfile(tokenlist):
   """ """
   # count tokens and generate a frequency profile
   mydict = {}
   for token in tokenlist:
      if token in mydict:
         mydict[token] = mydict[token] + 1
      else:
         mydict[token] = 1
   return mydict




def removeJunk(somedict, junksymbols):
   """ """
   for token in junksymbols:
      if token in somedict:
         del somedict[token]


