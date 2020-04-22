import avl
import bst
import time
import sys

sys.setrecursionlimit(10**6)

def generateNum(n):
    return [i for i in range(n,0,-1)]

f = open("results.txt",'w+')
# n = [10]
n = [10000,20000,30000,40000,50000,60000,70000,80000,90000,100000]
result1 = 'Build;'
result2 = 'Min;'
result3 = 'Inorder;'
# AVL test
for num in n:
    x = generateNum(num)
    tree = avl.Tree()
    before = time.time()*1000
    for value in x:
        tree.insert(avl.Leaf(value), tree.root) # insert test
    after = time.time()*1000
    ms = round(after-before,1)
    result1 += str(ms)+';'
    before = time.time()*1000
    print(tree.minValue(tree.root)) # minimum value test
    after = time.time()*1000
    ms = round(after-before,1)
    result2 += str(ms)+';'
    before = time.time()*1000
    tree.inOrder(tree.root) # inorder test
    after = time.time()*1000
    ms = round(after-before,1)
    result3 += str(ms)+';'
print(result1)
print(result2)
print(result3)
f.write("AVL\n")
f.write(result1+'\n')
f.write(result2+'\n')
f.write(result3+'\n')

result1 = 'Build;'
result2 = 'Min;'
result3 = 'Inorder;'
result4 = 'DSW;'
# BST test
for num in n:
    x = generateNum(num)
    tree = bst.Tree()
    before = time.time()*1000
    for value in x:
        tree.insertIter(bst.Leaf(value), tree.root) # insert test
    after = time.time()*1000
    ms = round(after-before,1)
    result1 += str(ms)+';'
    before = time.time()*1000
    print(tree.minValueIter(tree.root)) # minimum value test
    after = time.time()*1000
    ms = round(after-before,1)
    result2 += str(ms)+';'
    before = time.time()*1000
    tree.inOrderIter(tree.root) # inorder test
    after = time.time()*100
    ms = round(after-before,1)
    result3 += str(ms)+';'
    before = time.time()*1000
    tree.dswIter(tree.root) #dsw test
    after = time.time()*100
    ms = round(after-before,1)
    result4 += str(ms)+';'
print(result1)
print(result2)
print(result3)
print(result4)
f.write("BST\n")
f.write(result1+'\n')
f.write(result2+'\n')
f.write(result3+'\n')
f.write(result4+'\n')