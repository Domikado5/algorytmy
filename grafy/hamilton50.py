import NDG
import time
import sys
import numpy as np


sys.setrecursionlimit(10**9)

f = open("hamilton50.txt",'w')

vertices = [10,11,12,13,14]

result0 = 'vertices'

for v in vertices:
    result0 += ';' + str(v)

f.write(result0+'\n')

result1 = 'Hamilton 50%;'

for v in vertices:
    
    print(v)

    #wygenerowanie pustych danych dla grafu 50%
    neighborhoodMatrix = np.zeros((v,v), dtype=int)
    neighborhoodList = [[] for i in range(v)]
    edgesTable = []

    NDG.generateNonDirectedNonHamiltonianGraph(neighborhoodMatrix, neighborhoodList, edgesTable, v)

    #Hamilton 50%
    path = [ -1 for i in range(v)]

    before = time.time()*1000
    x = NDG.HamiltonCheck(v, neighborhoodMatrix, path)
    after = time.time()*1000

    ms = round(after-before,1)

    print("Hamilton 50% ", ms)

    result1 += str(ms) + ';'

f.write(result1+'\n')
f.close()