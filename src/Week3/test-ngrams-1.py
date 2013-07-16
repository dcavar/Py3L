#!/usr/bin/env python3

from corpus import loadTextFromFile, getNGrams, getTokenCounts, prettyPrintFrequencyProfile, relativizeTokenCounts, tokenize
from math import log



def getMIScore(bigramprob, unigramprobaA, unigramprobB):
    return bigramprob * log(bigramprob / (unigramprobaA * unigramprobB) )

def getMIScoreFromFQP( bigrams, unigrams, bigram):
    tokenA, tokenB = bigram.split()
    return bigrams[bigram] * log( bigrams[bigram] / (unigrams[tokenA] * unigrams[tokenB]) )



tokens = tokenize( loadTextFromFile("pg873.txt") )

unigrams = getNGrams(tokens, 1)
relativizeTokenCounts( unigrams )

bigrams = getNGrams(tokens, 2)
#prettyPrintFrequencyProfile(bigrams, myreverse=False)

relativizeTokenCounts( bigrams )


# young King: likelihood ratio
lhr = bigrams["young Fisherman"] / (unigrams["young"] * unigrams["Fisherman"])

# young King - pointwise Mutual Information
pmi = bigrams["young Fisherman"] * log( lhr )

print("young Fisherman", lhr, pmi, sep="\t")

# iron chain: likelihood ratio
lhr = bigrams["iron chain"] / (unigrams["iron"] * unigrams["chain"])

# iron chain - pointwise Mutual Information
pmi = bigrams["iron chain"] * log( lhr )

print("iron chain", lhr, pmi, sep="\t")
print("iron chain", getMIScoreFromFQP(bigrams, unigrams, "iron chain") )
print("young Fisherman", getMIScoreFromFQP(bigrams, unigrams, "young Fisherman") )
