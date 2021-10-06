class Bag:
    def __init__(self): # O(1)
        self._elementos = list()

    def __len__(self): # O(1)
        return len(self._elementos)

    def __contains__(self, e): # O(n)
        return e in self._elementos

    def add(self, e): # O(n)
        self._elementos.append(e)

    def remove(self, e): # O(n)
        assert e in self._elementos
        index = self._elementos.index(e)
        return self._elementos.pop(index)

    def __iter__(self):
        return _BagIterator(self._elementos)

    # traversal O(n)

class _BagIterator:
    def __init__(self, coleccion):
        self._bagElements = coleccion
        self._elementoActual = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._elementoActual < len(self._bagElements):
            elemento = self._bagElements[self._elementoActual]
            self._elementoActual += 1
            return elemento
        else:
            raise StopIteration