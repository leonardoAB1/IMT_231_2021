from Arrays import Array2D

class Matrix:
    def __init__(self, numRows, numCols):
        self._matriz = Array2D(numRows, numCols)
        self._matriz.clear(0)

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
        pass

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
        pass

    def __mul__(self, rhsMatrix):
        pass