#!/usr/bin/env python3
# -*- coding: utf-8 -*-

mytext = "Hello world"

charlist = list(mytext)

print(charlist[0])

print(charlist[0:3])

print(charlist[0: :2])

print( len(charlist) )

charlist[1] = "a"

print(charlist)

mynewtext = "".join(charlist)
print( mynewtext )





#################

mynewlist = [  ]

mynewlist.append("Hello")
mynewlist.append("world")
mynewlist.append(5674)
mynewlist.append(4.566)

myotherlist = mynewlist[:]
myotherlist.append("something")


print(mynewlist)

myothertext = mytext
myothertext = "Hallo Welt!"
print( (mytext + myothertext) * 3)







