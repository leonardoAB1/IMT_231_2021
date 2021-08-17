from array_ import Array

class Array2D:
    def __init__(self, nRows, nCols):
        self._rows=Array(nRows)
        
        for i in range(nCols-1):
            self._rows[i]= Array(nCols)
    
    def numRows(self):
        return len(self._rows) 
    
    def numCols(self):
        return len(self._rows[0])
    
    def clear(self, v:int):
        for row in self._rows: 
            row.clear()
    
    def __getitem__(self, ndIndex: tuple):
        return self._rows[ndIndex[0]][ndIndex[1]]
    
    def __setitem__(self, ndIndex: tuple, v: int):
        self._rows[ndIndex[0]][ndIndex[1]]=v
        