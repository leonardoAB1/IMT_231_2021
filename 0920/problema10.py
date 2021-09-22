"""
Problema 10
Modifique el algoritmo de búsqueda binaria implementado en clase 
para encontrar la primera ocurrencia de un valor 
que puede estar múltiples veces en una lista ordenada. 
Asegúrese que su solución sigue siendo O(log n).
"""

def binarySearch(collection, target):
    """
    >>> A=[9,9,9,9,9,9]
    >>> binarySearch(A, 9) 
    0
    >>> test0=[9,9,9,9,9,9] 
    >>> binarySearch(test0, 9) 
    0
    >>> test1=[5,9,9,9,9,9,9]  
    >>> binarySearch(test1, 9) 
    1
    >>> test2=[5,6,7,9,9,9,9]  
    >>> binarySearch(test2, 9) 
    3
    >>> binarySearch(test2, 6) 
    1
    >>> test3=[0,1,2,3,4,5,5,5,5,6,6,6,7]
    >>> binarySearch(test3, 6) 
    9
    >>> binarySearch(test3, 10) 
    -1
    """
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

if __name__=="__main__":
    import doctest
    doctest.testmod(verbose=True)