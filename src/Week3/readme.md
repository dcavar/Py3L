# Code for the 3rd Week of Python 3 for Linguists

(C) 2013 by [Malgosia Cavar] and [Damir Cavar]


## List comprehension

Filtering elements from a list can be achieved in many ways. We could construct a loop and try to save only the appropriate list elements to a new list.

We can read a text from a file and tokenize it using the ``corpus.py`` code that we have in the Week 3 folder:

	from corpus import getTextFromFile, tokenize
	mytokens = tokenize(getTextFromFile("pg873.txt"))

The variable mytokens in this example script will hold now the tokens from the ``pg873.txt`` file. If you print the token list, you will see that it contains also space-characters as tokens, as well as newline and all punctuation characters. If you want to remove those from the token list, use for example a for-loop.

Assume that we store the symbols and characters that we want to remove in a string as follows:

	junk = " \n\t"

The ``\n``-code refers to a single newline character, and the ``\t``-code refers to a single tabulator character. Together with those two symbols/tokens we want to eliminate all space-tokens from the list, that is ``" "``-tokens. We create a new empty list ``mynewtokens`` that will hold the tokens from ``mytokens`` without the unnecessary tokens.

	mynewtokens = []

The for-loop looks at every single token in ``mytokens``, and appends only those tokens to ``mynewtokens`` that are not characters in the ``junk``-string as declared above.

	for x in mytokens:
	   if x in junk:
	      continue
	   mynewtokens.append(x)

In the end we overwrite ``mytokens`` with a copy of ``mynewtokens``:

	mytokens = mynewtokens[:]

Instead of declaring ``junk`` to be a string, such that we filter single character-tokens from the token list ``mytokens``, we can also declare ``junk`` to be a list of strings that are longer than just one character. This way we can filter out arbitrary string elements from lists:

	junk = [ " ", "\n", "\t", "the" ]

There is a simpler way to remove elements from lists. We can use list comprehension and directly return a new list from ``mylist`` and save it as ``mytokens``. This way we avoid having to use a buffer-list like ``mynewtokens`` above.





---

[Damir Cavar]: http://cavar.me/damir/ "Damir Cavar"
[LSA Summer Institute 2013]: http://lsa2013.lsa.umich.edu/ "LSA Summer Institute 2013"
[Malgosia Cavar]: http://cavar.me/malgosia/ "Malgosia Cavar"
[Python.org]: http://www.python.org/ "Python.org"
[Python]: http://www.python.org/ "Python"
[University of Michigan]: http://www.umich.edu/ "University of Michigan"
[Python 3 for Linguists]: http://dl.dropbox.com/u/11318112/Python34Ling/index.html "Python 3 for Linguists"
[-> Main course page]: http://dl.dropbox.com/u/11318112/Python34Ling/index.html "Main course page"
[LSA 2013 Registration Information]: http://lsa2013.lsa.umich.edu/about/registration-information/ "LSA 2013 Registration Information"

