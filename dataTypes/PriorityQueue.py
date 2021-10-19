class PriorityQueue:
    def __init__(self):
        self._qLista=list()
        
    def isEmpty(self):
        return len(self._qLista)==0
    
    def __len__(self):
        return len(self._qLista)
    
    def enqueue(self, e, p):
        item=_PriorityQueueElemento(e, p)
        self._qLista.append(item)
        
    def dequeue(self):
        assert not self.isEmpty(), "No se puede hacer dequeue de una cola vacía"
        
        mayor_prioridad=self._qLista[0].priority
        indice=0
        for i in range(len(self)):
            if self._qLista[i].priority < mayor_prioridad:
                mayor_prioridad=self._qLista[i].priority
                indice=i
                
        item=self._qLista.pop(indice)
        return item.elemento
        
        
class _PriorityQueueElemento:
    def __init__(self, data, priority):
        self.elemento=data
        self.priority=priority
        
        
from Arrays import Array
from QueueLinked import Queue

class BPriorityQueue:
    def __init__(self, numNiveles):
        self._qSize=0
        self._qNiveles=Array(numNiveles)
        for i in range(numNiveles):
            self._qNiveles[i]=Queue()

    def isEmpty():
        return self._qSize==0
        
    def __len__(self):
        return self._qSize
    
    def enqueue(self, e, p):
        assert p>=0 and p<len(self._qNiveles), "Prioridad fuera de rango"
        self._qNiveles[p].enqueue(e)
        self.qSize+=1
        
    def dequeue(self):
        assert not self.isEmpty(),  "No se puede hacer dequeue de una cola vacía"
        i=0
        p=len(self._qNiveles)
        while i < p and self._qNiveles[i].isEmpty():
            i+=1
        self._qSize-=1
        return self._qNiveles[i].dequeue() 
        