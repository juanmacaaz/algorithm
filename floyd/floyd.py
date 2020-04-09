#Numero de variables
nV = 4

INF = 999

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

def printSolution(dist): 
    print("-------------------------")
    for i in range(nV): 
        for j in range(nV): 
            if(dist[i][j] == INF): 
                print("INF", end =" ")
            else: 
                print(dist[i][j], end ="  ")  
        print(" ")

# Formato [[]]
graph =     [[0, 8, 3, 7],
            [8, 0, 2, 1],
            [3, 2, 0, INF],
            [0, 8, 3, 0]]

floydWarshall(graph)