import NDG
import time
import sys
import numpy as np


sys.setrecursionlimit(10**9)

f = open("euler.txt",'w')

vertices = [40,45,50,55,60,65,70,75,80,85]
saturation = [0.3, 0.7]

result0 = 'vertices'

for v in vertices:
    result0 += ';' + str(v)

f.write(result0+'\n')

result1 = 'Euler 30%;'
result2 = 'Euler 70%;'

for v in vertices:
    
    print(v)

    # wygenerowanie pustych danych dla grafow 30%

    neighborhoodMatrix = np.zeros((v, v), dtype=int)
    neighborhoodList = [[] for i in range(v)]
    edgesTable = []

    NDG.generateNonDirectedHamiltonianGraph(neighborhoodMatrix, neighborhoodList, edgesTable, v, saturation[0])
    print("Wygenerowano macierz dla 30%")

    #Euler 30%
    neighborhoodMatrix2 = neighborhoodMatrix.copy()
    result = []

    before = time.time()*1000
    x = NDG.EulerCheck(0, v, neighborhoodMatrix2, result)
    after = time.time()*1000

    ms = round(after-before,1)

    print("Euler 30% ", ms)

    result1 += str(ms) + ';'

    # wygenerowanie danych dla 70%

    neighborhoodMatrix = np.zeros((v,v), dtype=int)
    neighborhoodList = [[] for i in range(v)]
    edgesTable = []

    NDG.generateNonDirectedHamiltonianGraph(neighborhoodMatrix, neighborhoodList, edgesTable, v, saturation[1])
    
    #Euler 70%
    neighborhoodMatrix2 = neighborhoodMatrix.copy()
    result = []

    before = time.time()*1000
    x = NDG.EulerCheck(0, v, neighborhoodMatrix2, result)
    after = time.time()*1000

    ms = round(after-before,1)

    print("Euler 70% ", ms)

    result2 += str(ms) + ';'

f.write(result1+'\n')
f.write(result2+'\n')
f.close()