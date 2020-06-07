import numpy as np
import random as rn
from termcolor import colored
import copy


vertices = 10 # liczba wierzcholkow
neighborhoodMatrix = np.zeros((vertices,vertices), dtype=int) # macierz sasiedztw / neighborhoodMatrix
neighborhoodList = [[] for i in range(vertices)]
edgesTable = []
saturation = [0.3, 0.7]


def generateNonDirectedHamiltonianGraph(nM, nL, eT, v, s):
    # every column need one or more connections
    edges = ((vertices*(vertices-1))//2)*s # ile krawedzi bedzie mial graf
    bonusEdges = edges - v # cykl hamiltona potrzebuje tyle krawedzi ile jest wierzcholkow (v) reszta wierzcholkow generowana losowo
    
    hamilton = [ i for i in range(v) ]
    rn.shuffle(hamilton)
    hamilton += [hamilton[0]]

    for i in range(v): # generowanie cyklu hamiltona
        nM[hamilton[i]][hamilton[i+1]] = 1
        nM[hamilton[i+1]][hamilton[i]] = 1

    while bonusEdges > 0: # generowanie macierzy
        free = np.where(nM == 0)
        free = np.stack((free[0], free[1]), axis=1)
        indices = np.where(free[:,0] != free[:,1])[0]
        x, y = free[np.random.choice(indices)]
        nM[x][y] = 1
        nM[y][x] = 1
        bonusEdges -= 1

    for i in range(v):
        connections = np.where(nM[i][:] == 1)
        nL[i] = list(connections[0])
        eT += [[i,j] for j in nL[i]] 

generateNonDirectedHamiltonianGraph(neighborhoodMatrix, neighborhoodList, edgesTable, vertices, saturation[0])
print("Macierz:")
print(neighborhoodMatrix)
print("Lista nastepnikow:")
print(neighborhoodList)
print("Krawedzie:")
print(edgesTable)
generateNonDirectedHamiltonianGraph(neighborhoodMatrix, neighborhoodList, edgesTable, vertices, saturation[1])
print("Macierz:")
print(neighborhoodMatrix)
print("Lista nastepnikow:")
print(neighborhoodList)
print("Krawedzie:")
print(edgesTable)