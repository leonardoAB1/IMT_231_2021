class Bag:
    def __init__(self): # O(1)
        self._head = None
        self._size = 0
        self._tail = None

    def __len__(self): # O(1)
        return self._size

    def __contains__(self, objetivo): # O(n)
        nodoActual = self._head
        while nodoActual is not None and nodoActual.data != objetivo:
            nodoActual = nodoActual.next
        return nodoActual is not None

    def add(self, elemento): # O(1)
        nuevoNodo = _BagNode(elemento)
        nuevoNodo.next = self._head
        self._head = nuevoNodo
        self._size += 1

    # def append(self, elemento): # O(1)
    #     nuevoNodo = _BagNode(elemento)
    #     if self._head is None:
    #         self._head = nuevoNodo
    #     else:
    #         self._tail.next = nuevoNodo
    #     self._tail = nuevoNodo

    # def remove(self, elemento):
    #     pred = None
    #     nodoActual = self._head
    #     while nodoActual is not None and nodoActual.data != elemento:
    #         pred = nodoActual
    #         nodoActual = nodoActual.next

    #     if nodoActual is not None:
    #         if nodoActual is self._head:
    #             self._head = nodoActual.next
    #         else:
    #             pred.next = nodoActual.next
    #         if nodoActual is self._tail:
    #             self._tail = pred


    def remove(self, elemento): # O(n)
        pred = None
        nodoActual = self._head
        while nodoActual is not None and nodoActual.data != elemento:
            pred = nodoActual
            nodoActual = nodoActual.next
        
        assert nodoActual is not None, "El elemento no es parte de la bolsa"

        self._size -= 1
        if nodoActual is self._head:
            self._head = nodoActual.next
        else:
            pred.next = nodoActual.next
        return nodoActual.data

    def __iter__(self):
        return _BagIterator(self._head)

    # traversal O(n)

class _BagIterator:
    def __init__(self, head):
        self._nodoActual = head

    def __iter__(self):
        return self

    def __next__(self):
        if self._nodoActual is None:
            raise StopIteration
        else:
            elemento = self._nodoActual.data
            self._nodoActual = self._nodoActual.next
            return elemento

    
class _BagNode(object):
    def __init__(self, elemento):
        self.data = elemento
        self.next = None