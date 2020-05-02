import networkx as nx
import numpy as np
import scipy
import itertools

def muestraCamino(ls):
    for x in ls:
        for y in x:
            print(chr(y+97).upper(), end='')
        print(' ', end='')

def perejasMinimas(combinacionesParejas, matrixR):
    minimo = 9999
    for x in combinacionesParejas:
        suma = matrixR[x[0][0]][x[0][1]]+matrixR[x[1][0]][x[1][1]]
        if suma < minimo:
            minimo = suma
            parejaMinima = x
    return parejaMinima, minimo

def combinatoria(vertices):
    combinaciones = list(itertools.combinations(vertices, 2))
    combinacionesParejas = list(itertools.combinations(combinaciones, 2))
    aux = []
    aux2 = []
    for x in combinaciones:
        for y in combinaciones:
            if x[0] not in y and x[1] not in y:
                if [y,x] not in aux and x not in aux2 and y not in aux2:
                    aux.append([x,y])
                    aux2.append(x)
                    aux2.append(y)
    combinacionesParejas = aux
    return len(combinacionesParejas), combinacionesParejas

def printGraf(G):
    for x in G:
        print(chr(x[0]+97).upper() + chr(x[1]+97).upper(), end= ',')
    print()

def getNodosImpares(G):
    nodesValid = []
    for x in G.degree:
        if (x[1]%2 != 0):
            nodesValid.append(x[0])
    return nodesValid

def bimatrix(graph):
    matrix = graph
    for i in range(0, len(matrix)):
        for j in range(0, len(matrix)):
            matrix[j][i] = graph[i][j]
    return matrix

initMatrix = bimatrix([ [0,15,13,14,10],
                        [0,0,7,18,12],
                        [0,0,0,14,8],
                        [0,0,0,0,8],
                        [0,0,0,0,0]])

cinitMatrix = initMatrix

initMatrix = np.matrix(initMatrix)

G = nx.from_numpy_matrix(initMatrix)

treeGenratorEdges = sorted(list(nx.minimum_spanning_edges(G)))
treeGenratorGraf  = nx.minimum_spanning_tree(G)

printGraf(treeGenratorEdges)
print(treeGenratorGraf.size(weight='weight'))
nodosEscogidos = getNodosImpares(treeGenratorGraf)
[print(chr(x+97).upper(), end='') for x in nodosEscogidos]
print()
size , combinaciones = combinatoria(nodosEscogidos)
print(size)
parejasMinima, minima = perejasMinimas(combinaciones, cinitMatrix)
muestraCamino(sorted(parejasMinima))
print()
print(minima)

grafoPreparado = []
for x in treeGenratorEdges:
    grafoPreparado.append((x[0], x[1]))

for x in parejasMinima:
    grafoPreparado.append(x)

nuevalista = []
yaCogidos = []

def minValue(valor):
    listsTemp = []
    for x in grafoPreparado:
        if valor in x:
            if grafoPreparado.count(x) == 2:
                return x

    for x in grafoPreparado:
        if valor in x:
            listsTemp.append(x)
    return min(listsTemp)


print(grafoPreparado)

def getVertex(actual, profucndidad):
    nuevalista.append(actual)
    profucndidad += 1
    for x in grafoPreparado:
        if x == minValue(actual):
            grafoPreparado.remove(x)
            if x[0] == actual:
                getVertex(x[1], profucndidad)
            else:
                getVertex(x[0], profucndidad)
            

getVertex(0, 0)
[print(chr(x+97).upper(), end='') for x in nuevalista]
print()
newList = []
for x in nuevalista:
    if x not in newList:
        newList.append(x)
newList.append(nuevalista[0])
[print(chr(x+97).upper(), end='') for x in newList]

verticesParaLaSuma = []
for x in range(len(newList)-1):
    verticesParaLaSuma.append([newList[x],newList[x+1]])

sumaTotal = 0
for x in verticesParaLaSuma:
    sumaTotal+=cinitMatrix[x[0]][x[1]]
print()
print(sumaTotal)
print((sumaTotal*2)/3)