#!/usr/bin/env python3

mytext = "Hello world"


def changeText(sometext):
   sometext = "Hallo Welt!"
   return sometext


print( changeText(mytext) )
print(mytext)


mydict = { "dog":"Hund", "cat":"Katze" }

def changeDict(somedict):
   somedict["mouse"] = "Maus"

changeDict(mydict)

print(mydict)
