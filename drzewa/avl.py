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
        # checking balance after insert
        self.balanceAfterInsert(leaf.value, parrent)
    
    def balanceAfterInsert(self, value, parrent):
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
            if parrent == self.root:
                flag = True
            else:
                flag = False
            if parrent.left is None: # no left branch
                tmp = parrent.right 
                if parrent.right is not None:
                    tmp.parrent = parrent.parrent
                if flag:
                    self.root = tmp
                return tmp
            elif parrent.right is None: # no right branch
                tmp = parrent.left
                if parrent.left is not None:
                    tmp.parrent = parrent.parrent
                if flag:
                    self.root = tmp
                return tmp
            tmp = self.minValue(parrent.right)
            if tmp == parrent:
                tmp = None
            if flag:
                self.root.value = tmp.value
            else:
                parrent.value = tmp.value
            parrent.right = self.delete(tmp.value, parrent.right)
        # update height
        parrent.height = self.updateHeight(parrent)
        if parrent == self.root:
            self.root.height = parrent.height
        
        # check balance
        parrent = self.balanceAfterDelete(parrent)

        return parrent
            
    def balanceAfterDelete(self, parrent):
        balance = self.getBalanceFactor(parrent)

        if balance > 1:
            if self.getBalanceFactor(parrent.left) >= 0: # LL rotation
                return self.rotateRight(parrent)
            elif self.getBalanceFactor(parrent.left) < 0: # LR rotation
                parrent.left = self.rotateLeft(parrent.left)
                return self.rotateRight(parrent)
        if balance < -1:
            if self.getBalanceFactor(parrent.right) <= 0: # RR rotation 
                return self.rotateLeft(parrent)
            elif self.getBalanceFactor(parrent.right) > 0: # RL rotation
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
        else:
            if y.parrent.left == parrent:
                y.parrent.left = y
            elif y.parrent.right == parrent:
                y.parrent.right = y
            y.parrent.height = self.updateHeight(y.parrent)
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
        else:
            if y.parrent.left == parrent:
                y.parrent.left = y
            elif y.parrent.right == parrent:
                y.parrent.right = y
            y.parrent.height = self.updateHeight(y.parrent)
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

    def printTree(self, root): # preorder printing
        if root is None:
            return
        print("{} ".format(root.value), end="")
        self.printTree(root.left)
        self.printTree(root.right)

    def inOrder(self, root): # inorder printing
        if root is None:
            return
        self.printTree(root.left)
        print("{} ".format(root.value), end="")
        self.printTree(root.right)

    def postOrder(self, root): # postorder printing
        if root is None:
            return
        self.printTree(root.left)
        self.printTree(root.right)
        print("{} ".format(root.value), end="")

    def chopDown(self, root): # delete whole tree - postorder
        if root is None:
            return
        root.left = self.chopDown(root.left)
        root.right = self.chopDown(root.right)
        if root == self.root:
            self.root = None
        else:
            self.delete(root.value, root)

    def minValue(self, parrent):
        if parrent is None or parrent.left is None:
            return parrent
        return self.minValue(parrent.left)

    def maxValue(self, parrent):
        if parrent is None or parrent.right is None:
            return parrent
        return self.maxValue(parrent.right)

    def max(self, parrent):
        if parrent.right is None:
            print(parrent.value)
            print("Max: ")
            print(parrent.value)
        else:
            print("{} -> ".format(parrent.value), end="")
            self.max(parrent.right)
    
    def min(self, parrent):
        if parrent.left is None:
            print(parrent.value)
            print("Min: ")
            print(parrent.value)
        else:
            print("{} -> ".format(parrent.value), end="")
            self.min(parrent.left)

    def isRoot(self, parrent):
        if parrent.parrent is None:
            return True
        else:
            return False

myTree = Tree()
myTree.insert(Leaf(10), myTree.root)
myTree.insert(Leaf(2), myTree.root)
myTree.insert(Leaf(1), myTree.root)
myTree.insert(Leaf(5), myTree.root)
myTree.insert(Leaf(3), myTree.root)
myTree.insert(Leaf(7), myTree.root)
myTree.insert(Leaf(11), myTree.root)
myTree.insert(Leaf(15), myTree.root)
print("###AVL###")
print("Root: ")
print(myTree.root.value)
myTree.printTree(myTree.root) # preorder print
print("\n Height:")
print(myTree.root.height)
print("Max value path: ")
myTree.max(myTree.root)
print("Min value path: ")
myTree.min(myTree.root)
myTree.delete(7, myTree.root) # delete 40
myTree.delete(7, myTree.root) # delete 40
print("After 40 delete")
print("Root:")
print(myTree.root.value)
myTree.printTree(myTree.root)
print("\n Height:")
print(myTree.root.height)
print("Preorder:")
myTree.printTree(myTree.root)
print("\nInorder:")
myTree.inOrder(myTree.root)
print("\nPostorder:")
myTree.postOrder(myTree.root)
myTree.chopDown(myTree.root)
print("\nAfter remove")
print("Preorder:")
myTree.printTree(myTree.root)