#!/usr/bin/env python3
# -*- coding: utf-8 -*-


mydict = { "to":35, "the":278, "in":23 }

print(mydict)
print( list(mydict.keys()) )
print( sum(mydict.values()) )


def test1(somedict):
   if "to" in somedict:
      del somedict["to"]

test1(mydict)
print(mydict)
