from Arrays import Array

class SparseMatrix:
    def __init__(self, numRows, numCols):
        self._numCols = numCols
        self._arrayRows = Array(numRows)

    def numCols(self):
        return self._numCols

    def numRows(self):
        return len(self._arrayRows)

    def __setitem__(self, indexTuple, value):
        row, col = indexTuple
        assert col < self._numCols, "Out of bounds"
        pred = None
        currentNode = self._arrayRows[row]
        while currentNode is not None and currentNode.col != col:
            pred = currentNode
            currentNode = currentNode.next

        if currentNode is not None and currentNode.col == col:
            if value == 0.0:
                if currentNode == self._arrayRows[row]:
                    self._arrayRows[row] = currentNode.next
                else:
                    pred.next = currentNode.next

            else:
                currentNode.value = value

        elif value != 0.0:
            newNode = _MatrixElementNode(col, value)
            newNode.next = currentNode
            if currentNode == self._arrayRows[row]:
                self._arrayRows[row] = newNode
            else:
                pred.next = newNode

    def __getitem__(self, indexTuple):
        assert indexTuple[1] < self._numCols, "Out of bounds"
        row, col = indexTuple
        currentNode = self._arrayRows[row]
        while currentNode is not None and currentNode.col != col:
            currentNode = currentNode.next

        if currentNode is not None:
            return currentNode.value
        else:
            return 0
    
    def __iter__(self):
        return _SparseMatrixIterator(self._arrayRows)


    def scaleBy(self, scalar):
        """Escala los valores de la matrix por un escalar"""
        pass

    def transpose(self):
        """Traspone la matrix"""
        pass

    def __add__(self, rhsMatrix):
        """Suma una segunda matriz a la actual"""
        pass

class _SparseMatrixIterator:
    def __init__(self, arrayRows):
        self._arrayRows = arrayRows
        self._rowActual = -1
        self._nodoActual = None
        self._buscarSiguienteElemento()

    def __iter__(self):
        return self

    def __next__(self):
        if self._nodoActual is None:
            raise StopIteration
        else:
            valor = self._nodoActual.value
            self._nodoActual = self._nodoActual.next
            if self._nodoActual is None:
                self._buscarSiguienteElemento()
            return valor
    
    def _buscarSiguienteElemento(self):
        i = self._rowActual + 1
        while i < len(self._arrayRows) and self._arrayRows[i] is None:
            i += 1
        self._rowActual = i
        if i < len(self._arrayRows):
            self._nodoActual = self._arrayRows[i]
        else:
            self._nodoActual = None

class _MatrixElementNode:
    def __init__(self, col, value):
        self.col = col
        self.value = value
        self.next = None


matriz = SparseMatrix(5, 5)
matriz[0, 2] = 4
matriz[4, 1] = 1
matriz[0, 4] = 3
matriz[3, 2] = 2

for elemento in matriz:
    print(elemento)