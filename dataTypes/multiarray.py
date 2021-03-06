from Arrays import Array
class MultiArray:
    def __init__(self, *dims):
        assert len(dims) > 1, "El arreglo debe tener 2 o más dimensiones"
        self._dims = dims
                
        num_elements=1
        for d in dims:
            assert d>0, "Dimensiones deben ser > 0"
            num_elements *= d
            
        self._elements = Array(num_elements)
        self._factors = Array(len(dims))
        self._compute_factors()
        
    def dims(self):
        return len(self._dims)
    
    def length(self, dim):
        assert dim >=1 and dim < len(self.dims), \
            "Componente de dimensión fuera de rango"
        return self._dims[dim-1]
    
    def clear(self, v):
        self._elements.clear(v)
        
    def __getitem__(self, nxTuple):
        assert len(nxTuple) == len(self.dims()), "Numero inválido de subindices"
        index = self._compute_index(nxTuple)
        assert index is not None, "Subindice fuera de rango"
        return self._elements[index]
    
    def __setitem__(self, nxTuple, v):
        assert len(nxTuple) == len(self.dims()), "Numero inválido de subindices"
        index = self._compute_index(nxTuple)
        assert index is not None, "Subindice fuera de rango"
        self._elements[index] = v
    
    def _compute_index(self, nxTuple):
        offset=0
        for j in range(len(nxTuple)):
            if nxTuple[j] < 0 or nxTuple[j] >=self._dims[j]:
                return None
            else:
                offset += nxTuple[j] *self._factors[j]
        return offset
    
    def _compute_factors(self):
        for j in range(len(self._dims)):
            self._factors[j]=1
            for k in range(j+1, len(self._dims)):
                self._factors[j] *= self._dims[k]
                
                
if __name__=="__main__":
    arr=MultiArray(10, 5, 5, 2)
    arr[8, 2, 3, 0]= 100
    arr[7, 1, 4, 1]= 200
    print(arr[8, 2, 3, 0])