#!/usr/bin/env python3


# mydict = {  "pas":"Hund", "konj":"Pferd"  }

mydict = {  }

character = "a"

if character in mydict:
   mydict[character] = mydict[character] + 1
else:
   mydict[character] = 1

character = "a"

if character in mydict:
   mydict[character] = mydict[character] + 1
else:
   mydict[character] = 1

print(mydict)
