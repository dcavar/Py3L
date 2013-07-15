# 3rd Week assignments

(C) 2013 by [Malgosia Cavar] and [Damir Cavar]

*Python 3 for Linguists*. Class material, example code, scripts and example data.

For more details see:

* [Python 3 for Linguists]


---

## Assignments

Assignment 3, Week 4

**Solve at least two of the following tasks, and if you want to compensate for missed assignments, solve one more and indicate so:**

1. Choose some collection of texts in a language of your choice. Make sure that the text is encoded in Unicode, ideally in UTF-8.
Use the code for generating token lists, frequency profiles and N-grams from our source repository and generate frequency profiles over characters, NOT word tokens. Explain your code for the generation of e.g. tri-gram character models.

2. Generate two N-gram models over characters from texts from two different languages. Use the Naive Bayesian classifier that we discussed, to identify the language of an unknown sentence or paragraph of text using these two models. Which N-gram size is ideal for your language pairs (test the efficiency, or precision on different ``n``-settings, shorter and longer text samples etc.)?

3. Generate an N-gram model of tokens for ``n>1`` from text that is not English. Find or specify a list of function words or stop words for this language in Python as a list of strings. Filter out all N-grams from your N-gram model that contain one or more stop words. Which of the remaining N-grams could be candidates for collocations, and why?

4. Summarize the statistics of the distribution of tokens with a specific suffix or prefix in text from a language of your choice. As in task 1., make sure that you use Unicode encoded texts, ideally UTF-8. For example, if you would consider English, you might want to compare the distribution of inflectional suffixes like *-ed, -s, -ing* with prefixes like *-un*. Perform such a comparison over a language of your choice. Generate the frequencies using the tokenize and N-gram generation functions that we developed, and print a summary of the frequencies and comparisons to the screen. You can use common string functions and loops to achieve this, or regular expressions over tokens. What problems did you face? How did you solve them?

5. Describe the relation between the frequency of tokens and their length. You can use the tokenize and frequency profile functions that we generated, and generate an analysis of the relation or correlation, the ratio between frequency and length, or any other metric that you might find appropriate. Use text and tokens from a language of your choice.

6. Compare the analyses from 5. between two or more languages.


### Deadline

**Submit before noon (ECT) on Monday 22nd**



---

# Project

**Deadline: Saturday 27th at noon EST**


---

## Reading

* [Jurafsky and Martin (2009) Chapter 4](http://www.cs.colorado.edu/~martin/slp.html)
* [Wikipedia N-gram](http://en.wikipedia.org/wiki/N-gram)


---

Use the code examples in the GitHub src folder of project [Py3L](https://github.com/dcavar/Py3L).

Send the resulting code file to our email addresses:

``dcavar@umich.edu``

``mcavar@umich.edu``




[Damir Cavar]: http://cavar.me/damir/ "Damir Cavar"
[LSA Summer Institute 2013]: http://lsa2013.lsa.umich.edu/ "LSA Summer Institute 2013"
[Malgosia Cavar]: http://cavar.me/malgosia/ "Malgosia Cavar"
[Python.org]: http://www.python.org/ "Python.org"
[Python]: http://www.python.org/ "Python"
[University of Michigan]: http://www.umich.edu/ "University of Michigan"
[Python 3 for Linguists]: http://dl.dropbox.com/u/11318112/Python34Ling/index.html "Python 3 for Linguists"
[-> Main course page]: http://dl.dropbox.com/u/11318112/Python34Ling/index.html "Main course page"
[LSA 2013 Registration Information]: http://lsa2013.lsa.umich.edu/about/registration-information/ "LSA 2013 Registration Information"

