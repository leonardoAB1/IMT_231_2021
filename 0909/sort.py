def bubbleSort(coleccion):
    n = len(coleccion)
    for i in range(n - 1): # O(n^2)
        for j in range(n - i - 1):
            if coleccion[j] > coleccion[j + 1]:
                # tmp = coleccion[j + 1]
                # coleccion[j + 1] = coleccion[j]
                # coleccion[j] = tmp
                coleccion[j], coleccion[j+1] = coleccion[j+1], coleccion[j]

def selectionSort(coleccion): # O(n^2)
    n = len(coleccion)
    for i in range(n - 1): # n - 1
        min_index = i
        for j in range(i + 1, n): # n - 1
            if coleccion[j] < coleccion[min_index]:
                min_index = j
        
        if min_index != i:
            # tmp = coleccion[min_index]
            # coleccion[min_index] = coleccion[i]
            # coleccion[i] = tmp
            coleccion[min_index], coleccion[i] = coleccion[i], coleccion[min_index]

def insertionSort(coleccion): # O(n^2)
    n = len(coleccion)
    for i in range(1, n): # n - 1 
        valor = coleccion[i]
        pos = i

        while pos > 0 and valor < coleccion[pos - 1]: # n -1 
            coleccion[pos] = coleccion[pos - 1]
            pos -= 1

        coleccion[pos] = valor

lista = [10, 51, 29, 18, 4, 31, 13, 5, 23, 64, 2]

print(lista)

insertionSort(lista)

print(lista)




