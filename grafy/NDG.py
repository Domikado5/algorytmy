import numpy as np
import random as rn
from termcolor import colored
import copy

def generateNonDirectedHamiltonianGraph(nM, nL, eT, v, s):
    # every column need one or more connections
    edges = ((v*(v-1))//2)*s # ile krawedzi bedzie mial graf
    bonusEdges = edges - v # cykl hamiltona potrzebuje tyle krawedzi ile jest wierzcholkow (v) reszta wierzcholkow generowana losowo
    
    hamilton = [ i for i in range(v) ]
    st = hamilton.pop(0)
    rn.shuffle(hamilton)
    hamilton = [st] + hamilton + [st]

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
        
        free = np.where(nM == 0)
        free = np.stack((free[0], free[1]), axis=1)
        indices = np.where( (( free[:,0] != free[:,1] ) & ( free[:,0] == y )) )[0] # losowanie dwoch kolejnych wiercholkow zeby zachowac parzystosc stopni wierzcholkow
        z = free[np.random.choice(indices)][1]
        nM[y][z] = 1
        nM[z][y] = 1
        bonusEdges -= 1

        nM[z][x] = 1
        nM[x][z] = 1
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



def Euler(current, v, nM):
    global result

    for i in range(v):
        if nM[current][i]:
            nM[current][i] = 0
            nM[i][current] = 0
            Euler(i, v, nM)
    
    result.append(current)

def EulerCheck(current, v, nM):
    Euler(current, v, nM)

    if(np.count_nonzero(nM == 1) == 0):
        return True
    else:
        return False



def nextVer(nM, current, r, p):
    if nM[ r[p-1] ][ current ] == 0:
        return False

    for i in r:
        if i == current:
            return False
    
    return True

def Hamilton(v, nM, p, r): # vertices neighborhood matrix possition results/path
    if p == v:
        if nM[ r[ p-1 ] ][ r[ 0 ] ] == 1:
            return True
        else:
            return False
    
    for i in range(1,v):
        if nextVer(nM, i, r, p):
            
            r[p] = i # add vertice to the result/path

            if Hamilton(v, nM, p+1, r):
                return True
            
            r[p] = -1

    return False

def HamiltonCheck(v, nM, r):
    r[0] = 0

    if not Hamilton(v, nM, 1, r):
        return False
    
    return True


vertices = 5 # liczba wierzcholkow
neighborhoodMatrix = np.zeros((vertices,vertices), dtype=int) # macierz sasiedztw / neighborhoodMatrix
neighborhoodList = [[] for i in range(vertices)]
edgesTable = []
saturation = [0.3, 0.7] # nasycenie grafu

print("\n",colored("Graf hamiltonowski 30%", 'white', 'on_grey', attrs=['bold']))
generateNonDirectedHamiltonianGraph(neighborhoodMatrix, neighborhoodList, edgesTable, vertices, saturation[0])
print("\n",colored("Macierz:", 'white', attrs=['bold']))
print(neighborhoodMatrix)
print("\n",colored("Lista nastepnikow:", 'white', attrs=['bold']))
print(neighborhoodList)
print("\n",colored("Krawedzie:", 'white', attrs=['bold']))
print(edgesTable)
print("Ilosc krawedzi: ",len(edgesTable)/2)

path = [ -1 for i in range(vertices) ]

if HamiltonCheck(vertices, neighborhoodMatrix, path):
    print(colored("Cykl Hamiltona: ", 'white', attrs=['bold']), path+[0])
else:
    print(colored("Cykl Hamiltona nie istnieje.", 'white', attrs=['bold']))

neighborhoodMatrix2 = neighborhoodMatrix.copy() # kopiowanie macierzy sasiedztw
result = []
if EulerCheck(0, vertices, neighborhoodMatrix2):
    print(colored("Cykl Eulera:", 'white', attrs=['bold']), result)
else:
    print(colored("Nie istnieje cykl Eulera", 'white', attrs=['bold']))
print("Dlugosc cyklu eulera: ", len(result))

neighborhoodMatrix = np.zeros((vertices,vertices), dtype=int) # zerowanie danych
neighborhoodList = [[] for i in range(vertices)]
edgesTable = []

print("\n",colored("Graf hamiltonowski 70%", 'white', 'on_grey', attrs=['bold']))
generateNonDirectedHamiltonianGraph(neighborhoodMatrix, neighborhoodList, edgesTable, vertices, saturation[1])
print("\n",colored("Macierz:", 'white', attrs=['bold']))
print(neighborhoodMatrix)
print("\n",colored("Lista nastepnikow:", 'white', attrs=['bold']))
print(neighborhoodList)
print("\n",colored("Krawedzie:", 'white', attrs=['bold']))
print(edgesTable)
print("Ilosc krawedzi: ",len(edgesTable)/2)

path = [ -1 for i in range(vertices)]

if HamiltonCheck(vertices, neighborhoodMatrix, path):
    print(colored("Cykl Hamiltona: ", 'white', attrs=['bold']), path+[0])
else:
    print(colored("Cykl Hamiltona nie istnieje.", 'white', attrs=['bold']))

neighborhoodMatrix2 = neighborhoodMatrix.copy() # kopiowanie macierzy sasiedztw
result = []
if EulerCheck(0, vertices, neighborhoodMatrix2):
    print(colored("Cykl Eulera:", 'white', attrs=['bold']), result)
else:
    print(colored("Nie istnieje cykl Eulera", 'white', attrs=['bold']))
print("Dlugosc cyklu eulera: ", len(result))

vertices = 10

neighborhoodMatrix = np.zeros((vertices,vertices), dtype=int) # macierz sasiedztw / neighborhoodMatrix
neighborhoodList = [[] for i in range(vertices)]
edgesTable = []

print("\n",colored("Graf 50% nie hamiltonowski", 'white', 'on_grey', attrs=['bold']))
generateNonDirectedNonHamiltonianGraph(neighborhoodMatrix, neighborhoodList, edgesTable, vertices)
print("\n",colored("Macierz:", 'white', attrs=['bold']))
print(neighborhoodMatrix)
print("\n",colored("Lista nastepnikow:", 'white', attrs=['bold']))
print(neighborhoodList)
print("\n",colored("Krawedzie:", 'white', attrs=['bold']))
print(edgesTable)

path = [ -1 for i in range(vertices)]

if HamiltonCheck(vertices, neighborhoodMatrix, path):
    print(colored("Cykl Hamiltona: ", 'white', attrs=['bold']), path+[0])
else:
    print(colored("Cykl Hamiltona nie istnieje.", 'white', attrs=['bold']))