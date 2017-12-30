from GoTo import GoTo, GoToGraph
from ProductionRule import ProductionRule


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






if __name__ == '__main__':
    g = Grammar("input.txt")
    graph = GoToGraph(g)
    print("+++++++++++++++++++++++++++")
    print(graph.nextIterations)
    print(graph.derivatedFrom)
    print(graph.duplicate)
    print(graph.cycles)
    print(graph.iterationList)


