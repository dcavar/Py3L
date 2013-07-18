#!/usr/bin/env python3

"""
This is our fun library function collection for
processing text files in the Python course at
LSA 2013 etc.
"""

import re
from operator import itemgetter


# open file and read content
def loadTextFromFile(filename):
    """Load text from a file and return the string of the content."""

    mytext = ""
    #print("Test message from loadTextFromFile", filename)
    try:
        ofp = open(filename, mode='r', encoding='utf-8')
        # process the file content
        mytext = ofp.read()
        ofp.close()
    except IOError:
        print("File", filename, "cannot be read!")
    return mytext


def tokenize(sometext):
    #return re.split("(\W)", sometext)
    tokens = re.split("\W", sometext)
    tokens = [ x for x in tokens if x not in [ "" ] ]
    return tokens


def getNGrams(tokenlist, n=2):
    mydict = {}

    for pos in range(len(tokenlist) - (n - 1)):
        ngram = tokenlist[pos:pos + n]
        ngram = " ".join(ngram)
        #print( ngram )
        mydict[ngram] = mydict.get(ngram, 0) + 1
    return mydict


def getTokenCounts(tokenlist):
    mydict = {}
    for token in tokenlist:
        if token in " \n,.?!()[];:`-'\"":
            continue
        #if token in mydict:
        #    mydict[token] = mydict[token] + 1
        #else:
        #    mydict[token] = 1
        # we reduced the four lines above to this one simple line
        mydict[token] = mydict.get(token, 0) + 1
    return mydict


def relativizeTokenCounts(somedict):
    total = sum( somedict.values() )
    if total <= 0:
        return
    for key in somedict:
        somedict[key] = somedict[key] / total


def prettyPrintFrequencyProfile(frqprofile, sortbyfrq=True, myreverse=True):
    myitems = frqprofile.items()
    if sortbyfrq:
        myitems = sorted(myitems, key=itemgetter(1), reverse=myreverse)
    else:
        myitems = sorted(myitems, key=itemgetter(0), reverse=myreverse)
    for x in myitems:
        print(x[0], x[1], sep="\t")


