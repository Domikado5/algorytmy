import DG
import time
import sys
import numpy as np


sys.setrecursionlimit(10**9)

f = open("fs.txt",'w')

vertices = [50,100,150,200,250,300,350,400,450,500]

result0 = 'vertices'

for v in vertices:
    result0 += ';' + str(v)

f.write(result0+'\n')

result1 = 'BFSsort;'
result2 = 'DFSsort;'

for v in vertices:
    
    print(v)

    neighborhoodMatrix = np.zeros((v, v), dtype=int)
    neighborhoodList = [[] for i in range(v)]
    edgesTable = []

    DG.generateDirectedGraph(neighborhoodMatrix, neighborhoodList, edgesTable, v)

    #BFSsort test
    before = time.time()*1000
    x = DG.BFSsort(neighborhoodList, v)
    after = time.time()*1000

    ms = round(after-before,1)

    print("BFSsort ", ms)

    result1 += str(ms) + ';'
    
    #DFSsort test
    before = time.time()*1000
    x = DG.DFSsort(neighborhoodList, v)
    after = time.time()*1000

    ms = round(after-before,1)

    print("DFSsort ", ms)

    result2 += str(ms) + ';'


f.write(result1+'\n')
f.write(result2+'\n')
f.close()