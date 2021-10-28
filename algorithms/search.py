"Aislar elementos de una colección que coincidan con un criterio de búsqueda."
def linearSearch(collection, objective):
    n = len(collection)
    for i in range(n):
        if collection[i] == objective:
            return True
    return False

# El peor caso es cuando ocurre el mayor numero de iteraciones
# En una lista ordenada, hay dos criterios de busqueda que llevan al peor caso: Pedir el numero mas grandde, pedir un numero fuera del set
# Asumiendo lista ordenada

def sortedLinearSeach(collection, objective):
    n = len(collection)
    for i in range(n):                              # O(n) lineal
        if collection[i] == objective:
            return True
        elif collection[i] > objective:
            return False
    return False

# O(findSmallest)=1 := Constante si colección ordenada, en este caso --> O(n)


def findSmallest(collection):
    n = len(collection)
    minimum = collection[0]
    for i in range(n):
        if collection[i] < minimum:
            minimum = collection[i]
    return minimum

# O(binarySearch)=log n


def binarySearch(collection, objective):
    inferior = 0
    superior = len(collection)-1

    while inferior <= superior:                     #O(log n)
        medio = (inferior + superior)//2            #O(1)
        if collection[medio] == objective:          
            return True                             #O(1)
        elif objective < collection[medio]:
            superior = medio-1                      #O(1)
        else:
            inferior = medio+1                      #O(1)
    return False

#Binary Search Recursive
def recBinarySearch(objetivo, secuencia, inferior, superior):
    if inferior>superior:   #caso base
        return False
    else:
        medio=(inferior+superior)//2
        if secuencia[medio]==objetivo:
            return True     #caso base 2
        elif objetivo<secuencia[medio]: #caso recursivo 1
            return recBinatySearch(objetivo, secuencia, inferior, medio-1)
        elif objetivo>secuencia[medio]: #caso recursivo 2
            return recBinarySearch(objetivo, secuencia, medio+1, superior)