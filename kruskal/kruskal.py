#Algoritmo de Kruskal
# Formato de entrada del fichero -->
# A B 3
# B A 4
# C R 5
# ...
from collections import defaultdict 
  
class Graph: 
    def __init__(self,vertices): 
        self.V= vertices
        self.graph = []
          
    def addEdge(self,u,v,w): 
        self.graph.append([u,v,w]) 

    def find(self, parent, i): 
        if parent[i] == i: 
            return i 
        return self.find(parent, parent[i]) 

    def union(self, parent, rank, x, y): 
        xroot = self.find(parent, x) 
        yroot = self.find(parent, y) 

        if rank[xroot] < rank[yroot]: 
            parent[xroot] = yroot 
        elif rank[xroot] > rank[yroot]: 
            parent[yroot] = xroot 

        else : 
            parent[yroot] = xroot 
            rank[xroot] += 1
  
    def KruskalMST(self): 
  
        result = []
  
        i = 0
        e = 0

        self.graph =  sorted(self.graph,key=lambda item: item[2]) 
  
        parent = [] ; rank = [] 

        for node in range(self.V): 
            parent.append(node) 
            rank.append(0)

        while e < self.V -1 : 
            u,v,w =  self.graph[i] 
            i = i + 1
            x = self.find(parent, u) 
            y = self.find(parent ,v) 

            if x != y: 
                e = e + 1     
                result.append([u,v,w]) 
                self.union(parent, rank, x, y)             

        print ("Los vertices construidos son: ")
        for u,v,weight  in result: 
            print ((chr(u+97),chr(v+97),weight))

def lecturaDatos(dir = "datos.txt"):
    lista_nodos = []
    archivo = open(dir, "r")
    aristas = []
    index = 0
    for line in archivo.read().split("\n"):
        aristaA = ord(line.split(" ")[0].lower())-97
        aristaB = ord(line.split(" ")[1].lower())-97
        coste   = int(line.split(" ")[2])
        aristas.append([])

        if aristaA not in lista_nodos:
            lista_nodos.append(aristaA)

        if aristaB not in lista_nodos:
            lista_nodos.append(aristaB)

        if aristaA > aristaB:
            aux = aristaB
            aristaB = aristaA
            aristaA = aux

        aristas[index].append(aristaA)
        aristas[index].append(aristaB)
        aristas[index].append(coste)
        index += 1

    aristas.sort(key = lambda x: x[2])
    return aristas, len(lista_nodos)

datos, nodos = lecturaDatos()

g = Graph(nodos)

for dato in datos:
    g.addEdge(dato[0], dato[1], dato[2])

g.KruskalMST()