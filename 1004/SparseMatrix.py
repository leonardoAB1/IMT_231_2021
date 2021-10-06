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

    def scaleBy(self, scalar):
        """Escala los valores de la matrix por un escalar"""
        pass

    def transpose(self):
        """Traspone la matrix"""
        pass

    def __add__(self, rhsMatrix):
        """Suma una segunda matriz a la actual"""
        pass



    

class _MatrixElementNode:
    def __init__(self, col, value):
        self.col = col
        self.value = value
        self.next = None