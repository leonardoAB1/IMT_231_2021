class Set:
    def __init__(self):
        self._elements=list()
        
    def __len__(self):
        return len(len, _elements)
    
    def __contains__(self, e): #in
        return e in self._elements
    
    def add(self, e):
        if e not in self:
            self._elements.append(e)
            
    def remove(self, e):
        assert e in self, "El elemento debe pertenecer al conjunto"
        self._elements.remove(e)
        
    def __eq__(self, setB):
        if len(self) != len(setB):
            return False
        else:
            return self.isSubsetOf(setB)
        
    def isSubsetOf(self, setB):
        for elemento in self:
            if elemento not in setB:
                return False
        return True
    
    def union(self, setB):
        newSet=Set()
        newSet._elements.extend(self._elements)
        for element in setB:
            if element not in self:
                newSet._elements.append(element)
        return newSet
    
    def intersect(self, setB):
        pass
    
    def difference(self, setB):
        pass
    
    def __iter__(self):
        return _SetIterator(self._elements)
    
class _SetIterator:
    def __init__(self, set):
        self._setRef=set
        self._iActual=0
        
    def __iter__(self):
        return self
    
    def __next__(self):
        if self._iActual<len(self._setRef):
            element=self.__arregloRef[self._iActual]
            self._iActual+=1
            return element
        else:
            raise StopIteration