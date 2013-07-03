#!/usr/bin/env python3

mytext = "Hello world"

mydict = {}

for x in mytext:
   mydict[x] = mydict.get(x, 0) + 1

print( mydict.get("a", 0) )

print(mydict)
