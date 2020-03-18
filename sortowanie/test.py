import random 
import datetime
import bubble
import insertion
import selection

seed  = 2137

n = [1000]

def setupRandom(seed, n):
    random.seed(seed)
    x = [random.randint(1,n) for i in range(n)]
    return x

def setupConst(n):
    x = [1 for i in range(n)]
    return x

def setupDesc(n):
    x = [n-1 for i in range(n)]
    return x

def setupAsc(n):
    x = [i for i in range(n)]
    return x

def test(sort):
    print(sort+"test:")
    for i in n:
        pass
    if sort == "bubble":
        pass
print("Bubble sort test:")

for i in n:
    x = setupRandom(seed,i)
    before = datetime.datetime.utcnow().timestamp()
    bubble.sort(x)
    after = datetime.datetime.utcnow().timestamp()
    #print(x)
    print("Time for n = "+str(i))
    print(after-before)

print("Insertion sort test:")

for i in n:
    x = setupRandom(seed,i)
    before = datetime.datetime.utcnow().timestamp()
    insertion.sort(x)
    after = datetime.datetime.utcnow().timestamp()
    #print(x)
    print("Time for n = "+str(i))
    print(after-before)

print("Selection sort test:")

for i in n:
    x = setupRandom(seed,i)
    before = datetime.datetime.utcnow().timestamp()
    selection.sort(x)
    after = datetime.datetime.utcnow().timestamp()
    #print(x)
    print("Time for n = "+str(i))
    print(after-before)