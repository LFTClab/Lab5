class FinalTree:
    def __init__(self, grammar, checker):
        self.terminals = grammar.terminals
        self.productionRules = grammar.productionrules
        self.order = checker.prodRules
        self.finalTree = []
        self.computeFinalTree()

    def computeFinalTree(self):
        newList = []
        #workingList = []
        self.finalTree.append(self.productionRules[0].right)
        index = 0
        # print(self.finalTree)
        while index < len(self.order):
            # print("---", self.order[index])
            # print("---", self.productionRules[self.order[index]])

            if index == 0:
                self.finalTree.append(self.productionRules[int(self.order[index])].right)
                index += 1
            else:
                newList = self.finalTree[-1]
                newList = list(reversed(newList))
                #print("++",newList)
                workingList = []
                first = False
                for i in newList:
                    if i in self.terminals:
                        workingList.append(i)
                    elif first == False :
                        for j in list(reversed(self.productionRules[int(self.order[index])].right)):
                            workingList.append(j)
                        index += 1
                        first = True
                    elif first == True:
                        workingList.append(i)
                self.finalTree.append(list(reversed(workingList)))

        print("Parsing tree:")
        for i in self.finalTree:
            print(i)

