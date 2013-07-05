#!/usr/bin/env python3
# -*- coding: utf-8 -*-

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
   if token in frequencyprofile:
      print("token is in FP")
   else:
      print("token is not in FP")
   frequencyprofile[token] = frequencyprofile.get(token, 0) + 1


for key in frequencyprofile:
   print(key, frequencyprofile[key])


# print(frequencyprofile)
