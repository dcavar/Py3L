#!/usr/bin/env python3



myfile = open("sample2.txt", mode='r', encoding='utf-8')

mytext = myfile.read()

myfile.close()

print(mytext)
