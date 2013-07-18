#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import sys, codecs, re
sys.stdout = codecs.getwriter('utf-8')(sys.stdout.detach())

class Grammar:
   lhs = {}
   rhs = {}

   def addRule(self, newlhs, newrhs):
      value = self.lhs.get(newlhs, [])
      if newrhs not in value:
         value.append(newrhs)
      self.lhs[newlhs] = value
      value = self.rhs.get(newrhs, [])
      if newlhs not in value:
         value.append(newlhs)
      self.rhs[newrhs] = value

   def loadGrammarFromFile(self, filename):
      grammar = ""
      try:
         inputfile = open(filename, mode='r', encoding='utf-8')
         grammar = inputfile.read()
         inputfile.close()
      except IOError:
         pass

      rules = re.findall("\s*(?P<rule>\w+[ \t]*->[ \t]*\w+([ \t]+\w+)*)[ \t]*(#[^\n]*)?\n", grammar)
      for x in rules:
         lhs, rhs = re.split("\s*->\s*", x[0])
         rhs = tuple(rhs.split())
         self.addRule(lhs, rhs)

   def getRHS(self, newlhs):
      "Returns the list of RHS for a given LHS-symbol."
      return self.lhs.get(newlhs, [])

   def getLHS(self, newrhs):
      return self.rhs.get(newrhs, [])

   def prettyPrint(self):
      for key in self.lhs:
         for rhs in self.lhs[key]:
            print(key, "->", " ".join(rhs))
      
   

mygrammar = Grammar()
mygrammar.loadGrammarFromFile("grammar1.txt")
#mygrammar.addRule("S", ("NP", "VP") )
#mygrammar..lhs["S"] = [ ('NP', 'VP') ]
#mygrammar.rhs[ ('NP', 'VP') ] = [ "S" ]

#print( mygrammar.getRHS("S") )
#print(mygrammar.getLHS( ('N',) ) )
mygrammar.prettyPrint()
