#!/usr/bin/env python3


mytext = "Hello world!"

my2ndtext = """1st line of text
This is a test.
This is the third line of text.
Last line"""

#print(my2ndtext)

lines = my2ndtext.split(sep="\n")
#print(lines)


#n = 0
#for line in lines:
#   print(n, line)
#   n = n + 1

#for n in range(len(mytext)):
#   print(n, mytext[n])

#print(lines)
#newlines = []
#n = 0
#for x in lines:
#   print(x)
#   newlines.append(str(n) + ": " + x)
#   n = n + 1
#print(newlines)

print(lines)
lines[0] = "Hello"
print(lines)

#mytuple = (1, 2, 3, 4)
#print(mytuple)
#for n in range(len( mytuple )):
#   mytuple[n] = str(n) + ": " + mytuple[n]
#print(mytuple)

mytuples = ("Hello", "a", 3, 4)
for i in mytuples:
   print(i)


# print(list(range(2, 11, 2)))

