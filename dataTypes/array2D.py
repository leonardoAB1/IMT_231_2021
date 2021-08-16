from array import Array

class Array2D:
    def __init__(self, nRows, nCols):
        self._filas=Array(nRows)
        
        for i in range(nCols):
            self._filas[i]= Array(nCols)
    
    def numRows(self):
        pass
    
    def numCols(self):
        pass
    
    def clear(self, v:int):
        pass
    
    def __getitem__(self, ndIndex: tuple):
        pass
    
    def __setitem__(self, ndIndex: tuple, v: int):
        pass