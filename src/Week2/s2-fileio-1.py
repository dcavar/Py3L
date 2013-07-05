#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from operator import itemgetter

mytext = ""

try:
   myfile = open("pg873.txt", mode='r', encoding='utf-8')
   mytext = myfile.read()
   myfile.close()
except FileNotFoundError:
   print("Sorry, did not find the file...")
except IOError:
   pass

mydict = {}

tokens = mytext.lower().split()

for x in tokens:
   mydict[x] = mydict.get(x, 0) + 1

#print( "Number of characters:", len(mytext) )

print("Number of tokens:", len(tokens))
print("Number of types:", len(mydict))

total = len(tokens)
for key in mydict:
   mydict[key] = mydict[key] / total


#for key in mydict:
#   print(key, mydict[key], sep="\t")
for item in sorted(mydict.items(), reverse=False, key=itemgetter(1)):
   print(item[0], item[1], sep="\t")


