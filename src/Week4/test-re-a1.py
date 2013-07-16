#!/usr/bin/env python3


import re

mytext = "revisited calls calling called ..."

match = re.search("(?P<prefix>un|re)?(?P<root>call|visit)(?P<isuffix>s|ed|ing)?", mytext)
if match:
   print(match.groups())
   print("Prefix:", match.group("prefix"))
   print("Root:", match.group("root"))
   print("Suffix:", match.group("isuffix"))
else:
   print("No match!")
