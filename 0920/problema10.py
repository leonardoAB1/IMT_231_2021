"""
Problema 10
Modifique el algoritmo de búsqueda binaria implementado en clase 
para encontrar la primera ocurrencia de un valor 
que puede estar múltiples veces en una lista ordenada. 
Asegúrese que su solución sigue siendo O(log n).
"""

def binarySearch(collection, target):
    inferior, superior = 0, len(collection)-1
    result=-1                                       #Equivale a elemento no encontrado

    while inferior <= superior:                     #O(log n)
        mid = (inferior + superior)//2              #O(1)
        if collection[mid] == target:  
            result=mid                              #O(1)
            superior= mid-1                         #O(1) continuar buscando a la izquierda
        elif target < collection[mid]:
            superior = mid-1                        #O(1)
        else:
            inferior = mid+1                        #O(1)
            
    return result
