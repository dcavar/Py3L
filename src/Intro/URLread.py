
"""
(C) 2013 by Damir Cavar

Reading remote text from URL.
"""



import urllib.request

req = urllib.request.Request('http://www.gutenberg.org/cache/epub/873/pg873.txt')
response = urllib.request.urlopen(req)
the_page = response.read()

the_page = str(the_page).replace("\\r\\n", "\n")
print(the_page)


#lines = str(the_page).split("\\r\\n")
#for line in lines:
#   print(line)
