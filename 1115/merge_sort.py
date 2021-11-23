from Arrays import Array

def unirSubgruposOrdenados(coleccion, izquierda, derecha, fin, array_tmp):
    a = izquierda
    b = derecha

    m = 0

    while a < derecha and b < fin:
        if coleccion[a] < coleccion[b]:
            array_tmp[m] = coleccion[a]
            a += 1
        else:
            array_tmp[m] = coleccion[b]
            b += 1
        m += 1

    while a < derecha:
        array_tmp[m] = coleccion[a]
        a += 1
        m += 1

    while b < fin:
        array_tmp[m] = coleccion[b]
        b += 1
        m += 1

    for i in range(fin - izquierda):
        coleccion[izquierda + i] = array_tmp[i]
#                         n             m
def mergeSortRecursivo(coleccion, inicio, fin, array_tmp): # O(n log n)
    # caso base
    if inicio == fin:
        return # O(1)

    # caso recursivo
    else:
        medio = (inicio + fin) // 2 # O(1)

        mergeSortRecursivo(coleccion, inicio, medio, array_tmp) # O(log n)
        mergeSortRecursivo(coleccion, medio + 1, fin, array_tmp)

        unirSubgruposOrdenados(coleccion, inicio, medio + 1, fin + 1, array_tmp) # O(n)

def mergeSort(coleccion):
    array_ordenado = Array(len(coleccion))
    mergeSortRecursivo(coleccion, 0, len(coleccion) - 1, array_ordenado)
    return array_ordenado



lista = [10, 23, 51, 18, 4, 31, 13, 5]

lista_ordenada = mergeSort(lista)

for i in lista_ordenada:
    print(i)