#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import sys, codecs, re
sys.stdout = codecs.getwriter('utf-8')(sys.stdout.detach())

try:
   inputfile = open("grammar-2.txt", mode='r', encoding='utf-8')

   mygrammar = {}
   for line in inputfile.readlines():
      match = re.search("\s*(?P<lhs>\w+)\s*->\s*(?P<rhs>(\w+\s*)+)(#.*)?", line)
      if match:
         print(line.strip())
         mygrammar[match.group("lhs")] = match.group("rhs")
         print(match.group("lhs"), "->", match.group("rhs"))

   inputfile.close()
except IOError:
   print("Cannot read file...")


