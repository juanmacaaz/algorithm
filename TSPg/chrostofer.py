#pip3 install scipy
#pip3 install munkres
#pip3 install networkx

import christofides

nV = 5

INF = 9999

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
    for x in x1:
        for y in x:
            print(chr(y+97), end=' ')
        print()

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
    return dist

def bimatrix(graph):
    matrix = graph
    for i in range(0, len(matrix)):
        for j in range(0, len(matrix)):
            matrix[j][i] = graph[i][j]
    return matrix

def printSolution(dist): 
    print("-------------------------")
    for i in range(nV): 
        for j in range(nV): 
            if(dist[i][j] == INF): 
                print("INF", end =" ")
            else: 
                print(dist[i][j], end ="  ")  
        print(" ")

matrix = [[0, 30, 15, INF, 10],
         [0, 0, 9, 50, 20],
         [0, 0, 0, 10, INF],
         [0, 0, 0, 0, 100],
         [0, 0, 0, 0, 0]]

matrix = floydWarshall(bimatrix(matrix))
cpMatrix = matrix
for columna in range(len(matrix)):
    for fila in range(len(matrix)):
        if fila >= columna:
            cpMatrix[fila][columna] = 0

print(cpMatrix)

christofides.compute(cpMatrix)