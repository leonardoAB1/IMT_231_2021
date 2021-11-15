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

def mergeSort(coleccion, inicio, fin, array_tmp):
    # caso base
    if inicio == fin:
        return

    # caso recursivo
    else:
        medio = (inicio + fin) // 2

        mergeSort(coleccion, inicio, medio, array_tmp)
        mergeSort(coleccion, medio + 1, fin, array_tmp)

        unirSubgruposOrdenados(coleccion, inicio, medio + 1, fin + 1, array_tmp)

from Arrays import Array

lista = [10, 23, 51, 18, 4, 31, 13, 5]
array_ordenado = Array(len(lista))

mergeSort(lista, 0, len(lista) - 1, array_ordenado)