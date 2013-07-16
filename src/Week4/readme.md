# Code for the 4th Week of Python 3 for Linguists

(C) 2013 by [Malgosia Cavar] and [Damir Cavar]


## Generating DOT-transition graphs from N-gram models

Run the script ``make-ngram.py`` and set the correct text-file in line 9:

	myngrams = getNGrams(tokenize( loadTextFromFile("bbc-1.txt") ))

Use a file-name of a file that you really have on your system. It will write out a conversion of the N-gram model to DOT in a file called ``test2.dot``. You can find more about the [DOT Documentation] online.

We are using here a very simple subset of the DOT-language elements and capabilities. Every bigram is translated to:

	the -> house;

This is translated to a two state graph with a transition from ``the`` to ``house``. The entire list of such directed graphs is wrapped to one coherent graph by surrounding it with curly brackets and labeling the directed graph (i.e. ``dirgraph``) with some arbitrary name:

	dirgraph mygraph {
	...
	}




## N-grams to graphs using Graphviz

Download [Graphviz] and install it. There is a version for the most common operating systems on the download page. After you installed [Graphviz], open the Viewer (on Macs this is [Graphviz], on Windows it might be called something else?).

Make sure that you do not double click on the ``.dot``-files, since they might be mistaken as Word template files by your operating system. Open them in [Graphviz] and let it generate the transition graph.




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
[Graphviz]: http://www.graphviz.org/ "Graphviz"
[DOT Documentation]: http://www.graphviz.org/content/dot-language "DOT Documentation"

