from array import Array

class Array2D:
    def __init__(self, nRows, nCols):
        self._filas = Array(nRows)
        
        for i in range(nCols):
            self._filas[i] = Array(nCols)

    def numRows(self):
        pass

    def numCols(self):
        pass

    def clear(self, v):
        pass

    def __getitem__(self, ndIndex): # ndIndex[0] = i1, ndIndex[1] = i2
        pass

    def __setitem__(self, ndIndex, v):
        pass
