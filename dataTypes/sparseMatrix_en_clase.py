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
        current_node = self.self._arrayRows[row]
        while current_node is not None and current_node.col !=col:
            pred=current_node
            current_node=current_node.next
        if current_node is not None and currentNode.col==col:
            if value == 0.0:
                if current_node== self._arrayRows[row]:
                    self._arrayRows[row]=current_node.next
                else:
                    pred.next = currentNode.next
            else:
                current_node.value=value
                
        elif value != 0.0:
            newNode = _MatrixElementNode(col, value)
            newNode.next=current_node
            if currentNode == self._arrayRows[row]:
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
        
class _MatrixElementNode:
    def __init__(self, col, value):
            self.col=col
            self.value=value
            self.next=None    
        