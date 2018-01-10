class States:
    def __init__(self, nonTerminals, terminals):
        self.nonTerminals = nonTerminals
        self.terminals = terminals
        self.dolar = '$'
        self.row = {}
        self.initrow()

    def initrow(self):
        for i in self.nonTerminals:
            if i != 'S1':
                self.row[i] = ''
        for i in self.terminals:
            self.row[i] = ''
        self.row[self.dolar] = ''

    def __repr__(self):
        s = ''
        for i in self.row.keys():
            s += i
            s += "-'"
            s += self.row[i]
            s += "' "
        return s