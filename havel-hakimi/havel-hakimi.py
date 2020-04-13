# Algoritmo que realiza havel hakimi

SEQUENCIA = [6, 5, 4, 3, 2, 2, 2, 2]

def havelHakimi(sequence):
    if all(isinstance(deg, int) for deg in sequence):
        s = list(sequence) 
    else:
        return False
    if len(s) == 0:
        print("Secuencia vacia")
        return True 
    if min(s)<0:
        print("Numero negativo detectado!")
        return False
    if sum(s)%2:
        print("La suma de la sequencia es par")
        return False
    while s:
        s.sort()
        s.reverse()
        print("Sequencia: "+str(s))
        if s[0]<0:
            print("Se ha restado a nodos que no existe!")
            return False
        d=s.pop(0)
        if d==0:
            if -1 in s:
                print("No es una sequencia grafica")
                return False
            else:
                print("Perfecto es una sequencia grafica")
                return True
            return True
        if d>len(s):
            print(str(d)+" es muy largo para la sequencia!")
            return False
        for i in range(0,d):
            s[i]-=1
        print("Quitado: "+str(d))
    return False

havelHakimi(SEQUENCIA)

lista = []
for x in range(200):
    if havelHakimi([4,1,x+2,x,x,x,x]):
        lista.append(x)

print(lista)