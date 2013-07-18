#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import sys, codecs, re
sys.stdout = codecs.getwriter('utf-8')(sys.stdout.detach())


mytext = "kæt"

# match = re.search("(?P<root>[cf]all|visit)(?P<suffix>ed|ing|s)?", mytext)
match = re.search("(?P<onset>[kg])(?P<nucleus>[Əæɑɜɪ])(?P<coda>[t])?", mytext)
if match:
    print(match.groups())
    print("Onset:", match.group("onset"))
    print("Nucleus:", match.group("nucleus"))
    print("Coda:", match.group("coda"))

