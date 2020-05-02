import itertools

#Numero de variables
nV = 8

INF = 99999

def initRecorridos():
    recorridos = []
    index = 0
    for x in range(nV):
        subrecorrido = []
        for y in range(nV):
            subrecorrido.append(index)
        recorridos.append(subrecorrido)
        index+=1
    return recorridos

def printRecorridos(x1):
    print("La matriz de recorridos es: ")
    print('  ', end='')
    for x in range(nV):
        print(chr(x+97),end=' ')
    print()
    print('-------------')
    i = 0
    for x in x1:
        print(chr(i+97), end='-')
        for y in x:
            print(chr(y+97), end=' ')
        print()
        i+=1

def floydWarshall(graph):
    recorridos = initRecorridos()
    dist = list(map(lambda i : list(map(lambda j : j, i)), graph) )
    for k in range(nV): 
        for i in range(nV): 
            for j in range(nV): 
                dt = dist[i][k] + dist[k][j]
                if dist[i][j] > dt:
                    dist[i][j] = dt
                    recorridos[i][j] = k
        printSolution(dist) 
    printRecorridos(recorridos)
    return dist, recorridos

def printSolution(dist): 
    print("-------------------------")
    print('  ', end='')
    for x in range(nV):
        print(chr(x+97),end='\t')
    print()
    for i in range(nV): 
        print(chr(i+97), end='-')
        for j in range(nV): 
            if(dist[i][j] == INF): 
                print("INF", end ="\t")
            else: 
                print(dist[i][j], end ="\t")  
        print(" ")

def muestraCamino(parejaMinima):
    for x in parejaMinima:
        for y in x:
            print(chr(y+97).upper(), end='')
        print(' ', end='')

def bimatrix(graph):
    matrix = graph
    for i in range(0, len(matrix)):
        for j in range(0, len(matrix)):
            matrix[j][i] = graph[i][j]
    return matrix


def subconjuntoSenares(matrix):
    verticesValidos = []
    matrixValidos = []
    index = 0
    for x in matrix:
        count = 0
        for y in x:
            if y != 0 and y != INF:
                count+=1
        if (count%2) != 0:
            verticesValidos.append(index)
        index+=1
    index = 0
    for x in matrix:
        submatrix = []
        subindex = 0
        for y in x:
            if subindex in verticesValidos:
                submatrix.append(y)
        if index in verticesValidos:
            matrixValidos.append(submatrix)
    return verticesValidos, matrixValidos
        

# Formato [[]]
graph =     [[0,8,20,INF,2,INF,INF,INF],
            [0,0,10,8,INF,2,INF,INF],
            [0,0,0,8,INF,INF,2,INF],
            [0,0,0,0,INF,INF,INF,2],
            [0,0,0,0,0,3,20,10],
            [0,0,0,0,0,0,INF,3],
            [0,0,0,0,0,0,0,2],
            [0,0,0,0,0,0,0,0]]

graph = bimatrix(graph)

printSolution(graph)

matrixR, recorridos = floydWarshall(graph)

vertices , matrix = subconjuntoSenares(graph)

print('Lista de valores senares: ')
[print(chr(x+97).upper(), end = '') for x in vertices]
print()

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
print(combinacionesParejas)
print('Se puede emparejar de x maneras:')
print(len(combinacionesParejas))

minimo = 9999
for x in combinacionesParejas:
    suma = matrixR[x[0][0]][x[0][1]]+matrixR[x[1][0]][x[1][1]]
    if suma < minimo:
        minimo = suma
        parejaMinima = x

print('La pareja minima es: ')
muestraCamino(parejaMinima)
print('(Con un peso de:',minimo,')')

camino = []

caminoA = []
step = recorridos[parejaMinima[0][0]][parejaMinima[0][1]]
caminoA.append(step)
while step != recorridos[step][parejaMinima[0][1]]:
    step = recorridos[step][parejaMinima[0][1]]
    caminoA.append(step)

if parejaMinima[0][0] != caminoA[0]:
    camino.append([parejaMinima[0][0], caminoA[0]])
i = 0
for x in range(len(caminoA)-1):
    camino.append([caminoA[i], caminoA[i+1]])
    i+=1
camino.append([caminoA[i], parejaMinima[0][1]])

caminoB = []
step = recorridos[parejaMinima[1][0]][parejaMinima[1][1]]
caminoB.append(step)
while step != recorridos[step][parejaMinima[1][1]]:
    step = recorridos[step][parejaMinima[1][1]]
    caminoB.append(step)

if parejaMinima[1][0] != caminoB[0]:
    camino.append([parejaMinima[1][0], caminoB[0]])
i = 0
for x in range(len(caminoB)-1):
    camino.append([caminoB[i], caminoB[i+1]])
    i+=1
camino.append([caminoB[i], parejaMinima[1][1]])

print('El camino a multiplicar es: ')
muestraCamino(camino)

pesoTotal = 0
for x in camino:
    pesoTotal += graph[x[0]][x[1]]

print()
print('El peso del camino a multiplicar es: ')
print(pesoTotal)

pesoGrafo = 0

for x in graph:
    for y in x:
        if y != INF:
            pesoGrafo+=y

print('El peso del grafo euleiano es:')
print((pesoGrafo/2)+minimo)