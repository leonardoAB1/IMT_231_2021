from Arrays import Array

class MultiArray: # MultiArray(10, 5, 5, 2)
    def __init__(self, *dims):
        assert len(dims) > 1, "El arreglo debe tener 2 o más dimensiones"
        self._dims = dims

        num_elementos = 1
        for d in dims:
            assert d > 0, "Dimensiones deben ser > 0"
            num_elementos *= d
        
        self._elementos = Array(num_elementos)
        self._factores = Array(len(dims))
        self._computar_factores()

    def dims(self):
        return len(self._dims)

    def length(self, dim):
        assert dim >= 1 and dim < len(self._dims), \
            "Componente de dimensión fuera de rango"
        return self._dims[dim-1]

    def clear(self, v):
        self._elementos.clear(v)
    
    def __getitem__(self, nxTuple):
        assert len(nxTuple) == self.dims(), "Número inválido de subíndices"
        index = self._computar_indice(nxTuple)
        assert index is not None, "Subíndice fuera de rango"
        return self._elementos[index]

    def __setitem__(self, nxTuple, v):
        assert len(nxTuple) == self.dims(), "Número inválido de subíndices"
        index = self._computar_indice(nxTuple)
        assert index is not None, "Subíndice fuera de rango"
        self._elementos[index] = v


    def _computar_indice(self, nxTuple):
        offset = 0
        for j in range(len(nxTuple)):
            if nxTuple[j] < 0 or nxTuple[j] >= self._dims[j]:
                return None
            else:
                offset += nxTuple[j] * self._factores[j]
        return offset


    def _computar_factores(self):
        for j in range(self.dims()):
            self._factores[j] = 1
            for k in range(j+1, len(self._dims)):
                self._factores[j] *= self._dims[k]


arr = MultiArray(10, 5, 5, 2)
arr[8, 2, 3, 0] = 100
arr[7, 1, 4, 1] = 200
print(arr[8, 2, 3, 0])