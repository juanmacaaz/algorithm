import networkx as nx
import matplotlib.pyplot as ptl
import itertools

def _expand(G, explored_nodes, explored_edges):
    frontier_nodes = list()
    frontier_edges = list()
    for v in explored_nodes:
        for u in nx.neighbors(G,v):
            if not (u in explored_nodes):
                frontier_nodes.append(u)
                frontier_edges.append([(u,v), (v,u)])
    return zip([explored_nodes | frozenset([v]) for v in frontier_nodes], [explored_edges | frozenset(e) for e in frontier_edges])

def find_all_spanning_trees(G, root=0):
    explored_nodes = frozenset([root])
    explored_edges = frozenset([])
    solutions = [(explored_nodes, explored_edges)]
    for ii in range(G.number_of_nodes()-1):
        solutions = [_expand(G, nodes, edges) for (nodes, edges) in solutions]
        solutions = set([item for sublist in solutions for item in sublist])
    return [nx.from_edgelist(edges) for (nodes, edges) in solutions]

def print_graph(l):
    print("---------------------------------------------------------")
    print("El grafo tiene los nodos: ")
    for x in l.nodes:
        print(x, end= ' ')
    print()
    print("El grafo tienes las aristas: ")
    for x in l.edges:
        print(x, end= ' ')
    print()
    print("El peso es de: ", l.size(weight="weight"))
    print("---------------------------------------------------------")
    

G = nx.Graph()

archivo = open("datos.txt", "r")

lineas = archivo.readlines()

lista_nodos = []

for linea in lineas:
    a = linea.split(" ")[0].upper()
    b = linea.split(" ")[1].upper()
    if a not in lista_nodos:
        lista_nodos.append(a)
    if b not in lista_nodos:
        lista_nodos.append(b)

for x in lista_nodos:
    G.add_node(x)

for linea in lineas:
    a = linea.split(" ")[0].upper()
    b = linea.split(" ")[1].upper()
    w = int(linea.split(" ")[2])
    G.add_edge(a, b, weight=w)

print_graph(G)

print("Arbol generador minimo es: ")
print_graph(nx.algorithms.minimum_spanning_tree(G))
print("Arbol generador maximo es: ")
print_graph(nx.algorithms.maximum_spanning_tree(G))

# Ahora que marcar el source
print("El arbol con el algorimo BFS es: ")
print_graph(nx.algorithms.bfs_tree(G, "A"))
print("El arbol con el algorimo DFS es: ")
print_graph(nx.algorithms.dfs_tree(G, "F"))