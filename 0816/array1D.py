import ctypes 

# ArrayType = ctypes.py_object * 5
# lista_valores = ArrayType()

# for i in range(5):
#     lista_valores[i] = None

# lista_valores[1] = 12
# lista_valores[2] = 34
# lista_valores[4] = 39

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

# https://docs.python.org/3.9/library/array.html#module-array

# from array import array

# arr = array('u', 'abcd')
# arr2 = array('B', [0,1,2,3,4])
