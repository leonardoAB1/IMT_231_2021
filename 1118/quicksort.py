def quickSort(coleccion):
    quickSortRecursivo(coleccion, 0, len(coleccion)-1)

def quickSortRecursivo(coleccion, inicio, fin):
    # caso base
    if inicio >= fin:
        return
    else:
        pivot = coleccion[inicio]

        pos = secuencia_particion(coleccion, inicio, fin)

        quickSortRecursivo(coleccion, inicio, pos - 1)
        quickSortRecursivo(coleccion, pos + 1, fin)

def secuencia_particion(coleccion, inicio, fin):
    pivot = coleccion[inicio]

    izquierda = inicio + 1
    derecha = fin

    while izquierda <= derecha:
        while izquierda < derecha and coleccion[izquierda] < pivot:
            izquierda += 1

        while derecha >= izquierda and coleccion[derecha] >= pivot:
            derecha -= 1

        if izquierda < derecha:
            tmp = coleccion[izquierda]
            coleccion[izquierda] = coleccion[derecha]
            coleccion[derecha] = tmp
    
    if derecha != inicio:
        coleccion[inicio] = coleccion[derecha]
        coleccion[derecha] = pivot
    
    return derecha


lista = [10, 23, 51, 18, 4, 31, 13, 5]

quickSort(lista)