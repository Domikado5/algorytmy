def shiftDown(a, n, i):
    leftBranch = 2 * i + 1
    rightBranch = 2 * i + 2
    root = i

    if leftBranch < n and a[root] < a[leftBranch]:
        root = leftBranch

    if rightBranch < n and a[root] < a[rightBranch]:
        root = rightBranch

    if root != i:
        a[i], a[root] = a[root], a[i]
        shiftDown(a, n, root)

def createHeap(a):
    for i in range(len(a), -1, -1):
        shiftDown(a, len(a), i)
           
def sort(a):
    createHeap(a)
    for i in range(len(a)-1, 0, -1):
        a[0] , a[i] = a[i], a[0]
        shiftDown(a, i, 0)
    return a