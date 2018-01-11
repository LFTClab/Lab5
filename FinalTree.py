class FinalTree:
    def __init__(self, grammar, checker):
        self.productionRules = grammar.productionrules
        self.order = checker.prodRules
        self.finalTree = [grammar.nonterminals[1]]
        self.computeFinalTree()

    def computeFinalTree(self):
        newList = []
        workingList = []
        index = 0
        #print(self.finalTree)
        while index < len(self.order):
            #print("---", self.order[index])
            #print("---", self.productionRules[self.order[index]])
            if self.finalTree[-1] == 'S':
                self.finalTree.append(self.productionRules[self.order[index]].right)
                index+=1
            else:
                newList = self.finalTree[-1]
                newList = list(reversed(newList))
                #print("++",newList)
                for i in newList:
                    if i != 'S':
                        workingList.append(i)
                    else:
                        for j in list(reversed(self.productionRules[self.order[index]].right)):
                            workingList.append(j)
                        index+=1
                self.finalTree.append(list(reversed(workingList)))
                workingList=[]


        print("Parsing tree:", self.finalTree)
