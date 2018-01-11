import copy

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

        print(self.workingStack, self.input)

    def parse(self):
        # verify working stack has a production rule
        while True:
            print(self.workingStack, self.input, self.prodRules)
            productionRule = ProductionRule([], [])
            count = 0
            reduce = False
            listP = []
            for item in reversed(self.workingStack):
                # print(item)
                if item in self.table.states.row.keys():
                    # print(item)
                    productionRule.right.insert(0, item)
                    count += 2
                    for i in self.table.graph.grammar.productionrules:
                        production = self.table.graph.grammar.productionrules[i]
                        if productionRule.right == production.right and i != 0:
                            # print("prod.rule", productionRule.right)
                            pr = copy.deepcopy(productionRule.right)
                            lr = copy.deepcopy(production.left)
                            listP.append((pr,lr))
                            # print("if",listP)

                            # self.input.pop(0)
            print("litp", listP)
            prod = self.getMaxList(listP)
            left = ""
            id = 0

            print("pp",prod)
            for i in self.table.graph.grammar.productionrules:
                production = self.table.graph.grammar.productionrules[i]
                if prod == production.right and i != 0:
                    left = production.left
                    id = i

            howMany = 0
            for i in listP:
                if len(i) == len(prod):
                    prod = i
                    howMany +=1

            for i in listP:
                if len(i) == len(prod):
                    prod = i

                    if prod != []:
                        count = len(prod[0]) * 2
                        if (self.table.table[self.workingStack[-1]].row[self.input[0]] == ''):
                            cifra = self.workingStack[-count - 1]
                            left = prod[1]
                            toAdd = self.table.table[cifra].row[left]
                            for i in self.table.graph.grammar.productionrules:
                                production = self.table.graph.grammar.productionrules[i]
                                if production.right == prod[0]:
                                    rule = i
                            if toAdd == '' and howMany == 0:
                                return "error"
                            if toAdd == '' :
                               print("Dsadada")
                            elif toAdd != 'acc':
                                del self.workingStack[(len(self.workingStack) - count):(len(self.workingStack))]
                                self.workingStack.append(left)
                                self.workingStack.append(int(toAdd[1:]))
                                self.prodRules.insert(0, rule)
                                reduce = True
                            else:
                                self.prodRules.insert(0, rule)
                                print(self.workingStack, self.input, self.prodRules)
                                return "acc2"


                        elif (self.table.table[self.workingStack[-1]].row[self.input[0]][0] == 'r'):
                            cifra = self.workingStack[-count-1]
                            left = prod[1]
                            print("led", left)
                            toAdd = self.table.table[cifra].row[left]
                            print("here", toAdd)
                            rule = self.table.table[self.workingStack[-1]].row[self.input[0]][1:]
                            if toAdd == '' and howMany == 0:
                                return "error"
                            if toAdd == '' :
                               print("Dsadada")
                            elif toAdd != 'acc':
                                del self.workingStack[(len(self.workingStack) - count):(len(self.workingStack))]
                                self.workingStack.append(left)
                                self.workingStack.append(int(toAdd[1:]))
                                self.prodRules.insert(0, rule)
                                reduce = True
                            else:
                                self.prodRules.insert(0, rule)
                                print(self.workingStack, self.input, self.prodRules)
                                return "acc2"
                howMany -= 1


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
                letter = self.table.table[self.workingStack[-1]].row[self.input[0]]
                if letter == 'acc':
                    return 'acc'

    def getMaxList(self, l):
        max = -1
        toReturn = []
        for i in l:
            if max < len(i[0]):
                max = len(i[0])
                toReturn = i
        return toReturn
