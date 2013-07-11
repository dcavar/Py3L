#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from corpus import getTextFromFile, makeFrequencyProfile, tokenize, getNGramModel, prettyPrintFRP, relativizeFP


# stopwordsEN = "a,able,about,across,after,all,almost,also,am,among,an,and,any,are,as,at,be,because,been,but,by,can,cannot,could,dear,did,do,does,either,else,ever,every,for,from,get,got,had,has,have,he,her,hers,him,his,how,however,i,if,in,into,is,it,its,just,least,let,like,likely,may,me,might,most,must,my,neither,no,nor,not,of,off,often,on,only,or,other,our,own,rather,said,say,says,she,should,since,so,some,than,that,the,their,them,then,there,these,they,this,tis,to,too,twas,us,wants,was,we,were,what,when,where,which,while,who,whom,why,will,with,would,yet,you,your".split(",")
stopwordsEN = ['a', 'able', 'about', 'across', 'after', 'all', 'almost', 'also', 'am', 'among',
               'an', 'and', 'any', 'are', 'as', 'at', 'be', 'because', 'been', 'but', 'by', 'can',
               'cannot', 'could', 'dear', 'did', 'do', 'does', 'either', 'else', 'ever', 'every',
               'for', 'from', 'get', 'got', 'had', 'has', 'have', 'he', 'her', 'hers', 'him',
               'his', 'how', 'however', 'i', 'if', 'in', 'into', 'is', 'it', 'its', 'just',
               'least', 'let', 'like', 'likely', 'may', 'me', 'might', 'most', 'must', 'my',
               'neither', 'no', 'nor', 'not', 'of', 'off', 'often', 'on', 'only', 'or', 'other',
               'our', 'own', 'rather', 'said', 'say', 'says', 'she', 'should', 'since', 'so',
               'some', 'than', 'that', 'the', 'their', 'them', 'then', 'there', 'these', 'they',
               'this', 'tis', 'to', 'too', 'twas', 'us', 'wants', 'was', 'we', 'were', 'what',
               'when', 'where', 'which', 'while', 'who', 'whom', 'why', 'will', 'with', 'would',
               'yet', 'you', 'your']
stopwordsEN = stopwordsEN + [ x.capitalize() for x in stopwordsEN ]
#print(stopwordsEN)


mytokens = tokenize( getTextFromFile("pg873.txt") )

# filter out empty string tokens
mytokens = [ x  for x in mytokens if x ]
#print(mytokens)

# filter out stopwords
mytokens = [ x  for x in mytokens if x not in stopwordsEN ]
#print(mytokens)

unigrams = getNGramModel(mytokens, 1)
bigrams  = getNGramModel(mytokens, 2)

#print(unigrams)

# prettyPrintFRP(bigrams, myreverse=False)

youngF = unigrams["young"]
FishermanF = unigrams["Fisherman"]
youngFishermanF = bigrams["young Fisherman"]
total = sum(unigrams.values())

observationtable = [ [ youngFishermanF,          FishermanF - youngFishermanF ],
                     [ youngF - youngFishermanF, (total - youngF) - (FishermanF - youngFishermanF)  ] ]
print(observationtable)

expectationtable = [ [ (sum(observationtable[0]) * (observationtable[0][0] + observationtable[1][0])) / total  ],
                     [] ]
print(expectationtable)


chi2 = (observationtable[0][0] - expectationtable[0][0]) ** 2 / expectationtable[0][0]
print("Chi2-score:", chi2)

relativizeFP(unigrams)
relativizeFP(bigrams)

print("\n\nProbability ratio:")
print("P(young Fisherman):", bigrams["young Fisherman"])
print("P(young) * P(Fisherman):", unigrams["young"] * unigrams["Fisherman"])
print("P(young Fisherman) / ( P(young) * P(Fisherman) ):",  bigrams["young Fisherman"] / (unigrams["young"] * unigrams["Fisherman"]))


