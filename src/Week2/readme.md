# Code for the 2nd Week of Python 3 for Linguists

(C) 2013 by [Malgosia Cavar] and [Damir Cavar]


## Unicode output error

Some of you complained about an error in Komodo Edit, when printing Unicode characters. When you print some strings, you might see the following error message in the Komodo Edit Command Output window:

	UnicodeEncodeError: 'ascii' codec can't encode characters in position 5-7: ordinal not in range(128)

This error is caused by the fact that the standard output stream of Python is set to text mode only. One has to use the binary output stream and a handler for Unicode strings. To achieve this, you need to put the following lines of code in your Python script:

	import sys, codecs

and somewhere below that you should set the sys.stdout standard output stream to the new binary output stream with for example UTF-8 handling:

	sys.stdout = codecs.getwriter('utf-8')(sys.stdout.detach())

If you place the two lines above in the beginning of your script somewhere, Unicode output should work well in the command line and in Komodo Edit.

Have a look at the example file: ``[unicode-output.py](unicode-output.py)``. When you run this script, you should see printed common Latin-characters, some IPA-symbols, Japanese, Korean and Chinese characters, as well as some Arabic text. Make sure that you have some Unicode font on your system, otherwise you might not see any output.

As you will see in the second line of almost all Python code files now, you can set the default encoding by using the line of code:

	# -*- coding: UTF-8 -*-

Let us know, if there is a problem.


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

