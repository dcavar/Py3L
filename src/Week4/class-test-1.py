#!/usr/bin/env python3

import re

class Grammar:
    lhs = {}
    rhs = {}

    def __init__(self, filename=None):
        "this is a comment"
        if filename:
            self.readFile(filename)

    def getRHS(self, lhs):
        "Returns the list of RHS for a given LHS."
        return self.lhs.get(lhs, [])

    def getLHS(self, rhs):
        return self.rhs.get(rhs, [])

    def addRule(self, newlhs, newrhs):
        value = self.lhs.get(newlhs, [])
        value.append(newrhs)
        self.lhs[newlhs] = value
        value = self.rhs.get(newrhs, [])
        value.append(newlhs)
        self.rhs[newrhs] = value

    def readFile(self, filename):
        try:
            inpfile = open(filename, encoding="utf-8", mode='r')
            for line in inpfile.readlines():
                match = re.search("(?P<lhs>\w+)\s*->\s*(?P<rhs>\w+(\s+\w+)*)(#.*)?", line)
                if match:
                    lhs = match.group("lhs")
                    rhs = match.group("rhs")
                    self.addRule(lhs, tuple(rhs.split()))
            inpfile.close()
        except Exception:
            pass

    def printGrammar(self):
        for x in self.lhs:
            for y in self.lhs[x]:
                print(x, "->", " ".join(y))


class ProbGrammar(Grammar):
    def countProbs(self, rules):
        pass


class Parser:
    
    grammar = Grammar()
    
    def parse(self, sentence):
        # tokens = tuple(sentence.split())
        agenda = [ tuple(sentence.split()) ]
        while agenda:
            tokens = tuple(agenda.pop())
            for x in range(len(tokens)):
                for y in range(1, len(tokens) - x + 1):
                    sequence = tokens[x:x+y]
                    print("sequence:", sequence)
                    replacementlist = self.grammar.getLHS( sequence )
                    print("replacementlist:", replacementlist)
                    if replacementlist:
                        replacement = list(tokens[:])
                        replacement[x:x+y] = [ replacementlist[0] ]
                        print("Adding to agenda:", replacement)
                        agenda.append(replacement)
            print("Agenda", agenda)




myparser = Parser()
myparser.grammar.readFile("grammar1.txt")

# parse "John loves Mary" is "N V N"
myparser.parse("John loves Mary")

#mygrammar = Grammar("grammar1.txt")
#mygrammar.readFile("grammar1.txt")
#mygrammar.printGrammar()

#mygrammar.addRule("S", ("NP", "VP") )

#print(mygrammar.getRHS("S") , mygrammar.getLHS( ("NP", "VP") ))
