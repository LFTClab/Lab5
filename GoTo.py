import copy

from FirstAndFollow import FirstAndFollow
from ProductionRule import ProductionRule


class GoTo:
    def __init__(self,prediction,itNo,grammar):
        self.firstAndFollow = FirstAndFollow(grammar)
        self.grammar = grammar
        self.productionRules = []
        self.predictions = [prediction]
        self.id = itNo
        #self.initialiseProductionRules(prodRule,grammar)

    def getProdRules(self,prdRule):
        newPrdRule = copy.deepcopy(prdRule)
        index = self.findPoint(newPrdRule.right)
        if  index != -1:
            newPrdRule.right[index], newPrdRule.right[index+1] = newPrdRule.right[index+1], newPrdRule.right[index]

        self.productionRules.append(newPrdRule)


        if index+2 < len(newPrdRule.right) :
            if newPrdRule.right[index+2] in self.grammar.nonterminals:
                for i in range (1,len(self.grammar.productionrules)):
                    if self.grammar.productionrules[i].left == newPrdRule.right[index+2]:
                        if (newPrdRule.right[index+2] == newPrdRule.right[-1]):
                            self.predictions.append(self.predictions[-1])
                        else:
                            if(newPrdRule.right[index+3] in self.grammar.nonterminals):
                                self.predictions.append(self.firstAndFollow.first[newPrdRule.right[index+3]][0])
                            else:
                                self.predictions.append(newPrdRule.right[index+3])
                        self.initialiseProductionRules(self.grammar.productionrules[i])


    def setProdRules(self,prodRules):
        self.productionRules = prodRules

    def setPredictions(self, predictions):
        self.predictions = predictions


    def findPoint(self, mylist):
        for i in range(0, len(mylist) - 1):
            if mylist[i] == '.':
                return i
        return -1



    def initialiseProductionRules(self,prodRule):
        newList = []
        newList.append(".")
        for elem in prodRule.right:
            newList.append(elem)

        p = ProductionRule(prodRule.left,newList)
        #print("!!!!!!!",self.productionRules)
        if self.findProd(p) == -1 :
            self.productionRules.append(p)
        else:
            self.predictions[self.findProd(p)] += prodRule.right[1]




        if prodRule.right[0] in self.grammar.nonterminals:
            for i in range (1,len(self.grammar.productionrules)):
                if self.grammar.productionrules[i].left == prodRule.right[0]:
                    if (prodRule.right[0] == prodRule.right[-1]):
                        self.predictions.append(self.predictions[-1])
                    else:
                        if(prodRule.right[1] in self.grammar.nonterminals):
                            self.predictions.append(self.firstAndFollow.first[prodRule.right[1]][0])
                        else:
                            self.predictions.append(prodRule.right[1])
                    self.initialiseProductionRules(self.grammar.productionrules[i])


    def __repr__(self):
        string = "\n-------------------\n"
        string += "iteration" + str(self.id) + "\n"
        for i in range(0, len(self.productionRules)):
            string += "[" + str(self.productionRules[i]) + ", " + str(self.predictions[i]) + "]" +"\n"
        string += "------------------"
        return string


    def checkProd(self,prdRule):
        for elem in prdRule:
            if elem not in self.productionRules:
                return False
        return True


    def findProd(self,rule):
        for i in range(0,len(self.productionRules)):
            if self.productionRules[i] == rule:
                return i
        return -1


    def __eq__(self, other):
        if self.checkProd(other.productionRules)==True and other.predictions == self.predictions:
            return True
        return False




