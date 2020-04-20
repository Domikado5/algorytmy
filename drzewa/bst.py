class Leaf:
    def __init__(self, value):
        self.parrent = None
        self.value = value
        self.left = None
        self.right = None

class Tree:
    def __init__(self):
        self.root = None

    def insert(self, leaf, parrent):
        if parrent is None:
            if leaf.parrent is None:
                self.root = leaf
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

    def insertIter(self, leaf, parrent):
        while True:
            if self.root is None:
                self.root = leaf
                break
            elif self.root.left is None and self.root.value > leaf.value:
                leaf.parrent = self.root
                self.root.left = leaf
                break
            elif self.root.right is None and self.root.value <= leaf.value:
                leaf.parrent = self.root
                self.root.right = leaf
                break
            if parrent.value > leaf.value:
                if parrent.left is None:
                    leaf.parrent = parrent
                    parrent.left = leaf
                    break
                else:
                    parrent = parrent.left
                    continue
            elif parrent.value <= leaf.value:
                if parrent.right is None:
                    leaf.parrent = parrent
                    parrent.right = leaf
                    break
                else:
                    parrent = parrent.right 
                    continue

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
                parrent = None
                if flag:
                    self.root = tmp
                return tmp
            elif parrent.right is None: # no right branch
                tmp = parrent.left
                if parrent.left is not None:
                    tmp.parrent = parrent.parrent
                parrent = None
                if flag:
                    self.root = tmp
                return tmp
            tmp = self.minValue(parrent.right)
            if flag:
                self.root.value = tmp.value
            else:
                parrent.value = tmp.value
            parrent.right = self.delete(tmp.value, parrent.right)
        return parrent

    def rootUpdate(self, leaf, parrent):
        if parrent == self.root:
            self.root = leaf
        elif parrent == self.root.left:
            self.root.left = leaf
        elif parrent == self.root.right:
            self.root.right = leaf

    def rotateLeft(self, parrent):
        y = parrent.right
        z = y.left
        y.left = parrent
        y.parrent = parrent.parrent
        parrent.parrent = y
        parrent.right = z
        if z is not None:
            z.parrent = parrent

        if y.parrent is None: # Updating root
            self.root = y
        elif self.isRoot(y.parrent): # Updating root childs
            if y.parrent.left == parrent:
                self.root.left = y
            elif y.parrent.right == parrent:
                self.root.right = y
        else:
            if y.parrent.left == parrent:
                y.parrent.left = y
            elif y.parrent.right == parrent:
                y.parrent.right = y
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

        if y.parrent is None: # Updating root
            self.root = y
        elif self.isRoot(y.parrent): # Updating root childs
            if y.parrent.left == parrent:
                self.root.left = y
            elif y.parrent.right == parrent:
                self.root.right = y
        else:
            if y.parrent.left == parrent:
                y.parrent.left = y
            elif y.parrent.right == parrent:
                y.parrent.right = y
        return y

    def backbone(self, parrent, back=[]): # create backbone to build a new tree
        if parrent is None:
            return
        self.backbone(parrent.left, back)
        back.append(parrent.value)
        self.backbone(parrent.right, back)

    def backboneIter(self, root, back=[]): # create backbone (iteration) to build a new tree
        stack = []
        while True:
            if root is not None:
                stack.append(root)
                root = root.left
            elif stack:
                root = stack.pop()
                back.append(root.value)
                root = root.right
            else:
                break
    
    def dswIter(self, parrent): # DSW iteration algorithm
        backbone = []
        self.backboneIter(parrent, backbone)
        n = len(backbone)-1
        self.root = self.buildTree(backbone, 0, n)

    def dsw(self, parrent): # DSW algorithm
        backbone = []
        self.backbone(parrent, backbone)
        n = len(backbone)-1
        self.root = self.buildTree(backbone, 0, n)
        
    def buildTree(self, backbone, start, end): # build tree from backbone
        if start>end:
            return 
        mid = (start+end)//2
        root = Leaf(backbone[mid])
        root.left = self.buildTree(backbone, start, mid-1)
        if root.left is not None:
            root.left.parrent = root
        root.right = self.buildTree(backbone, mid+1, end)
        if root.right is not None:
            root.right.parrent = root
        return root

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
    
    def inOrderIter(self, root): # inorder iteration printing
        stack = []
        while True:
            if root is not None:
                stack.append(root)
                root = root.left
            elif stack:
                root = stack.pop()
                print("{} ".format(root.value), end="")
                root = root.right
            else:
                break

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

    def minValueIter(self, parrent):
        while parrent.left is not None:
            parrent = parrent.left
        return parrent

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

# myTree = Tree()
# myTree.insert(Leaf(10), myTree.root)
# myTree.insert(Leaf(20), myTree.root)
# myTree.insert(Leaf(30), myTree.root)
# myTree.insert(Leaf(40), myTree.root)
# myTree.insert(Leaf(50), myTree.root)
# myTree.insert(Leaf(60), myTree.root)
# myTree.insert(Leaf(70), myTree.root)
# myTree.insert(Leaf(80), myTree.root)
# myTree.insert(Leaf(90), myTree.root)
# myTree.insert(Leaf(100), myTree.root)
# print("###BST###")
# print("Root: ")
# print(myTree.root.value)
# myTree.printTree(myTree.root)
# print("\nMax value path: ")
# myTree.max(myTree.root)
# print("Min value path: ")
# myTree.min(myTree.root)
# myTree.delete(10, myTree.root) # delete 10 from tree
# myTree.delete(10, myTree.root) # delete 10 from tree
# print("After 10 delete")
# print("Root:")
# print(myTree.root.value)
# myTree.printTree(myTree.root)
# print("\nPreorder:")
# myTree.printTree(myTree.root)
# print("\nInorder:")
# myTree.inOrder(myTree.root)
# print("\nPostorder:")
# myTree.postOrder(myTree.root)
# print("\nPreorder:")
# myTree.printTree(myTree.root)
# myTree.dsw(myTree.root)
# print("\nAfter DSW")
# print("\nRoot:")
# print(myTree.root.value)
# print("\nPreorder:")
# myTree.printTree(myTree.root)
# print("\nMax value path: ")
# myTree.max(myTree.root)
# myTree.chopDown(myTree.root)
# print("\nAfter remove:")
# myTree.printTree(myTree.root)