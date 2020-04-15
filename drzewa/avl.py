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

    def insert(self, leaf, parrent):
        if parrent is None:
            if leaf.parrent is None:
                self.root = leaf
            else:
                self.increaseHeight(leaf.parrent)
            return leaf
        elif parrent.value > leaf.value:
            leaf.parrent = parrent
            if parrent.left is None:
                parrent.left = self.insert(leaf,parrent.left)
            else:
                self.insert(leaf,parrent.left)
        else:
            leaf.parrent = parrent
            if parrent.right is None:
                parrent.right = self.insert(leaf,parrent.right)
            else:
                self.insert(leaf,parrent.right)
        # checking if tree is balanced after insertion
        balanceFactor = self.getBalanceFactor(parrent)

        if balanceFactor > 1: #left branch is higher than right branch
            if leaf.value < parrent.left.value: # LL rotation
                return self.rotateRight(parrent)
            elif leaf.value >= parrent.left.value: # LR rotation
                parrent.left = self.rotateLeft(parrent.left)
                return self.rotateRight(parrent)
        elif balanceFactor < -1: #right branch is higher than left branch
            if leaf.value >= parrent.right.value: # RR rotation
                return self.rotateLeft(parrent)
            elif leaf.value < parrent.right.value: # RL rotation
                parrent.right = self.rotateRight(parrent.right)
                return self.rotateLeft(parrent)
    
    def increaseHeight(self, parrent, i=1):
        i += 1
        if parrent is None:
            return None
        if parrent.height < i: # checking current height
            parrent.height = i
        if parrent.parrent is not None:
            self.increaseHeight(parrent.parrent, i)

    def rotateLeft(self, parrent):
        y = parrent.right
        z = y.left
        y.left = parrent
        y.parrent = parrent.parrent
        parrent.parrent = y
        parrent.right = z
        if z is not None:
            z.parrent = parrent

        parrent.height = self.updateHeight(parrent)
        y.height = self.updateHeight(y)
        if y.parrent is None: # Updating root
            self.root = y
        elif self.isRoot(y.parrent): # Updating root childs
            if y.parrent.left == parrent:
                self.root.left = y
            elif y.parrent.right == parrent:
                self.root.right = y
            self.root.height = self.updateHeight(self.root)
        return y
    
    def rotateRight(self, parrent):
        y = parrent.left
        z = y.right

        y.right = parrent
        y.parrent = parrent.parrent
        parrent.parrent = y
        parrent.left = z
        if z is not None:
            z.parrent = parrent

        parrent.height = self.updateHeight(parrent)
        y.height = self.updateHeight(y)
        if y.parrent is None: # Updating root
            self.root = y
        elif self.isRoot(y.parrent): # Updating root childs
            if y.parrent.left == parrent:
                self.root.left = y
            elif y.parrent.right == parrent:
                self.root.right = y
            self.root.height = self.updateHeight(self.root)
        return y

    def updateHeight(self, parrent):
        a = 0 if parrent.left is None else parrent.left.height
        b = 0 if parrent.right is None else parrent.right.height
        return 1+max(a,b)

    def getBalanceFactor(self, parrent):
        if parrent.left is None:
            left = 0
        else:
            left = parrent.left.height
        if parrent.right is None:
            right = 0
        else:
            right = parrent.right.height
        return left - right

    def printTree(self, root):
        if root is None:
            return
        print("{} ".format(root.value), end="")
        self.printTree(root.left)
        self.printTree(root.right)

    def max(self, root, route=[]):
        if root.right is None:
            route.append(root.value)
            print("Sciezka: ")
            print(*route, sep = " -> ")
            print("Max: ")
            print(root.value)
        else:
            route.append(root.value)
            self.max(root.right)
    
    def min(self, root, route=[]):
        if root.left is None:
            route.append(root.value)
            print("Sciezka:")
            print(*route, sep = " -> ")
            print("Min: ")
            print(root.value)
        else:
            route.append(root.value)
            self.min(root.left)

    def isRoot(self, parrent):
        if parrent.parrent is None:
            return True
        else:
            return False

myTree = Tree()
myTree.insert(Leaf(10), myTree.root)
myTree.insert(Leaf(20), myTree.root)
myTree.insert(Leaf(30), myTree.root)
myTree.insert(Leaf(40), myTree.root)
myTree.insert(Leaf(50), myTree.root)
myTree.insert(Leaf(25), myTree.root)
print(myTree.root.value)
myTree.printTree(myTree.root)
print("Wysokosc drzewa:")
print(myTree.root.height)
myTree.max(myTree.root)
myTree.min(myTree.root)
