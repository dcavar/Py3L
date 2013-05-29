#!/usr/bin/env python3

"""
This is some comment.
We want to tokenize text and count the words in the text.
Let us see what the result is.
"""

fp = open("test4.py", mode="r")

text = fp.read()

fp.close()


print(text.split())

frequencyprofile = {  }

for token in text.split():
   frequencyprofile[token] = frequencyprofile.get(token, 0) + 1

for key in frequencyprofile:
   print(key, frequencyprofile[key])

# print(frequencyprofile)
