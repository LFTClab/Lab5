from ProductionRule import ProductionRule


class Checker:
    def __init__(self, table, input):
        self.table = table
        self.input = input
        self.input.append('$')
        self.workingStack = []
        self.workingStack.append("$")
        self.workingStack.append(0)
        self.prodRules = []
        self.prodRules.append("epsilon")

        print(self.workingStack, self.input)

    def parse(self):
        #verify working stack has a production rule
        while True:
            print("john")
            print(self.workingStack, self.input, self.prodRules)
            productionRule = ProductionRule([],[])
            count = 0
            reduce = False
            for item in reversed(self.workingStack):
                #print(item)
                if item in self.table.states.row.keys():
                    #print(item)
                    productionRule.right.insert(0, item)
                    count += 2
                    for i in self.table.graph.grammar.productionrules:
                        production = self.table.graph.grammar.productionrules[i]
                        if productionRule.right == production.right and i != 0:
                            #self.input.pop(0)
                            del self.workingStack[(len(self.workingStack)-count):(len(self.workingStack))]
                            cifra = self.workingStack[-1]
                            toAdd = self.table.table[cifra].row['S']
                            if toAdd != 'acc':
                                print("toAdd", toAdd)
                                self.workingStack.append('S')
                                self.workingStack.append(int(toAdd[1:]))
                                self.prodRules.insert(0, i)
                                reduce = True
                            else:
                                return "acc"

            if reduce == False:
                letter = self.table.table[self.workingStack[-1]].row[self.input[0]]
                if letter != '' and letter != 'acc':
                    letter = letter[1:]
                    self.workingStack.append(self.input[0])
                    self.workingStack.append(int(letter))
                    self.input.pop(0)
                    reduce = True
                elif letter != 'acc':
                    return 'error'

            if reduce == False:
                print("yallla")
                letter = self.table.table[self.workingStack[-1]].row[self.input[0]]
                if letter == 'acc':
                    return 'acc'