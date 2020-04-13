# Algoritmo para saber si una sequencia con variables es un arbol

lista = []

for x in range(1, 10000):
    SEQUENCIA = [ x+2,3,x+1,x+1,2,x,x,1,1]
    if sum(SEQUENCIA) == ((2*len(SEQUENCIA))-2):
        lista.append(x)

print("Los valeros de X que cumplen son:", lista)