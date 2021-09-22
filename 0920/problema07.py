"""
Problema 7
Modifique el tipo de dato Array2D de modo que 
el array interno unidimensional almacene los valores 
dando preferencia a las columnas en lugar de filas.
"""
import ctypes 

class Array:
    def __init__(self, n):
        assert n > 0
        self._n = n
        PyArrayType = ctypes.py_object * n
        self._elementos = PyArrayType()
        self.clear(None)

    def __len__(self):
        return self._n

    def __getitem__(self, i):
        assert i >= 0 and i < len(self), "Index out of range"
        return self._elementos[i]

    def __setitem__(self, i, v):
        assert i >= 0 and i < len(self)
        self._elementos[i] = v

    def clear(self, v):
        for i in range(len(self)):
            self._elementos[i] = v

    def __iter__(self):
        return _ArrayIterator(self._elementos)

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
        

class Array2D:
    """
    >>> Z=Array2D(3,2)
    >>> Z[0,0]=1
    >>> Z[1,0]=2
    >>> Z[2,0]=3
    >>> Z[0,1]=4
    >>> Z[1,1]=5
    >>> Z[2,1]=6
    >>> Z
    |1 2 3 4 5 6|
    >>> print(Z) 
    | 1 4 |
    | 2 5 |
    | 3 6 |
    >>> Z[1,0]
    2
    >>> Z[1,1]=8
    >>> Z
    |1 2 3 4 8 6|
    >>> print(Z) 
    | 1 4 |
    | 2 8 |
    | 3 6 |
    """
    def __init__(self, nRows, nCols):
        self._nCols=nCols
        self._nRows=nRows
        self._elementos = Array(nCols*nRows)
    
    def numCols(self):
        return self._nCols

    def numRows(self):
        return self._nRows
    
    def clear(self, v):
        self._elementos.clear(v)

    def __getitem__(self, ndIndex): # ndIndex[0] = i1, ndIndex[1] = i2
        assert len(ndIndex) == 2, "Número inválido de subindíces"
        index = self._compute_index(ndIndex)
        assert index is not None, "Subíndice fuera de rango"
        return self._elementos[index]

    def __setitem__(self, ndIndex, v):
        assert len(ndIndex) == 2, "Número inválido de subindíces"
        index = self._compute_index(ndIndex)
        assert index is not None, "Subíndice fuera de rango"
        self._elementos[index] = v
                
    def __str__(self):
        string="| "
        for i in range(self.numRows()):
            for j in range(self.numCols()):
                string+=f"{self[i, j]} "
            string+="|\n| "
        return string[:-3]
    
    def __repr__(self) -> str:
        string="|"
        for i in range(len(self._elementos)):
            string+=f"{self._elementos[i]} "
        return string[:-1]+"|"
            
    def __len__(self):
        return len(self._elementos)
    
    def _compute_index(self, nxIndex):
        assert nxIndex[0]<self.numRows() and nxIndex[1]<self.numCols(), "Index out of range"
        index = (nxIndex[1]*self.numRows())+nxIndex[0]
        return index
            

if __name__=="__main__":
    import doctest
    doctest.testmod(verbose=True)
    #1  2  3  4  5  6
    #00 10 20 01 11 22