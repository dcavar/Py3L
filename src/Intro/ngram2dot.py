#!/usr/bin/env python3


from ngrams import makeNgramModel
from operator import itemgetter
import urllib.request, re

req = urllib.request.Request('http://www.gutenberg.org/cache/epub/873/pg873.txt')
response = urllib.request.urlopen(req)
the_page = response.read()
the_page = str(the_page).replace("\\r\\n", "\n")
the_page = the_page.replace("\\", " ")
the_page = re.sub("[;:,.<>?!()\\-_*+=/\"'\[\]]", " ", the_page)

fp = makeNgramModel(the_page.lower().split(), 2)

tuplelist = fp.items()

print("digraph X {")
for token, frq in sorted(tuplelist, key=itemgetter(1), reverse=True):
   tokens = token.split()
   if len(tokens[0]) == 0:
      continue
   if len(tokens[1]) == 0:
      continue
   print(tokens[0] + ' -> ' + tokens[1] + ' ;')
print("}")

