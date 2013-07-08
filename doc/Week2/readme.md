# 2nd Week assignments

(C) 2013 by [Malgosia Cavar] and [Damir Cavar]

*Python 3 for Linguists*. Class material, example code, scripts and example data.

For more details see:

* [Python 3 for Linguists]


---

## Assignments

### 1. Debug this code!

What is wrong with the code in files:

* [problem1.py](problem1.py)
* [problem2.py](problem2.py)
* [problem3.py](problem3.py)
* [problem4.py](problem4.py)


---

### 2. Coding tasks

Solve one of the next problems. If you want to make up for another assignment, choose a second one. If you want, solve all assignments.


---

#### 2.1. Remove stop-words from dictionaries

When generating frequency profiles of tokens from text, how can we remove [stop words](https://en.wikipedia.org/wiki/Stop_words) from the frequency profiles? Imagine, you use a function like ``makeFrequencyProfile(tokenlist)`` in ``codrpus.py`` that returns a frequency profile as a dictionary data structure. Or, alternatively, in file ``complete-fp.py`` after line 30 insert a code to remove all [stop words](https://en.wikipedia.org/wiki/Stop_words).

* Where can you find a list of stop-words for your specific language?
* How can we convert this list into a useful data-structure in Python?
* How do we remove tokens from a dictionary data-structure?


---

#### 2.2. Generate N-gram models

An N-gram model here is simply a frequency profile of not one token, but for example a sequence of tokens that occur next to each other in text. With ``n=2`` a bigram model of the text ``"Hello how are you"`` could be:

	Hello how	1
	how are	1
	are you	1

Use file ``list-loop-1.py`` and modify it such that we have a function that gets two parameters: a list of tokens, and n = the size of the N-grams

	def getNGramList(tokenlist, n):
		...

The function should return a list of N-grams of size ``n`` (with ``n >= 1``), generated from a ``tokenlist`` of strings.


---

#### 2.3. Generate a list of reverted tokens

We generate a list of tokens from a text. Use any of the previous code examples for that.

We want to print a token list of reverse strings, i.e. from ``cat`` we want to generate ``tac``. We do not need duplicates, so we can use for example the ``set(sometokenlist)`` function to generate a set of tokens, before we reverse all the tokens.

One can reverse a string by using the following notation:

	mystring = "cat"
	print( mystring[ : : -1 ] )

The interpretation is that we take a slice of string ``mystring`` from the beginning to its end (``mystring[ : ]``), i.e. the default for the start-index is 0, the default for the end-index is the length of the string. The final ``-1`` in the code above is a stepper that implies "take every character, starting from the end of the string", thus the reversion of the string results.

You might need a loop to go through the list of tokens and append the reversed token to a new list of reverse strings. Appending strings to a list can be achieved using such a code:

	mylist = [ ]
	mylist.append( mystring[ : : -1 ] )



---

## Reading

We were talking about Regular Expressions, Regular Grammars, Finite State Automata. Please read the following two documents for the next week:

* [Wikipedia Regular Expression article](http://en.wikipedia.org/wiki/Regular_expression)
* [Python 3 documentation introduction of the re-module](http://docs.python.org/3/library/re.html#module-re)
* [Python Regular Expression HOWTO](http://docs.python.org/3/howto/regex.html)

You can test regular expressions online. There are various tools in the internet. The one that we used in class is:

* [regexpal](http://regexpal.com/)




[Damir Cavar]: http://cavar.me/damir/ "Damir Cavar"
[LSA Summer Institute 2013]: http://lsa2013.lsa.umich.edu/ "LSA Summer Institute 2013"
[Malgosia Cavar]: http://cavar.me/malgosia/ "Malgosia Cavar"
[Python.org]: http://www.python.org/ "Python.org"
[Python]: http://www.python.org/ "Python"
[University of Michigan]: http://www.umich.edu/ "University of Michigan"
[Python 3 for Linguists]: http://dl.dropbox.com/u/11318112/Python34Ling/index.html "Python 3 for Linguists"
[-> Main course page]: http://dl.dropbox.com/u/11318112/Python34Ling/index.html "Main course page"
[LSA 2013 Registration Information]: http://lsa2013.lsa.umich.edu/about/registration-information/ "LSA 2013 Registration Information"

