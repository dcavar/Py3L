#!/usr/bin/env python3


mytext = "Hello world"

mydict = {}

for x in mytext:
   if x in mydict:
      mydict[x] = mydict[x] + 1
   else:
      mydict[x] = 1

try:
   print( mydict["a"] )
except KeyError:
   print(0)

print( mydict.get("a", 0) )

print(mydict)


