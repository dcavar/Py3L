#!/usr/bin/env python3


from operator import itemgetter


mytext = ""

try:
    myfile = open("pg873.txt", mode='r', encoding='utf-8')
    mytext = myfile.read()
    myfile.close()
except IOError:
    print("Cannot read from file...")
except FileNotFoundError:
    print("Cannot find the file...")

tokens = mytext.split()
mytext = ""
types = set(tokens)


print("Number of tokens:", len(tokens) )
print("Number of types:", len(types) )

mycounts = {}
for x in tokens:
    if x in mycounts:
        mycounts[x] = mycounts[x] + 1
    else:  # x is not a key in mycounts
        mycounts[x] = 1

#print(mycounts)

# print the dictionary in a nicer line by line way
#for x in mycounts:
#    print(x, mycounts[x], sep="\t")

myitems = mycounts.items()

myitems = sorted(myitems, reverse=False, key=itemgetter(1))
#print(myitems)

for x in myitems:
    print(x[0], x[1], sep="\t")

#print(mycounts.items())

#print(mycounts)

