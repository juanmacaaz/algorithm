# Este codigo es util para realizar el algoritmo de Dijksta



list_vars = [0,1,2,3,4,5,6,7,8,9]

datos = [
    [0,-1,-1,12,-1,-1,-1,-1,-1,-1],
    [7,0,-1,-1,17,-1,-1,2,16,-1],
    [13,4,0,-1,11,-1,7,3,-1,6],
    [-1,18,14,0,-1,10,3,-1,15,-1],
    [-1,5,-1,-1,0,-1,16,6,-1,-1],
    [14,-1,19,-1,16,0,-1,-1,11,-1],
    [-1,-1,-1,10,-1,-1,0,-1,3,12],
    [-1,-1,-1,3,-1,-1,-1,0,-1,-1],
    [-1,-1,-1,-1,-1,-1,14,-1,0,2],
    [-1,-1,4,-1,-1,16,-1,-1,10,0]
]

def nuevo_valores(lista_matrix, linea_valores, valor_suma, valores_cogidos):
    for x in range(0, len(lista_matrix)):
        if lista_matrix[x] != -1 and x not in valores_cogidos:
            if lista_matrix[x]+valor_suma < linea_valores[x] or linea_valores[x] == -1:
                linea_valores[x] = lista_matrix[x]+valor_suma


def coger_valor_minimo(lista, valores_cogidos):
    valor_minimo = 999999999
    indice = 0
    pos_minimo = 0
    for x in lista:
        if indice not in valores_cogidos and x != -1:
            if valor_minimo > x:
                valor_minimo = x
                pos_minimo = indice
        indice+=1
    return valor_minimo, pos_minimo

def muestra_paso(letra ,linea_valore):
    print(chr(letra+97), end=" -- ")
    for x in linea_valore:
        print(x, end=" ")
    print()

def init(list_vars, datos):
    index = 0
    matrix = dict()
    for var in list_vars:
        matrix[var] = datos[index]
        index += 1
    return matrix

def mostrar_solucion(matrix, inicial):
    valores_cogidos = []
    linea_valores = []
    siguiente_valor = inicial
    valor_anterior_suma = 0

    valores_cogidos.append(inicial)
    linea_valores = matrix[siguiente_valor]

    for x in range(0, len(matrix)):
        muestra_paso(siguiente_valor,linea_valores)
        valor_anterior_suma, siguiente_valor = coger_valor_minimo(linea_valores, valores_cogidos)
        valores_cogidos.append(siguiente_valor)
        nuevo_valores(matrix[siguiente_valor], linea_valores, valor_anterior_suma, valores_cogidos)
    
    for x in valores_cogidos:
        print(chr(x+97), end=" ")

matrix = init(list_vars, datos)

print("La solucion de la tabla es:")
mostrar_solucion(matrix, ord('h')-97)