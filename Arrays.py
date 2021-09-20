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
        assert i >= 0 and i < len(self)
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
            elemento = self._arregloRef[self._iActual]
            self._iActual += 1
            return elemento
        else:
            raise StopIteration

class Array2D:
    def __init__(self, nRows, nCols):
        self._filas = Array(nRows)
        
        for i in range(nRows):
            self._filas[i] = Array(nCols)

    def numRows(self):
        return len(self._filas)

    def numCols(self):
        return len(self._filas[0])

    def clear(self, v):
        for fila in self._filas:
            fila.clear(v)

    def __getitem__(self, ndIndex): # ndIndex[0] = i1, ndIndex[1] = i2
        assert len(ndIndex) == 2, "Número inválido de subindíces"
        fila = ndIndex[0]
        columna = ndIndex[1]
        assert fila >= 0 and fila < self.numRows() \
            and columna >= 0 and columna < self.numCols(), \
                "Subíndices fuera  de rango"
        array_interno = self._filas[fila]
        return array_interno[columna]

    def __setitem__(self, ndIndex, v):
        assert len(ndIndex) == 2, "Número inválido de subindíces"
        fila = ndIndex[0]
        columna = ndIndex[1]
        assert fila >= 0 and fila < self.numRows() \
            and columna >= 0 and columna < self.numCols(), \
                "Subíndices fuera  de rango"
        array_interno = self._filas[fila]
        array_interno[columna] = v
