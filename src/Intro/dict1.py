# -*- coding: utf-8 -*-

"""
(C) 2013 by Damir Cavar

basic dict operations
"""


#import ngrams

from ngrams import makeNgramModel



mydict = { "dog":0,
           "cat":65,
           "cow":273646 }


mydict["cat"] = mydict["cat"] + 1

print(mydict)



print(mydict["cat"])


print( mydict.get("rabbit", 0) )


# print(makeNgramModel("This is a test".split(), 3))


print(mydict.items())
