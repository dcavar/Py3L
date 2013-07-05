#!/usr/bin/env python3
# -*- coding: utf-8 -*-

mytext = "hello world"

print(mytext[1])
print(mytext[2:4])
print( mytext[0: : 2 ] )


print(mytext.center(80))

print("Number of es in mytext:", mytext.count("e") )

print("Number of lds in mytext:", mytext.count("ld") )

print(mytext.endswith("ing"))

print(mytext.capitalize())
mytext = mytext.capitalize()

print(mytext)
