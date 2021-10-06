from Arrays import Array

class Array2D_CM:
    def __init__(self, nRows, nCols):
        self._elementos = Array(nRows*nCols)
        self._nRows = nRows
        self._nCols = nCols

    def _computar_indice(self, nxTuple): # [0, 3] -> 6   3*2+0 = ix[1]*nRows + ix[0]
        offset = nxTuple[1]* self._nRows + nxTuple[0]
        return offset

    def __setitem__(self, nxTuple, v):
        ix = self._computar_indice(nxTuple)
        self._elementos[ix] = v

    def __getitem__(self, nxTuple, v):
        ix = self._computar_indice(nxTuple)
        return self._elementos[ix]

#   0   1   2   3   4
# +---+---+---+---+---+ 
# | 0 | 2 | 4 | 6 | 8 |  0
# +---+---+---+---+---+
# | 1 | 3 | 5 | 7 | 9 |  1
# +---+---+---+---+---+

# 0 3 6
# 1 4 7 
# 2 5 8

arr = Array2D_CM(3, 3)

arr[2, 1] = 10

for i, el in enumerate(arr._elementos):
    print(i, el)