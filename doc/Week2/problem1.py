#!/usr/bin/env python3

mytext = ""

try:
   myfile = open("test.txt", mode='r', encoding='utf-8')
   mytext = myfile.read()
   myfile.close()
except UnicodeEncodeError:
   print("Cannot open the file.")

print(mytext)