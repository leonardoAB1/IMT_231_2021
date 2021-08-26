from Arrays import Array2D

class Matrix:
    def __init__(self, numRows, numCols):
        self._matriz = Array2D(numRows, numCols)
        self._matriz.clear(0)
        
    def __str__(self):
        string="| "
        for i in range(self.numRows()):
            for j in range(self.numCols()):
                string+=f"{self[i, j]} "
            string+="|\n| "
        return string[:-3]
    
    def numRows(self):
        return self._matriz.numRows()

    def numCols(self):
        return self._matriz.numCols()

    def __getitem__(self, ndIndex):
        return self._matriz[ndIndex[0], ndIndex[1]]

    def __setitem__(self, ndIndex, escalar):
        self._matriz[ndIndex[0], ndIndex[1]] = escalar

    def scaleBy(self, escalar):
        for fila in range(self.numRows()):
            for columna in range(self.numCols()):
                self[fila, columna] *= escalar

    def transpose(self):
        newMatrix=Matrix(self.numCols(), self.numRows())
        for row in range(self.numRows()):
            for column in range(self.numCols()):
                newMatrix[column, row]=self[row,column]
        return newMatrix

    def __add__(self, rhsMatrix):
        assert rhsMatrix.numRows() == self.numRows() and \
            rhsMatrix.numCols() == self.numCols(), \
                "Dimensiones no compatibles para esta operación"
        nuevaMatriz = Matrix(self.numRows(), self.numCols())
        for fila in range(self.numRows()):
            for columna in range(self.numCols()):
                nuevaMatriz[fila, columna] = self[fila, columna] + rhsMatrix[fila, columna]
        return nuevaMatriz


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
        assert self.numCols()==rhsMatrix.numRows(),\
            "Dimensiones no compatibles para esta operación"
        newMatrix=Matrix(self.numRows(), rhsMatrix.numCols())
        for l in range(rhsMatrix.numCols()):
            for i in range(self.numRows()):
                suma=0
                for j in range(self.numCols()):
                    suma+=self[i,j]*rhsMatrix[j,l]
                newMatrix[i,l]=suma
        return newMatrix   