#!/usr/bin/env python3

# -*- coding: UTF-8 -*-

import sys, codecs

sys.stdout = codecs.getwriter('utf-8')(sys.stdout.detach())

# use this and then prefix all function names with corpus.
#import corpus
# or use this
from corpus import loadTextFromFile, tokenize, getTokenCounts, prettyPrintFrequencyProfile, relativizeTokenCounts

from math import log


mytext = loadTextFromFile("pg873.txt")

# tokenize mytext and return list of tokens
tokens = tokenize(mytext)

# count tokens
mydict = getTokenCounts(tokens)
relativizeTokenCounts(mydict)

# pretty-print tokens and frequencies
#prettyPrintFrequencyProfile(mydict, sortbyfrq=True, myreverse=True)

mytext = loadTextFromFile("sports-bbc.txt")
mysportsdict = getTokenCounts(tokenize(mytext))
relativizeTokenCounts(mysportsdict)

unknowntext = """Yesterday we scored ten goals in the last 45 minutest of the game."""


"""
Wimbledon 2013: Andy Murray's victory could boost British tennis
Comments (149)
All too often sporting moments and achievements are given a misplaced historical significance. Not on Sunday.
Andy Murray made genuine history on Wimbledon's Centre Court by winning the men's singles in straight sets against Serb Novak Djokovic to become the first British male champion since Fred Perry in 1936.
    Murray got to the top not because of the Lawn Tennis Association and this country's development programmes but in spite of them
Comparisons of this nature are always pretty futile, but as achievements go it ranks alongside England's World Cup triumph in 1966, England's Rugby World Cup victory in 2003 and Sir Bradley Wiggins ending Britain's long wait for a winner of the Tour de France.
But in some ways, Murray's achievement surpasses all those. For Wimbledon to host the greatest tennis tournament in the world for so many years without a winner or even a serious challenger has been a serious embarrassment. 
"""


"""
The young fisherman likes pomegranates.
"""


ukntokens = tokenize(unknowntext)
hpgprob = 0.0
bbcprob = 0.0
for token in ukntokens:
    hpgprob += log(mydict.get(token, 0.000000000001))
    bbcprob += log(mysportsdict.get(token, 0.000000000001))
if hpgprob > bbcprob:
    print("This is probably related to the House of Pomeg.")
else:
    print("This is probably related to BBC Sports articles")
print("hpgprob:", hpgprob)
print("bbcprob:", bbcprob)
