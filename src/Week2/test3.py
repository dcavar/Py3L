#!/usr/bin/env python3

mytext = "hello world"

print(mytext[1])
print(mytext[2:4])
print( mytext[0: : 2 ] )

print(mytext.center(46))

print("Number of es in mytext:", mytext.count("e"))

print(mytext.endswith("ld"))

mytext = mytext.capitalize()

print(mytext)
