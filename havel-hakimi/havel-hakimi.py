# Algoritmo que realiza havel hakimi

SEQUENCIA = [2,3,3,3,4,4,4,7]

def havelHakimi(sequence):
    # Things that may immediatly disqualify a sequence:
    # 1) non-integers
    # 2) negative numbers
    # 3) sum of sequence is not even
    if all(isinstance(deg, int) for deg in sequence):
        s = list(sequence) 
    else:
        return False #list contains non-integer degrees
    #An empty sequence is still graphic
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
            print("Perfecto es una sequencia grafica")
            return True
        if d>len(s):
            print(str(d)+" es muy largo para la sequencia!")
            return False
        for i in range(0,d):
            s[i]-=1
        print("Quitado: "+str(d))
    return False

havelHakimi(SEQUENCIA)