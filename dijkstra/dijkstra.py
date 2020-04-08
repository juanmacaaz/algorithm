# Este codigo es util para realizar el algoritmo de Dijksta

data = open("datos.txt", "r")
data_lines = data.readlines()

list_vars = list(range(0, int(data_lines[0])))
inicio  = data_lines[1].split(",")[0].lower()
final   = data_lines[1].split(",")[1][0].lower()

datos = []

for x in range(2, len(list_vars)+2):
    line = data_lines[x]
    nums = line.split(",")
    sub_nums = []
    for y in nums:
        sub_nums.append(int(y))
    datos.append(sub_nums)

def nuevo_valores(lista_matrix, linea_valores, valor_suma, valores_cogidos, recorrido, siguiente_valor):
    for x in range(0, len(lista_matrix)):
        if lista_matrix[x] != -1 and x not in valores_cogidos:
            if lista_matrix[x]+valor_suma < linea_valores[x] or linea_valores[x] == -1:
                linea_valores[x] = lista_matrix[x]+valor_suma
                recorrido[x] = siguiente_valor


def coger_valor_minimo(lista, valores_cogidos):
    valor_minimo = 9999999999
    indice = 0
    pos_minimo = 0
    for x in lista:
        if indice not in valores_cogidos and x != -1:
            if valor_minimo > x:
                valor_minimo = x
                pos_minimo = indice
        indice+=1
    return valor_minimo, pos_minimo

def muestra_paso(letra ,linea_valore, recorrido):
    print(chr(letra+97), end=" -- ")
    for x in linea_valore:
        print(str(x), end=" ")
    print()

def init(list_vars, datos):
    index = 0
    matrix = dict()
    for var in list_vars:
        matrix[var] = datos[index]
        index += 1
    return matrix

def mostrar_solucion(matrix, inicial, final):
    valores_cogidos = []
    linea_valores = []
    siguiente_valor = inicial
    valor_anterior_suma = 0
    recorrido = []
    recorrido_final = []
    for x in range(0, len(matrix[siguiente_valor])):
        recorrido.append(inicial)

    valores_cogidos.append(inicial)
    linea_valores = matrix[siguiente_valor]

    for x in range(0, len(matrix)):
        recorrido_final.append(recorrido[siguiente_valor])
        muestra_paso(siguiente_valor,linea_valores,recorrido)
        valor_anterior_suma, siguiente_valor = coger_valor_minimo(linea_valores, valores_cogidos)
        valores_cogidos.append(siguiente_valor)
        nuevo_valores(matrix[siguiente_valor], linea_valores, valor_anterior_suma, valores_cogidos, recorrido, siguiente_valor)
        if siguiente_valor == final:
            print("El peso es de: ", linea_valores[final])
    recorrido_final.append(recorrido[siguiente_valor])
    recorrido_final.append(final)
    
    print("El recorrido es: ", end="")

    for x in valores_cogidos:
        if x in recorrido_final:
            print(chr(x+97), end=" ")

matrix = init(list_vars, datos)

print("La solucion de la tabla es:")
mostrar_solucion(matrix, ord(inicio)-97, ord(final)-97)