#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from corpus import relativizeFP, getTextFromFile, tokenize, removeJunk
from operator import itemgetter



#mylist = [ "A", "B", "C", "D", "E", "A", "B", "C" ]

mytokens = tokenize(getTextFromFile("pg873.txt"))


# use this:

#junk = " \n\t"
#mynewtokens = []
#for x in mytokens:
#   if x in junk:
#      continue
#   mynewtokens.append(x)
#mytokens = mynewtokens[:]

# or this:
mytokens = [e for e in mytokens if e not in junk]



def getMeTheNGramModel(tokens, n):
   mydict = {}
   position = 0
   for x in tokens[0:-(n-1)]:
      ngram = " ".join( tokens[ position : position + n ] )
      mydict[ngram] = mydict.get(ngram, 0) + 1
      #print( ngram )
      position += 1
   relativizeFP(mydict)
   return mydict

unigrams = getMeTheNGramModel(mytokens, 1)
bigrams  = getMeTheNGramModel(mytokens, 2)

res = []
for x in bigrams:
   tokens = x.split()
   prob = 1
   for y in tokens:
      prob *= unigrams.get(y, 0.00000000000001)
   #print(x, bigrams[x], bigrams[x]/prob, sep="\t")
   res.append( (x, bigrams[x], bigrams[x]/prob) )

res = sorted(res, key=itemgetter(2))
for y in res:
   print(y)
