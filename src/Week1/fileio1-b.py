#!/usr/bin/env python3



myfile = open("sample1.txt", mode='r', encoding='utf-8')

mytext = myfile.read()

myfile.close()

print(mytext)
