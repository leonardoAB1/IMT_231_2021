class Set:
    def __init__(self):
        self._elementos = list()

    def __len__(self):
        return len(self._elementos)

    def __contains__(self, e):
        return e in self._elementos
        
    def add(self, e):
        if e not in self:
            self._elementos.append(e)
    
    def remove(self, e):
        assert e in self, "El elemento debe pertenecer al conjunto"
        self._elementos.remove(e)

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
        nuevoSet = Set()
        nuevoSet._elementos.extend(self._elementos)
        for elemento in setB:
            if elemento not in self:
                nuevoSet._elementos.append(elemento)
        return nuevoSet

    def intersect(self, setB):
        nuevoSet = Set()
        for elemento in self:
            if elemento in setB:
                nuevoSet._elementos.append(elemento)
        return nuevoSet

    def difference(self, setB):
        nuevoSet = Set()
        for elemento in self:
            if elemento not in setB:
                nuevoSet._elementos.append(elemento)
        return nuevoSet

    def __iter__(self):
        return _SetIterator(self._elementos)

class _SetIterator:
    def __init__(self, set):
        self._setRef = set
        self._iActual = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._iActual < len(self._setRef):
            elemento = self._setRef[self._iActual]
            self._iActual += 1
            return elemento
        else:
            raise StopIteration