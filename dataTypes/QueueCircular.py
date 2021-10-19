from Arrays import Array

class Queue:
    def __init__(self, maxSize):
        self._conteo=0
        self._front=0
        self._back=maxSize-1
        self.qArray=Array(maxSize)
        
    def isEmpty(self):
        return self._conteo==0
    
    def isFull(self):
        return self._conteo==len(self._qArray)
    
    def __len__(self):
        return self._conteo
    
    def enqueue(self, e):
        assert not self.isFull(), "No se puede hacer enqueue a una cola llena"
        maxSize=len(self._qArray)
        self._back=(self.back+1)%maxSize
        self._qArray[self._back]=e
        self._conteo+=1
        
    def dequeue(self):
        assert not self.isEmpty(), "No se puede hacer dequeue de una cola vacía"
        elemento=self._qArray[self._front]
        maxSize=len(self._qArray)
        self._front=(self._front +1) % maxSize
        self._conteo -= 1
        return elemento