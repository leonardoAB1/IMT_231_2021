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
        pred=None
        current_node = self._arrayRows[row]
        while current_node is not None and current_node.col !=col:
            pred=current_node
            current_node=current_node.next
        if current_node is not None and current_node.col==col:
            if value == 0.0:
                if current_node== self._arrayRows[row]:
                    self._arrayRows[row]=current_node.next
                else:
                    pred.next = current_node.next
            else:
                current_node.value=value
                
        elif value != 0.0:
            newNode = _MatrixElementNode(col, value)
            newNode.next=current_node
            if current_node == self._arrayRows[row]:
                self._arrayRows[row]=newNode
            else:
                pred.next=newNode
                
    def __getitem__(self, indexTuple):
        row, col = indexTuple
        current_node=self._arrayRows[row]
        while current_node is not None and current_node.col != col:
            current_node = current_node.next
            
        if current_node is not None:
            return current_node.value
        else:
            return 0
        
    def scaleBy(self, scalar):
        """Escala los valores de la matrix por un escalar"""
        pass
    
    def scaleBy(self):
        """Transpone la matrix"""
        pass
    
    def __add_(self, rhsMatrix):
        """Suma la segunda matrix a la actual"""
        pass
    
    def __iter__(self):
        return _SparseMatrixIterator(self._arrayRows)
        
class _SparseMatrixIterator:
    def __init__(self, arrayRows):
        self._arrayRows=arrayRows
        self._rowActual=-1
        self._nodoActual=None
        self._buscarSiguieteElemento()
        
    def __iter__(self):
        return self
    
    def __next__(self):
        if self._nodoActual is None:
            raise StopIteration
        else:
            valor=self._nodoActual.value
            self._nodoActual=self._nodoActual.next
            if self._nodoActual is None:
                self._buscarSiguieteElemento()
            return valor
        
    def _buscarSiguieteElemento(self):
        i=self._rowActual+1
        while i<len(self._arrayRows) and self._arrayRows[i] is None:
            i+=1
        self._rowActual=i
        if i<len(self._arrayRows):
            self._nodoActual=self._arrayRows[i]
        else:
            self._nodoActual=None
    
class _MatrixElementNode:
    def __init__(self, col, value):
            self.col=col
            self.value=value
            self.next=None    
        
        
def main():
    matriz=SparseMatrix(5, 5)
    matriz[0, 2]=4
    matriz[4, 1]=1
    matriz[0, 4]=3
    matriz[3, 2]=2
    
    for elemento in matriz:
        print(elemento)
        
        
if __name__=="__main__":
    main()