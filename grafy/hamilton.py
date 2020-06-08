import NDG
import time
import sys
import numpy as np


sys.setrecursionlimit(10**9)

f = open("hamilton.txt",'w')

vertices = [100,200,300,400,500,600,700,800,900,1000]
saturation = [0.3, 0.7]

result0 = 'vertices'

for v in vertices:
    result0 += ';' + str(v)

f.write(result0+'\n')

result1 = 'Hamilton 30%;'
result2 = 'Hamilton 70%;'

for v in vertices:
    
    print(v)

    # wygenerowanie pustych danych dla grafow 30%

    neighborhoodMatrix = np.zeros((v, v), dtype=int)
    neighborhoodList = [[] for i in range(v)]
    edgesTable = []

    NDG.generateNonDirectedHamiltonianGraph(neighborhoodMatrix, neighborhoodList, edgesTable, v, saturation[0])
    print("Wygenerowano macierz dla 30%")

    # hamilton 30%

    path = [ -1 for i in range(v) ]

    before = time.time()*1000
    x = NDG.HamiltonCheck(v, neighborhoodMatrix, path)
    after = time.time()*1000

    ms = round(after-before,1)

    print("Hamilton 30% ", ms)

    result1 += str(ms) + ';'

    # wygenerowanie pustych danych dla grafow 70%

    neighborhoodMatrix = np.zeros((v,v), dtype=int)
    neighborhoodList = [[] for i in range(v)]
    edgesTable = []

    NDG.generateNonDirectedHamiltonianGraph(neighborhoodMatrix, neighborhoodList, edgesTable, v, saturation[1])

    # hamilton 70%

    path = [ -1 for i in range(v) ]

    before = time.time()*1000
    x = NDG.HamiltonCheck(v, neighborhoodMatrix, path)
    after = time.time()*1000

    ms = round(after-before,1)

    print("Hamilton 70% ", ms)

    result2 += str(ms) + ';'


f.write(result1+'\n')
f.write(result2+'\n')
f.close()