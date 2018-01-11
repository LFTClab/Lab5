# coding=utf-8
class FirstAndFollow:
    def __init__(self,grammar):
        self.grammar = grammar
        self.first = {}
        self.follow = {}
        self.findFirst()
        self.findFollow()

    def initFirst(self):

        """
           Initialize the dictionary self.first; for each nonterminal we associate an empty list
        """

        for nonterm in self.grammar.nonterminals:
            self.first[nonterm] = []


    def initFollow(self):
        for nonterm in self.grammar.nonterminals:
            self.follow[nonterm] = []

        self.follow[self.grammar.productionrules[0].left].append('$')


    def findFirst(self):
        """
            We have to compute the first for each nonterminals in our grammar.
            So, for each nonterminal that we appear in the left side o a production rule, we have to check the right side of that production rule.
            -If in the right side, the first term is a terminal, then we simply add it to the first list, and go to the next production rule.
            -If in the right side, the first term is a nonterminal, then we append all the elems in its first to the current first list
            -If in the right side, the first term is a nonterminal and its first list contains ε, then we need to go to the next term and check again if it's terminal or nonterminal and so on
        """
        # TODO: de tratat cazul in care exista ε intr-o regula de productie ( a 3-a liniuta)

        self.initFirst()
        for nonterm in list(reversed(self.grammar.nonterminals)):
            for i in range(0,len(self.grammar.productionrules)):
                if nonterm == self.grammar.productionrules[i].left:
                    #print(nonterm+"....."+str(self.grammar.productionrules[i]))
                    if self.grammar.productionrules[i].right[0] in self.grammar.terminals:
                        if self.grammar.productionrules[i].right[0] not in self.first[nonterm]:
                            self.first[nonterm].append(self.grammar.productionrules[i].right[0])

        first = False
        for nonterm in list(reversed(self.grammar.nonterminals)):
            first = False
            #if nonterm == 'expr':
                #print("???")
            for i in range(0,len(self.grammar.productionrules)):
                if nonterm == self.grammar.productionrules[i].left:
                    for j in self.grammar.productionrules[i].right:
                        if j in self.grammar.nonterminals and self.grammar.productionrules[i].right[0] not in self.grammar.terminals and first == False:
                            for elem in self.first[j]:
                                if elem not in self.first[nonterm]:
                                    self.first[nonterm].append(elem)
                                    first = True


        #print("First:",self.first)


    def findFollow(self):
        """
            We have to compute the follow for each nonterminal in our grammar
            We look for the nonterminals in the right sides of the production rules:
                -if we have a terminal in the right side of our nonterminal, then we add it to the follow list
                -if we have a nonterminal in the right side of our nonterminal, then we add the first of the nonterminal to the follow list
        """
        #TODO: de tratat cazul in care exista ε in lista de follow a unui nonterminal

        self.initFollow()
        for nonterm in list(reversed(self.grammar.nonterminals)):
            for i in range(0,len(self.grammar.productionrules)):
                index = self.getIndex(self.grammar.productionrules[i].right,nonterm)
                if index != -1:
                    if index < len(self.grammar.productionrules[i].right)-1:
                        if self.grammar.productionrules[i].right[index+1] in self.grammar.terminals:
                            self.follow[nonterm].append(self.grammar.productionrules[i].right[index+1])

        for nonterm in list(reversed(self.grammar.nonterminals)):
            for i in range(0, len(self.grammar.productionrules)):
                index = self.getIndex(self.grammar.productionrules[i].right, nonterm)
                if index != -1:
                    if index == len(self.grammar.productionrules[i].right)-1:
                        if self.grammar.productionrules[i].right[index] != self.grammar.productionrules[i].left:
                           for elem in self.follow[self.grammar.productionrules[i].left]:
                               self.follow[nonterm].append(elem)

        #print("Follow:",self.follow)

    def getIndex(self,myList,elem):
        for i in range(0,len(myList)):
            if elem == myList[i]:
                return i
        return -1

