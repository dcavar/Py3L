#!/usr/bin/env python3

"""
(C) 2013 by Damir Cavar

Make sure that you paste some German and English text for
the extraction of language models in text-de-1.txt and
text-en-1.txt. The more text you put in these files,
the better it should be for your model generation.
"""

# https://github.com/dcavar/Py3L

from ngrams import makeNgramModel

# read file
ifp = open("text-de-1.txt", mode='r', encoding='utf8')
mytext = ifp.read()
ifp.close()

mymodel_de = makeNgramModel(mytext, 3)

total = sum(mymodel_de.values())

for key, value in mymodel_de.items():
    mymodel_de[key] = value / total
#    print(key, mymodel_de[key])


# read file
ifp = open("text-en-1.txt", mode='r', encoding='utf8')
mytext = ifp.read()
ifp.close()

mymodel_en = makeNgramModel(mytext, 3)

total = sum(mymodel_en.values())

for key, value in mymodel_en.items():
    mymodel_en[key] = value / total
#    print(key, mymodel_en[key])


mytext = "Dies ist ein kleiner Test."

mymodel_unk = makeNgramModel(mytext, 3)

total = sum(mymodel_unk.values())

en_dist = 0.0
de_dist = 0.0
for key, value in mymodel_unk.items():
    mymodel_unk[key] = value / total
    en_dist += abs(mymodel_en.get(key, 1) - mymodel_unk[key])
    de_dist += abs(mymodel_de.get(key, 1) - mymodel_unk[key])

print(mytext)

print(en_dist, de_dist)

if en_dist < de_dist:
    print("This text is English!")
else:
    print("This text is German!")

