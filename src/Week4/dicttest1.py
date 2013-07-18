#!/usr/bin/env python3

mydict = { "Kuh":["cow","krowa", "krava"], "Fisch":["fish", "ryba"] }

mydict["Hund"] = ["dog", "pies"]
mydict["Katze"] = ["cat", "kot"]
mydict["Maus"] = ["mouse", "misz"]
mydict["Maus"] = mydict["Maus"] + [ 0 ]

print(mydict["Hund"][1])

print(mydict)
