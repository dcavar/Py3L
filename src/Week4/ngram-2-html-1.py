#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import sys, codecs
sys.stdout = codecs.getwriter('utf-8')(sys.stdout.detach())

from corpus import loadTextFromFile, tokenize, getNGrams

mytext = loadTextFromFile("cnn-1.txt")
mytokens = tokenize(mytext)
myngrams = getNGrams(mytokens, 2)

try:
   outputfile = open("sample-a1.html", mode='w', encoding='utf-8')

   print("<html>", file=outputfile)
   print("<head></head>", file=outputfile)
   print("<body>", file=outputfile)
   print("<h1>My fancy bigram model layout</h1>", file=outputfile)
   for bigram in myngrams:
      lefttoken, righttoken = bigram.split()
      print(lefttoken + " <i>" + righttoken + "</i> " + str(myngrams[bigram]) + "<br/>", file=outputfile)
   print("</body>", file=outputfile)
   print("</html>", file=outputfile)

   outputfile.close()
except IOError:
   print("Cannot open file...")

