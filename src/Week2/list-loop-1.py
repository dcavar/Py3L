#!/usr/bin/env python3
# -*- coding: utf-8 -*-


mylist = [ "A", "B", "C", "D", "E" ]

n = 4

position = 0
for x in mylist[0:-(n-1)]:
   print( " ".join( mylist[ position : position + n ] ) )
   position += 1


