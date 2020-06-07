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
    edges = ((v*(v-1))//2)*s # ile krawedzi bedzie mial graf
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

def generateNonDirectedNonHamiltonianGraph(nM, nL, eT, v):
    edges = ((v*(v-1))//4) # ile krawedzi bedzie mial graf
    edges -= 1 # usuniecie jednej krawedzi ktora bd prowadzic do odizolowanego wierzcholka
    
    vertices = [ i for i in range(v) ]
    rn.shuffle(vertices)
    isolated = vertices.pop() # losowe wybranie odizolowanego wierzcholka
    
    nM[isolated][vertices[0]] = 1 # wybranie losowej krawedzi prowadzacej do izolowanego wierzcholka
    nM[vertices[0]][isolated] = 1
    
    while edges > 0: # losowanie reszty krawedzi
        free = np.where(nM == 0)
        free = np.stack((free[0], free[1]), axis=1)
        indices = np.where((free[:,0] != free[:,1]) & (free[:,0] != isolated) & (free[:,1] != isolated))[0]
        x, y = free[np.random.choice(indices)]
        nM[x][y] = 1
        nM[y][x] = 1
        edges -= 1

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

neighborhoodMatrix = np.zeros((vertices,vertices), dtype=int) # macierz sasiedztw / neighborhoodMatrix
neighborhoodList = [[] for i in range(vertices)]
edgesTable = []

generateNonDirectedHamiltonianGraph(neighborhoodMatrix, neighborhoodList, edgesTable, vertices, saturation[1])
print("Macierz:")
print(neighborhoodMatrix)
print("Lista nastepnikow:")
print(neighborhoodList)
print("Krawedzie:")
print(edgesTable)

neighborhoodMatrix = np.zeros((vertices,vertices), dtype=int) # macierz sasiedztw / neighborhoodMatrix
neighborhoodList = [[] for i in range(vertices)]
edgesTable = []

generateNonDirectedNonHamiltonianGraph(neighborhoodMatrix, neighborhoodList, edgesTable, vertices)
print("Macierz:")
print(neighborhoodMatrix)
print("Lista nastepnikow:")
print(neighborhoodList)
print("Krawedzie:")
print(edgesTable)