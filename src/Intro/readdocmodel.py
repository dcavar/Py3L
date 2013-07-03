#!/usr/bin/env python3

import glob, sys
from docmodel import tokenize
from math import log


def readModel(filename):
   myfp = {}
   try:
      fp = open(filename, mode='r', encoding='utf-8')
      for line in fp.readlines():
         key, value = line.split()
         myfp[key] = float(value)
      fp.close()
   except IOError:
      pass
   return myfp


def calculateSimilarity(filename, models):
   tokens = tokenize(open(filename, mode='r', encoding='utf-8').read())
   m1 = log(1)
   m2 = log(1)
   for x in tokens:
      m1 += log(models[0].get(x, 0.0000000001))
      m2 += log(models[1].get(x, 0.0000000001))
   if m1 < m2:
      return 2
   else:
      return 1


if __name__ == "__main__":
   models = []
   names = []
   for filename in glob.glob("*.dat"):
      names.append(filename)
      models.append(readModel(filename))
   for filename in sys.argv[1:]:
      closest = calculateSimilarity(filename, models)
      print(closest, filename)
   print(names)
   
   

