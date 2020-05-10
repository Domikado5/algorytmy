import numpy as np
import random as rn


vertices = 5 # liczba wierzcholkow
neighborhoodMatrix = np.zeros((vertices,vertices), dtype=int) # macierz sasiedztw / neighborhoodMatrix
neighborhoodList = [[] for i in range(vertices)]
edgesTable = []

def generateGraph(nM, nL, eT, v): # generowanie grafu prosta metodą / wypełnianie tylko wartości w górnym trójkącie
    # every column need one or more connection
    edges = (vertices*(vertices-1))//4
    bonusEdges = edges - (v - 1)
    players = [i for i in range(2, v)]
    winners = np.zeros(bonusEdges, dtype=int)
    i = 0
    begin = 2
    while bonusEdges > 0:
        winner = rn.choice(players)
        count = np.count_nonzero(winners == winner)
        if count < winner:
            winners[i] = winner
            bonusEdges -= 1
            i += 1
        else:
            players.remove(winner)
    for i in range(1, v):
        nM[rn.randint(0,i-1)][i] = 1
        count = np.count_nonzero(winners == i)
        while count > 0:
            findBonus = np.where(nM[0:i,i] == 0)
            findBonus = np.copy(findBonus[0])
            j = np.random.choice(findBonus)
            nM[j][i] = 1
            count -= 1
    for i in range(v):
        connections = np.where(nM[i][:] == 1)
        nL[i] = list(connections[0])
        eT += [[i,j] for j in nL[i]] 
    

generateGraph(neighborhoodMatrix, neighborhoodList, edgesTable, vertices)
print("Macierz sasiedztw: \n", neighborhoodMatrix)
print("Lista następnikow: \n", neighborhoodList)
print("Tabela krawedzi: \n", edgesTable)