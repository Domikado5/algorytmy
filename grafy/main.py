import numpy as np
import random as rn
from termcolor import colored


vertices = 10 # liczba wierzcholkow
neighborhoodMatrix = np.zeros((vertices,vertices), dtype=int) # macierz sasiedztw / neighborhoodMatrix
neighborhoodList = [[] for i in range(vertices)]
edgesTable = []

def generateDirectedGraph(nM, nL, eT, v): # generowanie grafu prosta metodą / wypełnianie tylko wartości w górnym trójkącie
    # every column need one or more connections
    edges = (vertices*(vertices-1))//4
    bonusEdges = edges - (v - 1)
    players = [ i for i in range(2, v) ]
    winners = np.zeros(bonusEdges, dtype=int)
    i = 0
    begin = 2

    while bonusEdges > 0:
        winner = rn.choice(players)
        count = np.count_nonzero(winners == winner)
        if count < winner-1:
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
    
def generateNonDirectedGraph():
    pass


def BFS(nL, v):
    visited = []
    queue = []
    visited.append(0)
    queue = np.unique(np.concatenate((queue, nL[0])))
    queue = queue.astype('int32')
    print("Odwiedzone", visited, " Kolejka ",queue)
    while len(visited) < v:
        nextVer = queue[0]
        visited.append(nextVer)
        for i in range(len(nL[nextVer])):
            if nL[nextVer][i] not in visited and nL[nextVer][i] not in queue: # sprawdzanie czy wierzchołek już wystąpił
                queue = np.append(queue, nL[nextVer][i])
        queue = np.delete(queue, 0)
        print("Odwiedzone", visited, " Kolejka ", queue)
        
        
def DFS(nL, v, s=0):
    visited = []
    stack = []
    visited.append(s)
    stack = np.array(stack + nL[s][::-1])
    print("Odwiedzone", visited, " Stos ", stack)
    while len(visited) < v:
        nextVer = stack[-1]
        stack = np.delete(stack, -1)
        visited.append(nextVer)
        tmp = []
        if nL[nextVer]:
            tmp = nL[nextVer][::-1]
        for x in tmp:
            if x not in visited and x not in stack: # sprawdzanie czy wierzchołek już wystąpił
                stack = np.append(stack, x)
        print("Odwiedzone", visited, " Stos ", stack)    


generateDirectedGraph(neighborhoodMatrix, neighborhoodList, edgesTable, vertices)
print(colored("Macierz sasiedztw: \n", 'white', attrs=['bold']), neighborhoodMatrix)
print(colored("\nLista następnikow: \n", 'white', attrs=['bold']), neighborhoodList)
print(colored("\nTabela krawedzi: \n", 'white', attrs=['bold']), edgesTable)
print(colored("\nPrzechodzenie wszerz:", 'white', attrs=['bold']))
BFS(neighborhoodList, vertices)
print(colored("\nPrzechodzenie w głąb:", 'white', attrs=['bold']))
DFS(neighborhoodList, vertices)