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

#https://docs.python.org/3.9/library/array.html#module-array 
  
#from array import array

#arr=array("u", "abcd")
#arr2=array("u", [0,1,2,3,4])

class Array2D:
    def __init__(self, nRows, nCols):
        self._rows = Array(nRows)
        
        for i in range(nRows):
            self._rows[i] = Array(nCols)

    def numRows(self):
        return len(self._rows)

    def numCols(self):
        return len(self._rows[0])

    def clear(self, v):
        for row in self._rows:
            row.clear(v)

    def __getitem__(self, ndIndex): # ndIndex[0] = i1, ndIndex[1] = i2
        assert len(ndIndex) == 2, "Número inválido de subindíces"
        row = ndIndex[0]
        column = ndIndex[1]
        assert row >= 0 and row < self.numRows() \
            and column >= 0 and column < self.numCols(), \
                "Subíndices fuera  de rango"
        return self._rows[row][column]

    def __setitem__(self, ndIndex, v):
        assert len(ndIndex) == 2, "Número inválido de subindíces"
        row = ndIndex[0]
        column = ndIndex[1]
        assert row >= 0 and row < self.numRows() \
            and column >= 0 and column < self.numCols(), \
                "Subíndices fuera  de rango"
        array_interno = self._rows[row]
        array_interno[column] = v
