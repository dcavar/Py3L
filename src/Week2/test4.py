#!/usr/bin/env python3
# -*- coding: utf-8 -*-

mytext = "Hello world"

mycharacters = list(mytext)
mycharacters[1] = "a"

# merge list of strings back to a string
print( "-".join(mycharacters)  )


print( mytext[2] )

mytext = "Hallo Welt!"
print(mytext)

# we cannot change characters in a string this way!
#mytext[1] = "e"

print( mytext + " " + mytext )
print( (mytext + " ") * 3 )
