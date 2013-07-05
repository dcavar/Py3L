#!/usr/bin/env python3
# -*- coding: utf-8 -*-

mytext = "Hello world how are you"

mytokens = mytext.split()

myothertokens = mytokens[:]


mytokens[0] = "Hi"


print(myothertokens)
print(mytokens)
