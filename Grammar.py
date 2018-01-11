from FinalTree import FinalTree
from GoTo import GoTo, GoToGraph
from ProductionRule import ProductionRule
from States import States
from Checker import *
from Table import *

class Grammar:
    def __init__(self,filename):
        self.terminals = []
        self.nonterminals = []
        self.productionrules = {}
        self.readGrammar(filename)

    def readGrammar(self,filename):
        f = open(filename,"r")
        count = 0
        for elem in f.readline().strip().split(' '):
            self.nonterminals.append(elem)
        for elem in f.readline().strip().split(' '):
            self.terminals.append(elem)
        for line in f:
            elems = line.strip().split('->')
            rightpart = elems[1].split(' ')
            self.productionrules[count]= ProductionRule(elems[0],rightpart)
            count+=1

        print("Terminals:",self.terminals)
        print("NonTerminals:",self.nonterminals)
        print("ProductionRules:",self.productionrules)

def printGotoGraph(gt):
    print("\n")
    print("-----gotoGraph-----")
    print("iteration", gt.id)
    for i in range(0, len(gt.productionRules)):
        print("[" + str(gt.productionRules[i]) + ", " + gt.predictions[i] + "]")

def readSequence(fileName):
    f = open(fileName, "r")
    l = []
    for elem in f.readline().strip():
        l.append(elem)
    return l

if __name__ == '__main__':
    g = Grammar("input.txt")
    graph = GoToGraph(g)
    print("+++++++++++++++++++++++++++")
    #print(graph.nextIterations)
    #print(graph.derivatedFrom)
    print(graph.iterationList)
    states = States(g.nonterminals, g.terminals)
    table = Table(states, graph)
    #   transition(3 lists - working stack($0), sequence, production rules)
    #   check if working stack has a valid production rule and replace with S followed by ...
    inputSequence = readSequence("sequence.in")
    checker = Checker(table, inputSequence)
    print("+++++++++++++++++++++++++++")
    result = checker.parse()
    if result == 'error':
        #sorry :(
        print(result)
    else:
        print("ACC", result)
        ft = FinalTree(g,checker)

