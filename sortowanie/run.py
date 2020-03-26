import random 
import time
import bubble
import insertion
import selection
import counting
import heap
import quickRight
import quickRandom
import merge
import shell
import sys

sys.setrecursionlimit(1000000)
seed  = 5937 # seed do losowania tablic
n = [10000,20000,30000,40000,50000] # wielkosci tablic
maxNumber = 1000000 # maksymalny zakres liczb
f = open("results.txt",'w+')

def setupRandom(seed, n):
    random.seed(seed)
    x = [random.randint(1,maxNumber) for i in range(n)]
    return x

def setupConst(n):
    x = [maxNumber for i in range(n)]
    return x

def setupDesc(n):
    x = [n-1 for i in range(n)]
    return x

def setupAsc(n):
    x = [i for i in range(n)]
    return x

def setupA(n):
    x1 = [i for i in range(n) if i%2==0 ]
    x2 = [i for i in range(n,0,-1) if i%2!=0]
    x = x1 + x2
    return x

sortType = [3,8,7,4,2,1,0]
# pominieto quicksorty z uwagi na przekroczenie maksymalnej rekurencji

for s in sortType:
    if s == 0:
        sortName = "Bubble"
    elif s == 1:
        sortName = "Insertion"
    elif s == 2:
        sortName = "Selection"
    elif s == 3:
        sortName = "Counting"
    elif s == 4:
        sortName = "Heap"
    elif s == 5:
        sortName = "Quick (right)"
    elif s == 6:
        sortName = "Quick (random)"
    elif s == 7:
        sortName = "Shell"
    elif s == 8:
        sortName = "Merge"
    f.write(sortName+"\n")
    print(sortName)
    for i in n:
        tmpTime = 'i'
        for j in range(5):
            if j == 0:
                x = setupRandom(seed,i)
            elif j == 1:
                x = setupConst(i)
            elif j == 2:
                x = setupDesc(i)
            elif j == 3:
                x = setupAsc(i)
            elif j == 4:
                x = setupA(i)
            before = round(time.time_ns() / (10 ** 9),10)
            if s == 0:
                x = bubble.sort(x)
            elif s == 1:
                x = insertion.sort(x)
            elif s == 2:
                x = selection.sort(x)
            elif s == 3:
                x = counting.sort(x, i, maxNumber)
            elif s == 4:
                x = heap.sort(x)
            elif s == 5:
                x = quickRight.sort(x,0,i-1)
            elif s == 6:
                x = quickRandom.sort(x,0,i-1)
            elif s == 7:
                x = shell.sort(x)
            elif s == 8:
                x = merge.sort(x,0,len(x)-1)
            after = round(time.time_ns() / (10 ** 9),10)
            #print(x)
            tmpTime += ';' + str(after-before)
            print(after-before)
        f.write(tmpTime+"\n")
        print(tmpTime)
    f.write('\n')
f.close()