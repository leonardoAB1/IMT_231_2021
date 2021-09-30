        
class sparseMatrix:
    """
    >>> Z=sparseMatrix(3,2)
    >>> Z[0,0]=1
    >>> Z[1,0]=2
    >>> Z[2,0]=3
    >>> Z[1,1]=5
    >>> Z[2,1]=6
    >>> Z._rows[0].traversal() 
    1
    >>> Z._rows[0][1]
    0
    >>> Z._rows[1].traversal() 
    2
    5
    >>> Z._rows[2].traversal() 
    3
    6
    """
        
    def __init__(self, nRows, nCols): #O(n)
        self._nCols=nCols
        self._nRows=nRows
        self._rows = linkedList(nRows)
        
        for i in range(nRows):
            self._rows[i] = linkedList(nCols)
        
    def numCols(self):
        return self._nCols

    def numRows(self):
        return self._nRows
        
    def __getitem__(self, ndIndex): # ndIndex[0] = i1, ndIndex[1] = i2
        assert len(ndIndex) == 2, "Número inválido de subindíces"
        row = ndIndex[0]
        column = ndIndex[1]
        assert row >= 0 and row < self.numRows() \
            and column >= 0 and column < self.numCols(), \
                "Subíndices fuera  de rango"
        return self._rows[row][column]
    
    def __setitem__(self, ndIndex, value):
        assert len(ndIndex) == 2, "Número inválido de subindíces"
        row = ndIndex[0]
        column = ndIndex[1]
        assert row >= 0 and row < self.numRows() \
            and column >= 0 and column < self.numCols(), \
                "Subíndices fuera  de rango"
        array_interno = self._rows[row]
        array_interno[column] = value
        
        
        
class linkedList:
    def __init__(self, size):
        self._head=None
        self._size = size
        
    def __len__(self):  #O(1)
        return self._size
    
    def __getitem__(self, index):
        assert index >= 0 and index < len(self), "Index out of range"
        pred = None
        current_node = self._head
        while current_node is not None and current_node.index != index:
            pred = current_node
            current_node = current_node.next
        if current_node is not None:
            return current_node.data
        else:
            return 0
    
    def __setitem__(self, index, item):
        assert index >= 0 and index < len(self), "Index out of range"
        pred = None
        current_node = self._head
        while current_node is not None and current_node.index < index:
            pred = current_node
            current_node = current_node.next
            
        new_node = Node(item)
        new_node.index = index
        new_node.next = current_node
        
        if current_node is self._head:
            self._head=new_node
        else:
            pred.next = new_node
    
    def __contains__(self, item): #O(n)
        current=self._head
        while current is not None and current.data != item:
            current=current.next
        return current is not None
    
    def traversal(self): #O(n)
        current=self._head
        while current is not None:
            print(current.data)
            current=current.next

    def remove(self, target):
        pred=None
        current=self._head
        while current is not None and current.data != target:
            pred=current
            current=current.next
            
        #saltar al node a eliminar
        if current is not None:
            if current is self._head:
                self._head=current.next
            else:
                pred.next=current.next
        return self._head


class _ListIterator:
    def __init__(self, head):
        self._current_node = head

    def __iter__(self):
        return self

    def __next__(self):
        if self._current_node is None:
            raise StopIteration()
        else:
            item = self._current_node.data
            self._current_node = _current_node.next
            return item
     
        
class Node:
    def __init__(self, data):
        self.data=data
        self.next=None
        self.index=0
        
        
if __name__=="__main__":
    import doctest
    doctest.testmod(verbose=True)