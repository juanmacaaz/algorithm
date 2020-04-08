# Este codigo es util para realizar el algoritmo de Dijksta

list_vars = [0,1,2,3,4]

datos = [
    [0,6,-1,-1,16],
    [-1,0,-1,-1,-1],
    [18,-1,0,10,3],
    [9,-1,6,0,-1],
    [4,19,9,2,0]
]

def muestra_paso(linea_valore):
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

    for x in range(0, len(matrix)-1):
        linea_valores = matrix[siguiente_valor]
        muestra_paso(linea_valores)

matrix = init(list_vars, datos)

print(matrix)
mostrar_solucion(matrix, 'c')