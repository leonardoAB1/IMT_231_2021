class Stack:
    def __init__(self):
        self._top=None
        self._size=0
        
    def isEmpty(self): #O(1)
        return self._top is None
    
    def __len__(self): #O(1)
        return self._size
    
    def peek(self):#O(1)
        assert not self.isEmpty(), "No se puede hacer peek en un stack vacío"
        return self._top.data

    def pop(self): #O(1)
        assert not self.isEmpty(), "No se puede hacer pop en un stack vacío"
        nodo=self._top
        self._top=self._top.next
        self._size -= 1
        return nodo.data
    
    def push(self, e): #O(1)
        self._top=_StackNode(e, self._top)
        self._size +=1

class _StackNode:
    def __init__(self, value, next):
        self.data = value
        self.next = next