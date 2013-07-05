#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
(C) 2013 by Damir Cavar, Malgosia Cavar

Larger comments can be marked with initial and final
trippple double-quotes.

In Komodo Edit select

Tools > Run Command...

- Make sure that the Run field contains:

   %(python3) "%F"

- The double quotes around %F seem to be necessary on systems
  like Windows, if the filename contains spaces.

- Select "Add to Toolbox" at the bottom of the dialog.

When click the "Run" button, the code will be executed, and
a run command icon appears in the Toolbox right of the editor
tab/window.

If you right-click on the "%(python3) "%F"" entry in Windows,
or control-click on Macs, you can select the Properties
entry in the pop-up-menu. There you can change the text of
the Toolbox entry to "Run in Python 3" for example, and
select the command by double-clicking on it to run the
Python 3 code in the currently opened tab or window,
independent of filename or location on your disk.
"""


# This print statement will print the two output strings
# to stdout (the screen or the Command Output window of
# Komodo Edit) with a space inbetween, because the default
# setting of print is sep=' '
print("Hello world", 'How are you')


# We can override sep with '-':
print("A", "B", sep="-")


# We can override sep with '_' and the line end with three newlines:
print("A", "B", sep="_", end="\n\n\n")


# double or single quotes to mark strings (= sequences of characters)
print('last "line"')


# escaping double quotes with a backslash, when used in
# a double-quote marked string
print("Hello \"sunshine\"")

