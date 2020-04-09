#Algoritmo de Kruskal

def lecturaDatos(dir = "datos.txt"):
    archivo = open(dir, "r")
    aristas = []
    index = 0
    for line in archivo.read().split("\n"):
        aristaA = line.split(" ")[0]
        aristaB = line.split(" ")[1]
        coste   = line.split(" ")[2]
        aristas.append([])
        aristas[index].append(aristaA)
        aristas[index].append(aristaB)
        aristas[index].append(coste)
        index += 1
    aristas.sort()
    return aristas

datos = lecturaDatos()
print(datos)