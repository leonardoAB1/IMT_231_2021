from .Arrays import Array2D

class Matrix:
    def __init__(self, numRows, numCols):
        self._matrix=Array2D(numRows, numCols)
        self._matrix.clear(0)
    
    def __str__(self):
        string="| "
        for i in range(self.numRows()):
            for j in range(self.numCols()):
                string+=f"{self[i, j]} "
            string+="|\n| "
        return string[:-3]
    
    
    def numRows(self):
        return self._matrix.numRows()
    
    def numCols(self):
        return self._matrix.numCols()
    
    def __getitem__(self, ndIndex):
        return self._matrix[ndIndex[0], ndIndex[1]]
    
    def __setitem__(self, ndIndex, scalar):
        self._matrix[ndIndex[0], ndIndex[1]]=scalar
        
    def scaleBy(self, scalar):
        for row in range(self.numRows()):
            for column in range(self.numCols()):
                self[row, column]*=scalar
    
    def transpose(self):
        newMatrix=Matrix(self.numCols, self.numRows)
        for row in range(self.numRows):
            for column in range(self.numCols):
                newMatrix[column][row]=self[row][column]
        return newMatrix
    
    def __add__(self, rhsMatrix):
        assert rhsMatrix.numRows() == self.numRows() and \
            rhsMatrix.numCols() == self.numCols(), \
                "Dimensiones no compatibles para esta operación"
        newMatrix = Matrix(self.numRows(), self.numCols())
        for fila in range(self.numRows()):
            for columna in range(self.numCols()):
                newMatrix[fila, columna] = self[fila, columna] + rhsMatrix[fila, columna]
        return newMatrix
         
    def __sub__(self, rhsMatrix):
        assert rhsMatrix.numRows() == self.numRows() and \
            rhsMatrix.numCols() == self.numCols(), \
                "Dimensiones no compatibles para esta operación"
        newMatrix = Matrix(self.numRows(), self.numCols())
        for fila in range(self.numRows()):
            for columna in range(self.numCols()):
                newMatrix[fila, columna] = self[fila, columna] - rhsMatrix[fila, columna]
        return newMatrix
    
    def __mul__(self, rhsMatrix):
        newMatrix=Matrix(self.numRows, rhsMatrix.numCols)
        for l in range(rhsMatrix.numCols):
            for i in range(self.numRows):
                for j in range(self.numCols):
                    newMatrix[i][l]=sum(self[i][j], self[j][l])
        return newMatrix   