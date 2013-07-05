#!/usr/bin/env python3
# -*- coding: utf-8 -*-


myfile = open("sample2.txt", mode='r', encoding='utf-8')

mytext = myfile.read()

myfile.close()

print(mytext)
