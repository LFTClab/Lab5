import copy


class Table:
    def __init__(self, states, graph):
        self.states = states
        self.graph = graph
        self.table = {}
        self.initTable()

    def initTable(self):
        for i in self.graph.iterationList:
            self.table[i.id] = copy.deepcopy(self.states)

        for index in self.table.keys():
            look_for = index
            shift = False
            for i in self.graph.derivatedFrom.keys():
                if look_for in self.graph.derivatedFrom[i]:
                    column = self.graph.nextIterations[i]
                    self.table[look_for].row[column] = 'S' + str(i)
                    shift = True
            if shift == False or shift == True:
                for i in self.graph.iterationList:
                    if i.id == look_for:
                        right = i.productionRules[0].right
                        right = right[:-1]
                        for index in self.graph.grammar.productionrules:
                            production = self.graph.grammar.productionrules[index]
                            if production.right == right and index !=0:
                                for j in i.predictions:
                                    for prediction in j:
                                        if prediction != '|':
                                            self.table[look_for].row[prediction] = 'r' + str(index)
                                            shift = True
            if shift == False:
                self.table[look_for].row[self.states.dolar] = 'acc'

        print("TABLE")
        for i in self.table:
            print(i , self.table[i])

