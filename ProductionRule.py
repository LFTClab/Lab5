class ProductionRule:
    def __init__(self,left,right):
        self.left = left
        self.right = right

    def getLeft(self):
        return self.left

    def getRight(self):
        return self.right

    def __repr__(self):
        str = ""
        str += self.left + " -> "
        for elem in self.right:
            str += elem + " "
        return str

    def __str__(self):
        str = ""
        str += self.left + " -> "
        for elem in self.right:
            str += elem + " "
        return str

    def __eq__(self, other):
        if other.left == other.left and self.listsEq(other.right)==True:
            return True
        return False


    def listsEq(self,other):
        newList = []
        for i in range(0, len(other)):
            for j in range (0, len(self.right)):
                if i==j:
                    if other[i] == self.right[j]:
                        newList.append(i)

        if len(newList) == len(self.right):
            return True
        else:
            return False

    def __hash__(self):
        string = ""
        for elem in self.right:
            string += elem
        return hash(self.left + string)

