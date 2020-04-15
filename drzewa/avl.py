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
        # checking if tree is balanced after insert
        self.balance(leaf.value, parrent)
    
    def balance(self, value, parrent):
        balanceFactor = self.getBalanceFactor(parrent)

        if balanceFactor > 1: #left branch is higher than right branch
            if value < parrent.left.value: # LL rotation
                return self.rotateRight(parrent)
            elif value >= parrent.left.value: # LR rotation
                parrent.left = self.rotateLeft(parrent.left)
                return self.rotateRight(parrent)
        elif balanceFactor < -1: #right branch is higher than left branch
            if value >= parrent.right.value: # RR rotation
                return self.rotateLeft(parrent)
            elif value < parrent.right.value: # RL rotation
                parrent.right = self.rotateRight(parrent.right)
                return self.rotateLeft(parrent)

    def delete(self, value, parrent):
        if parrent is None: # no value found
            return parrent
        elif value < parrent.value: # searching value on the left branch
            parrent.left = self.delete(value, parrent.left)
            if parrent == self.root:
                self.root.left = parrent.left
        elif value > parrent.value: # searching value on the right branch
            parrent.right = self.delete(value, parrent.right)
            if parrent == self.root:
                self.root.right = parrent.right
        else: # found value
            if parrent.left is None: # no left branch
                tmp = parrent.right 
                if parrent.right is not None:
                    tmp.parrent = parrent.parrent
                parrent = None
                return tmp
            elif parrent.right is None: # no right branch
                tmp = parrent.left
                if parrent.left is not None:
                    tmp.parrent = parrent.parrent
                parrent = None
                return tmp
            tmp = self.minValue(parrent.right)
            parrent.value = tmp.value
            parrent.right = self.delete(tmp.value, parrent.right)
        # update height
        parrent.height = self.updateHeight(parrent)
        if parrent == self.root:
            self.root.height = parrent.height
        
        # check balance
        balance = self.getBalanceFactor(parrent)
        if balance > 1:
            if self.getBalanceFactor(parrent.left) >= 0:
                return self.rotateRight(parrent)
            elif self.getBalanceFactor(parrent.left) < 0:
                parrent.left = self.rotateLeft(parrent.left)
                return self.rotateRight(parrent)
        if balance < -1:
            if self.getBalanceFactor(parrent.right) <= 0:
                return self.rotateLeft(parrent)
            elif self.getBalanceFactor(parrent.right) > 0:
                parrent.right = self.rotateRight(parrent.right)
                return self.rotateLeft(parrent)
        return parrent
            
            
    def rootUpdate(self, leaf, parrent):
        if parrent == self.root:
            self.root = leaf
        elif parrent == self.root.left:
            self.root.left = leaf
        elif parrent == self.root.right:
            self.root.right = leaf

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

    def max(self, parrent, route=[]):
        if parrent.right is None:
            route.append(parrent.value)
            print("Sciezka: ")
            print(*route, sep = " -> ")
            print("Max: ")
            print(parrent.value)
        else:
            route.append(parrent.value)
            self.max(parrent.right)
    
    def minValue(self, parrent):
        if parrent is None or parrent.left is None:
            return parrent
        return self.minValue(parrent.left)

    def min(self, parrent, route=[]):
        if parrent.left is None:
            route.append(parrent.value)
            print("Sciezka:")
            print(*route, sep = " -> ")
            print("Min: ")
            print(parrent.value)
        else:
            route.append(parrent.value)
            self.min(parrent.left)

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
print("Korzeń: ")
print(myTree.root.value)
myTree.printTree(myTree.root)
print("Wysokosc drzewa:")
print(myTree.root.height)
myTree.max(myTree.root)
myTree.min(myTree.root)
myTree.delete(20, myTree.root)
print("Korzeń:")
print(myTree.root.value)
myTree.printTree(myTree.root)
print("Wysokosc drzewa:")
print(myTree.root.height)