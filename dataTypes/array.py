import ctypes

ArrayType = ctypes.py_object*5
lista_valores = ArrayType()

for i in range(5):
    lista_valores[i]=None
    
lista_valores[1]=12
lista_valores[2]=34
lista_valores[4]=39

#Implementación más robusta
class Array:
    def __init__(self, n):
        assert n>0
        self._n=n
        PyArrayType=ctypes.py_object*n
        self._elements=PyArrayType()
        self.clear(None)
        
    def __len__(self):
        return self._n
    
    def __getitem__(self, i):
        assert i >= 0 and i < len(self)
        return self._elements[i]
    
    def __setitem__(self, i , v):
        assert i >= 0 and i < len(self)
        self._elements[i]=v
        
    def clear(self, v):
        for i in range(len(self)):
            self._elements[i]=v
        
    def __iter__self(self):
        return _ArrayIterator(self._elements)
    

class _ArrayIterator:
    def __init__(self, array):
        self._arrayRef=array
        self._iActual= 0
        
    def __iter__(self):
        return self
    
    def __next__(self):
        if self._iActual < len(self._arrayRef):
            element=self._arrayRef[self._iActual]
            self._iActual += 1
            return element
        else:
            raise StopIteration
        
#https://docs.python.org/3.9/library/array.html#module-array 
  
from array import array

arr=array("u", "abcd")
arr2=array("u", [0,1,2,3,4])