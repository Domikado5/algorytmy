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
            if leaf.value < parrent.leaf.value: # LL rotation
                pass
            elif leaf.value > parrent.leaf.value: # LR rotation
                pass
        elif balanceFactor < -1 and leaf.value > parrent.right.value: #right branch is higher than left branch
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

myTree = Tree()
myTree.root = Leaf(10) # define root of tree
myTree.insert(Leaf(11), myTree.root)
myTree.insert(Leaf(11), myTree.root)
myTree.insert(Leaf(11), myTree.root)
myTree.insert(Leaf(9), myTree.root)
myTree.printTree(myTree.root)
print("Wysokosc drzewa:")
print(myTree.root.height)
myTree.max(myTree.root)
myTree.min(myTree.root)
