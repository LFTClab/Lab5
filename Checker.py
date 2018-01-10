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
        productionRule = ProductionRule([],[])
        count = 0
        reduce = False
        for item in self.workingStack[::-1]:
            #print(item)
            if item in self.table.states.row.keys():
                productionRule.right.insert(0, item)
                count += 1
                for i in self.table.graph.grammar.productionrules:
                    production = self.table.graph.grammar.productionrules[i]
                    if productionRule.__eq__(production):
                        self.input.pop(0)
                        del self.workingStack[(len(self.workingStack)-count):(len(self.workingStack))]
                        self.prodRules.append(i)
                        reduce = True
        if reduce:
            pass
        else:
            letter = self.table.table[self.workingStack[-1]].row[self.input[0]]
            if letter != '':
                letter = letter[1:]
                self.workingStack.append(self.input[0])
                self.workingStack.append(letter)
                self.input.pop(0)
                reduce = True

        if reduce == False:
            letter = self.table.table[self.workingStack[-1]].row[self.input[0]]
            if letter == 'acc':
                return 'acc'

        print(self.workingStack, self.input, self.prodRules)