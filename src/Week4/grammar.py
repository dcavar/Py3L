#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import sys, codecs, re
sys.stdout = codecs.getwriter('utf-8')(sys.stdout.detach())


def readGrammar(filename):
    try:
        inpfile = open(filename, encoding="utf-8", mode='r')
        for line in inpfile.readlines():
            match = re.search("(?P<lhs>\w+)\s*->\s*(?P<rhs>\w+(\s+\w+)*)(#.*)?", line)
            if match:
                lhs = match.group("lhs")
                rhs = match.group("rhs")
                print(lhs + " -> " + rhs)
        inpfile.close()
    except Exception:
        pass

readGrammar("grammar1.txt")

