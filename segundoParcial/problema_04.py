#Implemente un método para remover nodos de una lista doblemente enlazada. 
#Realice el análisis de complejidad del método implementado.

class DNode:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    """
    >>> DList=DoublyLinkedList()
    >>> DList.insert(0)
    >>> DList.insert(1)
    >>> DList.insert(2)
    >>> DList.insert(7)
    >>> DList.insert(8)
    >>> DList.insert(9)
    >>> DList.traversal()
    0
    1
    2
    7
    8
    9
    >>> DList.traversal_from_tail()
    9
    8
    7
    2
    1
    0
    >>> DList.search(8).data==8
    True
    >>> DList.insert(6)
    >>> DList.insert(12)
    >>> DList.traversal()
    0
    1
    2
    6
    7
    8
    9
    12
    >>> DList.traversal_from_tail()
    12
    9
    8
    7
    6
    2
    1
    0
    >>> DList.insert(-2)
    >>> DList.traversal()
    -2
    0
    1
    2
    6
    7
    8
    9
    12
    >>> DList.traversal_from_tail()
    12
    9
    8
    7
    6
    2
    1
    0
    -2
    >>> DList.remove(12)
    >>> DList.traversal()
    -2
    0
    1
    2
    6
    7
    8
    9
    >>> DList.traversal_from_tail()
    9
    8
    7
    6
    2
    1
    0
    -2
    >>> DList.remove(6)
    >>> DList.traversal()
    -2
    0
    1
    2
    7
    8
    9
    >>> DList.traversal_from_tail()
    9
    8
    7
    2
    1
    0
    -2
    >>> DList.remove(-2)
    >>> DList.traversal()
    0
    1
    2
    7
    8
    9
    >>> DList.traversal_from_tail()
    9
    8
    7
    2
    1
    0
    """
    def __init__(self):
        self.head=None
        self.tail=None
    
    def traversal(self):
        nodo_actual = self.head
        while nodo_actual is not None:
            print(nodo_actual.data)
            nodo_actual = nodo_actual.next
            
    def traversal_from_tail(self):
        nodo_actual = self.tail
        while nodo_actual is not None:
            print(nodo_actual.data)
            nodo_actual = nodo_actual.prev
            
    def search(self, target):#O(n)
        """Returns reference to target node"""
        if self.head is None:
            return

        nodo_actual = self.head

        if target < nodo_actual.data:
            while nodo_actual is not None and target <= nodo_actual.data:
                if target == nodo_actual.data:
                    return nodo_actual
                else:
                    nodo_actual = nodo_actual.prev
        else:
            while nodo_actual is not None and target >= nodo_actual.data:
                if target == nodo_actual.data:
                    return nodo_actual
                else:
                    nodo_actual = nodo_actual.next

        return

    def insert(self, value):
        nuevo_nodo = DNode(value)
        
        if self.head is None:
            self.head = nuevo_nodo
            self.tail = nuevo_nodo
        elif value < self.head.data:
            nuevo_nodo.next = self.head
            self.head.prev = nuevo_nodo
            self.head = nuevo_nodo
        elif value > self.tail.data:
            nuevo_nodo.prev = self.tail
            self.tail.next = nuevo_nodo
            self.tail = nuevo_nodo
        else:
            nodo_actual = self.head
            while nodo_actual is not None and nodo_actual.data < value:
                nodo_actual = nodo_actual.next

            nuevo_nodo.next = nodo_actual
            nuevo_nodo.prev = nodo_actual.prev
            nodo_actual.prev.next = nuevo_nodo
            nodo_actual.prev = nuevo_nodo
            
    def remove(self, value):#O(n) en el peor de los casos, O(1) en el mejor
        #edge case empty list or argument
        if value is None or self.head is None:#O(1)
            return
        
        #if node to remove is head
        elif self.head.data==value:#O(1)
            self.head.next.prev=None
            self.head=self.head.next
            
        #if node to remove is tail#O(1)
        elif self.tail.data==value:
            self.tail.prev.next=None
            self.tail=self.tail.prev
            
        else:
            node_to_remove=self.search(value)#O(n)
            #value not found in list
            if node_to_remove is None:#O(1)
                return

            #remove middle node
            if node_to_remove.next is not None:#O(1)
                node_to_remove.next.prev=node_to_remove.prev
                
            #change prev only if the prev of node to delete is not None
            if node_to_remove.prev is not None:#O(1)
                node_to_remove.prev.next=node_to_remove.next


if __name__=="__main__":
    import doctest
    doctest.testmod(verbose=True)