class GoToGraph:
    def __init__(self,grammar):
        self.grammar = grammar
        gt = GoTo('$', 0, self.grammar)
        gt.initialiseProductionRules(self.grammar.productionrules[0])
        #print(gt)
        self.iterationList = [gt]
        self.nextIterations = {}
        self.derivatedFrom = {}
        self.duplicate = {}
        self.count = 1
        self.iter = 1
        self.findNext(0)
        self.cycles = {}
        self.graph()


    def graph(self):
        #print(self.iter,"-------",len(self.iterationList))
        while self.iter < self.count:
            #print("#########")
            #print(self.iterationList)
            #print("#########")
            #print(self.iter, "-------",len(self.iterationList))
            self.getGraph(self.iter)
            #if self.iter == 12:
                #print("next iter:",self.nextIterations)
                #break
            self.iter += 1



    def findNext(self,i):
        newList = []
        if i < len(self.iterationList):
            for elem in self.iterationList[i].productionRules:
                index = self.findPoint(elem.right)
                if index != -1:
                    if elem.right[index+1] not in newList:
                        newList.append(elem.right[index+1])
        if newList != []:
            for elem in newList:
                self.nextIterations[self.count] = elem
                self.derivatedFrom[self.count] = [self.iterationList[i].id]
                self.count += 1

        #print(self.nextIterations)


    def findPoint(self,mylist):
        for i in range(0,len(mylist)-1):
            if mylist[i] == '.':
                return i
        return -1


    def getGraph(self,key):
        #print(self.nextIterations)
        #print(self.derivatedFrom)
        #print(self.duplicate)
        newprodRules = []
        newPredictions = []
        #print("iterno:",key)
        #print("derivatedFrom:",self.derivatedFrom[key])
        prevIter = self.derivatedFrom[key][0]
        #print("#########", prevIter)
        if(prevIter in self.nextIterations.keys() or prevIter == 0):

            prevProdRule = self.getProdRuleByLiteral(self.nextIterations[key],prevIter)
            #print("Prev:",prevProdRule)
            for elem in prevProdRule:
                gt = GoTo(prevProdRule[elem],key,self.grammar)
                gt.getProdRules(elem)
                #print( "++++++++++", gt.productionRules)
                for i in range(0,len(gt.productionRules)):
                    index = self.findRule(newprodRules,gt.productionRules[i])
                    if  index== -1:
                        newprodRules = newprodRules + [gt.productionRules[i]]
                        newPredictions = newPredictions + [gt.predictions[i]]
                    else:
                        if gt.predictions[index] not in newPredictions[index]:
                            newPredictions[index] += "|" + gt.predictions[index]

            #print("!!!!!!!",newprodRules)
            #print("########",newPredictions)
            gt.setProdRules(newprodRules)
            gt.setPredictions(newPredictions)
            if(self.iterationExists(gt) == -1):
                #print(gt)
                #print("oooooooookkkkkkkkk")
                self.iterationList.append(gt)
                #if(len(self.iterationList) == 14) :
                    #print("$$$$$$$$$$$$$")
                self.findNext(len(self.iterationList)-1)

            else:
                #self.iterationList.append(gt)
                #print("keyyyyyyyyyyy",key)
                #print("duplicate", gt)
                self.cycles[key] = self.nextIterations[key]
                del(self.nextIterations[key])
                del(self.derivatedFrom[key])
                if self.iterationExists(gt) not in self.duplicate:
                    self.duplicate[gt.id] = self.iterationExists(gt)
                    #self.derivatedFrom[self.iterationExists(gt)].append(gt.id)
                else:
                    self.duplicate[gt.id] = self.duplicate[self.iterationExists((gt))]
                    #self.derivatedFrom[self.iterationExists(gt)].append(gt.id)
                if self.iterationExists(gt) in self.derivatedFrom :
                    self.derivatedFrom[self.iterationExists(gt)].append(prevIter)
                else:
                    if (self.iterationExists(gt) in self.duplicate):
                        self.derivatedFrom[self.duplicate[self.iterationExists(gt)]].append(prevIter)

                #self.iter +=1
                #self.nextIterations[]
                #self.findNext(key)
                #self.getGraph(key+1)


    def getIterationByID(self,id):
        for i in range(0,len(self.iterationList)):
            if self.iterationList[i].id == id[0]:
                return i
        return -1

    def getProdRuleByLiteral(self,literal,iterationNo):
        iteration = {}
        for index in range(0,len(self.iterationList)):
            if self.iterationList[index].id == iterationNo:
                for j in range(0,len(self.iterationList[index].productionRules)):
                    for i in range (0,len(self.iterationList[index].productionRules[j].right)-1):
                        if self.iterationList[index].productionRules[j].right[i] == '.' and self.iterationList[index].productionRules[j].right[i+1]== literal:
                            iteration[self.iterationList[index].productionRules[j]] = self.iterationList[index].predictions[j]
        return iteration

    def iterationExists(self,gt):
        for i in range (0,len(self.iterationList)):
            if self.iterationList[i] == gt:
                #print("$$$$$$$$$$", i)
                return i
        return -1

    def findRule(self,list,rule):
        for i in range(0, len(list)):
            if list[i] == rule and  len(list[i].right) == len(rule.right):
                return i
        return -1