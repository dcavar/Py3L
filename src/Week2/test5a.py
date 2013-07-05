#!/usr/bin/env python3
# -*- coding: utf-8 -*-

mytext = "abcdefg"

try:
    print(mytext[2])
    print(mytext[45])
    print(mytext[3])
except IndexError:
    print("Sorry, index out of range.")


print("this is the end of the script")
