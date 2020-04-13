import networkx as nx
import matplotlib.pyplot as ptl
import itertools

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

def is_all(l):
    cogido = []
    for x in l:
        if x[0] not in cogido:
            cogido.append(x[0])
        if x[1] not in cogido:
            cogido.append(x[1])
    return len(cogido)

def get_degrees(g):
    return [d for n, d in g.degree()]

def all_sub_graph(g):
    l = []
    r_edges = []
    for x in list(itertools.combinations(g.edges.data(data=True), len(g.nodes)-1)):
        new = nx.Graph()
        new.add_nodes_from(g.nodes)
        edges = []
        for e in x:
            edges.append([e[0], e[1], e[2]["weight"]])
        edges = sorted(edges, key=lambda t: t[2])
        edges = sorted(edges, key=lambda t: t[1])
        edges = sorted(edges, key=lambda t: t[0])
        s_edges = str(edges[0])+str(edges[1])+str(edges[2])
        if s_edges not in r_edges:
            r_edges.append(s_edges)
            for z in edges:
                new.add_edge(z[0], z[1], weight=z[2])
            l.append(new)
    return set(l)

def get_all_spanning_trees(g):
    l = []
    for x in all_sub_graph(g):
        if nx.algorithms.is_tree(x) == True and (is_all(x.edges) == len(g.nodes)):
            l.append(x)
    return l

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

for x in get_all_spanning_trees(G):
    print_graph(x)

print("Arbol generador minimo es: ")
print_graph(nx.algorithms.minimum_spanning_tree(G))
print("Arbol generador maximo es: ")
print_graph(nx.algorithms.maximum_spanning_tree(G))