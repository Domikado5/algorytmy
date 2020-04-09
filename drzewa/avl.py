class Leaf:
    def __init__(self, value):
        self.parrent = None
        self.value = value
        self.left = None
        self.right = None
        self.height = 1

class Tree:
    def __init__(self):
        self.root = None

    def insert(self, leaf, parrent=self.root):
        if parrent is None:
            parrent = leaf
            if leaf.parrent.left is None or leaf.parrent.right is None: # increase height of tree branches (parrents) 
                self.increaseHeight(leaf.parrent)
        elif parrent.value > leaf.value:
            leaf.parrent = parrent
            self.insert(leaf,parrent.left)
        else:
            leaf.parrent = parrent
            self.insert(leaf,parrent.right)
        # checking if tree is balanced after insertion
        balanceFactor = self.getBalanceFactor(parrent)

        if balanceFactor > 1: #left branch is higher than right branch
            if leaf.value < parrent.leaf.value: # LL rotation
                pass
            elif leaf.value > parrent.leaf.value: # LR rotation
                pass
        elif balanceFactor < -1 and leaf.value > parrent.right.value: #right branch is higher than left branch RR rotation
            if leaf.value > parrent.right.value: # RR rotation
                pass
            elif leaf.value < parrent.right.value: # RL rotation
                pass
    
    def increaseHeight(self, parrent, i=1):
        i += 1
        if parrent.height < i: # checking current height
            parrent.height = i
        if parrent.parrent is not None:
            self.increaseHeight(parrent.parrent, i)

    def leftRotate():
        pass

    def rightRotate():
        pass

    def getBalanceFactor(self, parrent):
        return parrent.left.height - parrent.right.height

myTree = Tree()

    