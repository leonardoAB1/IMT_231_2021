#Implemente un método para remover nodos de una lista circular. Realice el 
#análisis de complejidad del método implementado.
class Node:
    def __init__(self, data):
        self.data = data
        self.next = next

class CircularLinkedList:
    """
    >>> cllist=CircularLinkedList()
    >>> cllist.add(5)
    >>> cllist.add(3)
    >>> cllist.add(8)
    >>> cllist.add(12)
    >>> cllist.add(7)
    >>> cllist.add(88)
    >>> cllist.traversal()
    3
    5
    7
    8
    12
    88
    >>> cllist.search(0)
    False
    >>> cllist.remove(5)
    >>> cllist.traversal()
    3
    7
    8
    12
    88
    >>> cllist.remove(3)
    >>> cllist.traversal()
    7
    8
    12
    88
    >>> cllist.remove(88)
    >>> cllist.traversal()
    7
    8
    12
    """
    def __init__(self, listRef=None):
        self.listRef = listRef

    def traversal(self):
        nodo_actual = self.listRef
        terminado = self.listRef is None
        while not terminado:
            nodo_actual = nodo_actual.next
            print(nodo_actual.data)
            terminado = nodo_actual is self.listRef

    def search(self, target):
        nodo_actual = self.listRef
        terminado = self.listRef is None
        while not terminado:
            nodo_actual = nodo_actual.next
            if nodo_actual.data == target:
                return True
            else:
                terminado = nodo_actual is self.listRef
                # si lista circular esta ordenada
                # terminado = nodo_actual is listRef or nodo_actual.data > target
        return False

    def add(self, value):
        nuevo_nodo = Node(value)
        if self.listRef is None:
            self.listRef = nuevo_nodo
            nuevo_nodo.next = nuevo_nodo
        elif value < self.listRef.next.data: # insert at the front
            nuevo_nodo.next = self.listRef.next
            self.listRef.next = nuevo_nodo
        elif value > self.listRef.data: # insert at the back
            nuevo_nodo.next = self.listRef.next
            self.listRef.next = nuevo_nodo
            self.listRef = nuevo_nodo
        else: # insert in the middle
            pred = None
            nodo_actual = self.listRef
            terminado = self.listRef is None
            while not terminado:
                pred = nodo_actual
                nodo_actual = nodo_actual.next
                terminado = nodo_actual is self.listRef or nodo_actual.data > value
            nuevo_nodo.next = nodo_actual
            pred.next = nuevo_nodo
            
    def remove(self, value):#En el mejor de los casos O(1), en el peor de los casos O(n)
        #empty list
        if self.listRef==None:#O(1)
            return
            
        #single element cll
        if (self.listRef.data==value) and (self.listRef.next==self.listRef):#O(1)
            self.listRef=None
            return
        
        current=self.listRef
        #element to delete is listRef
        if self.listRef.data==value:
            #find last node
            while current.next!=self.listRef: #O(n)
                current=current.next
            #point last node to the next of listRef
            current.next=self.listRef.next
            self.listRef=current
            return 
        else:
            #search node to be deleted until end or value found
            while current.next != self.listRef and current.next.data!=value:#O(n)
                current=current.next
        
            #check if found
            if current.next.data==value:#O(1)
                tmp=current.next
                current.next=tmp.next
            
            else:#O(1)
                return
        
        
if __name__=="__main__":
    import doctest
    doctest.testmod(verbose=True)
