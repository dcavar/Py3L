#!/usr/bin/env python3

"""
so this is my large large comment and description of the code...
It goes over a couple of lines...
"""

mytext = "---"

try:
    myinputfile = open("bbc-1.txt", mode='r', encoding='utf-8')
    mytext = myinputfile.read()
    myinputfile.close()
except FileNotFoundError:
    print("Sorry, cannot find the file...")

tokens = mytext.split()
numtokens = len(tokens)
print( "Number of tokens:", numtokens )


