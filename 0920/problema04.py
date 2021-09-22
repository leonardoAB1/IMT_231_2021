"""
Problema 4
Si bien Python provee el tipo list para construir y manejar secuencias mutables, 
muchos lenguajes no tienen una estructura similar, 
al menos no como parte del lenguaje. 
Implemente la estructura de datos Vector usando la clase Array implementada en clase. 
Su implementación debe producir una secuencia mutable que funcione como una lista de Python. 
Cuando el array interno necesite ser expandido, el nuevo arreglo debe duplicar el tamaño del original. 
Las operaciones que pueden ser realizadas en este ADT están descritas a continuación. 
Asuma que el array interno nunca disminuye de tamaño.
"""
import ctypes

class Array:
    def __init__(self, n):
        assert n > 0
        self._n = n
        PyArrayType = ctypes.py_object * n
        self._elements = PyArrayType()
        self.clear(None)

    def __len__(self):
        return self._n

    def __getitem__(self, i):
        assert i >= 0 and i < len(self), "Index out of range"
        return self._elements[i]

    def __setitem__(self, i, v):
        assert i >= 0 and i < len(self)
        self._elements[i] = v

    def clear(self, v):
        for i in range(len(self)):
            self._elements[i] = v

    def __iter__(self):
        return _ArrayIterator(self._elements)


class _ArrayIterator:
    def __init__(self, arreglo):
        self._arregloRef = arreglo
        self._iActual = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._iActual < len(self._arregloRef):
            element = self._arregloRef[self._iActual]
            self._iActual += 1
            return element
        else:
            raise StopIteration


class Vector():
    """
    >>> A=Vector()
    >>> print(f"{A}, elements:{A._elements}, capacity:{A._capacity}")
    [None,None], elements:0, capacity:2
    >>> A.append(0)
    >>> A.append(44)
    >>> A.append(3)
    >>> A.append(4)
    >>> print(f"{A}, elements:{A._elements}, capacity:{A._capacity}")
    [0,44,3,4], elements:4, capacity:4
    >>> A.insert(2, 8)
    >>> print(f"{A}, elements:{A._elements}, capacity:{A._capacity}")
    [0,44,8,3,4,None,None,None], elements:5, capacity:8
    >>> A.append(7)
    >>> A.append(101)
    >>> print(f"{A.remove(0)} removed")
    0 removed
    >>> print(f"{A}, elements:{A._elements}, capacity:{A._capacity}")
    [44,8,3,4,7,101,None,None], elements:6, capacity:8
    >>> print(f"{A}; Where is 3?:Index number {A.indexOf(3)}")
    [44,8,3,4,7,101,None,None]; Where is 3?:Index number 2
    >>> print(f"{A}; Does vector contains 5?:{A.contains(5)}")
    [44,8,3,4,7,101,None,None]; Does vector contains 5?:False
    >>> print(f"{A.remove(0)} removed")
    44 removed
    >>> print(f"{A}, elements:{A._elements}, capacity:{A._capacity}")
    [8,3,4,7,101,None,None,None], elements:5, capacity:8
    >>> B=Vector()
    >>> B.append(5)
    >>> B.append(6)
    >>> B.append(7)
    >>> B.append(8)
    >>> A.extend(B)
    >>> A.remove(0)
    8
    >>> A.remove(0)
    3
    >>> print(f"{A}, elements:{A._elements}, capacity:{A._capacity}")
    [4,7,101,5,6,7,8,None,None,None,None,None,None,None,None,None], elements:7, capacity:16
    >>> C=A.subVector(2,5)
    >>> print(f"C={C}, elements:{C._elements}, capacity:{C._capacity}")
    C=[101,5,6,7], elements:4, capacity:4
    """
    def __init__(self):
        "Crea un nuevo vector vacío con una capacidad inicial de dos elementos"
        
        self._arr = Array(2)
        self._capacity = 2
        self._elements = 0

    def __str__(self):
        string="["
        for i in self._arr:
            string+=f"{i},"
        return string[:-1]+"]"
    
    def length(self):
        "Retorna el número de elementos contenidos en el vector."
        return self._elements

    def contains(self, item):
        "Determina si el argumento dado está contenido en el vector."
        n = self.length()
        for i in range(n):
            if self._arr[i] == item:
                return True
        return False

    def getitem(self, index):
        """
        Retorna el valor almacenado en el elemento especificado por index.
        index debe estar dentro del rango válido."""
        assert index<self._elements, "Index out of range"
        return self._arr[index]

    def setitem(self, index, item):
        """Modifica el valor almacenado en el elemento especificado por
        index para almacenar item. index debe estar dentro del rango 
        válido, el cual incluye la primera posición después del último 
        elemento."""
        assert index<=self._elements+1, "Index out of range"
        self._arr[index]=item
        
    def _realloc(self, newCapacity):
        "Redimensiona el array interno"
        
        newArray=Array(newCapacity)
        # copy old _arr into the new one
        
        for i in range(self._elements):
            newArray[i]=self._arr[i]
            
        self._capacity= newCapacity
        self._arr = newArray
        
    def append(self, item):
        "Agrega el item dado al final de la lista"
        if self._elements >= self._capacity:
            self._realloc(2*self._capacity)
            
        self._arr[self._elements]=item
        self._elements+=1

    def insert(self, index, item):
        """Inserta el item dado en la posición especificada por index. 
        Los elementos en la posición de index y siguientes deben ser 
        desplazados para hacer espacio para el nuevo elemento. 
        index debe estar dentro del rango válido"""
        assert index<self._elements+1, "Index out of range"
        if self._elements!=self._capacity:
            i=self._elements
            while i>=index:
                self._arr[i+1]=self._arr[i]
                i-=1
            self._arr[index]=item
            self._elements+=1
        else:
            self._realloc(2*self._capacity)
            self.insert(index, item)
            

    def remove(self, index):
        """Remueve y retorna el item en la posición dada por index. 
        Los elementos en la posición de index y siguientes deben ser 
        desplazados para ocupar el vacío creado por el item removido. 
        index debe estar dentro del rango válido"""
        assert index<self._elements, "Index out of range"
        for i in range(index, self._elements):
            if i==index:
                item=self._arr[i]
            self._arr[i]=self._arr[i+1]
            
        self._elements-=1
        return item

    def indexOf(self, item):
        """Retorna el índice del elemento que contenga item. 
        item debe estar en la lista"""
        assert self.contains(item), "Item not in vector."
        n = self.length()
        position=0
        while position<=n:
            if self._arr[position] == item:
                return position
            position+=1

    def extend(self, otroVector):
        "Extiende este vector agregando todos los elementos de otroVector"
        for i in otroVector:
            self.append(i)

    def subVector(self, inicio, fin):
        """Crea y retorna un nuevo vector que contiene una subsecuencia 
        de elementos en el vector entre las posiciones inicio y fin, 
        incluyendo esos elementos. inicio y fin deben estar dentro 
        del rango válido"""
        assert inicio<self._elements and fin<self._elements, "Index out of range"
        newVector=Vector()
        for i in range(inicio, fin+1):
            newVector.append(self._arr[i])
        return newVector

    def __iter__(self):
        """Crea y retorna un iterador que puede ser usado para 
        iterar sobre los elementos del vector"""
        return self._arr.__iter__()
    

if __name__=="__main__":
    import doctest
    doctest.testmod(verbose=True)