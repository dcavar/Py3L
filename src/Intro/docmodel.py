#!/usr/bin/env python3

import ngrams, sys
from operator import itemgetter


stopwords = ('a', 'able', 'about', 'across', 'after', 'all', 'almost', 'also', 'am', 'among', 'an', 'and', 'any', 'are', 'as', 'at', 'be', 'because', 'been', 'but', 'by', 'can', 'cannot', 'could', 'dear', 'did', 'do', 'does', 'either', 'else', 'ever', 'every', 'for', 'from', 'get', 'got', 'had', 'has', 'have', 'he', 'her', 'hers', 'him', 'his', 'how', 'however', 'i', 'if', 'in', 'into', 'is', 'it', 'its', 'just', 'least', 'let', 'like', 'likely', 'may', 'me', 'might', 'most', 'must', 'my', 'neither', 'no', 'nor', 'not', 'of', 'off', 'often', 'on', 'only', 'or', 'other', 'our', 'own', 'rather', 'said', 'say', 'says', 'she', 'should', 'since', 'so', 'some', 'than', 'that', 'the', 'their', 'them', 'then', 'there', 'these', 'they', 'this', 'tis', 'to', 'too', 'twas', 'us', 'wants', 'was', 'we', 'were', 'what', 'when', 'where', 'which', 'while', 'who', 'whom', 'why', 'will', 'with', 'would', 'yet', 'you', 'your')




def processFile(filename, fp):
   print(filename)
   try:
      ifp = open(filename, mode='r', encoding='utf8')
      text = ifp.read()
      ifp.close()
   except IOError:
      print("Sorry, cannot read from file", filename)
   ngrams.makeNgramModel(text.split(), 1, fp)


def relativize(fp):
   total = sum(fp.values())
   if total == 0:
      return
   for token in fp:
      fp[token] = fp[token] / total


def filterStopWords(fp, stopwords):
   for key in stopwords:
      if key in fp:
         del fp[key]
      if key.capitalize() in fp:
         del fp[key.capitalize()]
   

def get100mf(fp):
   topterms = sorted(fp.items(), key=itemgetter(1), reverse=True)[ :101]
   for term in topterms:
      print(term[0], term[1], sep="\t")
   


if __name__ == '__main__':
   fp = {}
   for i in sys.argv[1:]:
      processFile(i, fp)

   relativize(fp)
   filterStopWords(fp, stopwords)
   get100mf(fp)

   #for token in fp:
   #   print(token, fp[token])
   
