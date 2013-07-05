#!/usr/bin/env python3
# -*- coding: utf-8 -*-

mytext = "Hello you world how are you"

mycounts = {}

for character in mytext:
    print(character)
    print("----")
    if character in mycounts:
        mycounts[character] = mycounts[character] + 1
    else:
        mycounts[character] = 1

print(mycounts)
