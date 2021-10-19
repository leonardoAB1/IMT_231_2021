class Queue:
    def __init__(self):
        self._qLista=list()
        
    def isEmpty(self):
        return len(self)==0
    
    def __len__(self):
        return len(self._qLista)
    
    def enqueue(self, e):
        self._qLista.append(e)
        
    def dequeue(self):
        assert not self.isEmpty(), "No se puede hacer dequeue de una cola vacía"
        return self._qLista.pop(0)