def linearSearch(valores, objetivo):
    n = len(valores)
    for i in range(n): # O(n) lineal
        if valores[i] == objetivo:
            return True
    return False

def sortedLinearSearch(valores, objetivo):
    n = len(valores)
    for i in range(n): # O(n) lineal
        if valores[i] == objetivo:
            return True
        elif valores[i] > objetivo:
            return False
    return False

def findSmallest(valores):
    n = len(valores)
    minimo = valores[0]
    for i in range(n):
        if valores[i] < minimo:
            minimo = valores[i]
    return minimo

def binarySearch(valores, objetivo):
    inferior = 0
    superior = len(valores) - 1

    while inferior <= superior: # O(log n)
        medio = (inferior + superior) // 2 # O(1)
        if valores[medio] == objetivo:
            return True # O(1)
        elif objetivo < valores[medio]:
            superior = medio - 1 # O(1)
        else:
            inferior = medio + 1 # O(1)
    
    return False