#!/usr/bin/env python3

from operator import itemgetter


mydict = { "the":2384, "to":1298, "house":45, "a":1800 }

print( list(mydict.keys()) )
print( list(mydict.values()) )
print( list(mydict.items()) )

myitems = sorted(mydict.items(), reverse=True, key=itemgetter(1))
print(myitems)

#myitems = mydict.items()
#for x in myitems:
#    print(itemgetter(1)(x))  # x[1]



