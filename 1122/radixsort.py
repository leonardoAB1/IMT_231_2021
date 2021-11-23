from Arrays import Array
from QueueLinked import Queue

def radixSort(coleccion, numero_digitos): # O(k + mn)
    canastas = Array(10)
    for k in range(10): # O(k)
        canastas[k] =  Queue()

    columna = 1

    for d in range(numero_digitos): # O(m)
        for elemento in coleccion: # O(n)
            digito = (elemento // columna) % 10
            canastas[digito].enqueue(elemento)

        i = 0
        for canasta in canastas: # O(1) -> O(n)
            while not canasta.isEmpty(): # O(n)
                coleccion[i] = canasta.dequeue()
                i += 1

        columna *= 10

lista = [10, 23, 51, 18, 4, 31, 13, 5, 48, 62, 29, 8, 37]
print(lista)
radixSort(lista, 2)
print(lista)