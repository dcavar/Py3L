#!/usr/bin/env python3

mytext = "Hello world"

print(len(mytext))

print(mytext[0])

print(mytext[1])

num = 142

try:
   print(mytext[num])
except IndexError:
   print("I am so sorry, there is no character", num, "in the string")


print("end")

