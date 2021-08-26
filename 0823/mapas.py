class Map:
    def __init__(self):
        self._listaEntries = list()
    
    def __len__(self):
        return len(self._listaEntries)

    def __contains__(self, key):
        ix = self._findPosition(key)
        return ix is not None
    
    def _findPosition(self, key):
        for i in range(len(self)):
            if self._listaEntries[i].key == key:
                return i
        return None

    def add(self, key, value):
        ix = self._findPosition(key)
        if ix is not None:
            self._listaEntries[ix].value = value
            return False
        else:
            entry = _MapEntry(key, value)
            self._listaEntries.append(entry)
            return True

    def valueOf(self, key):
        ix = self._findPosition(key)
        assert ix is not None, "Llave inválida"
        return self._listaEntries[ix].value

    def remove(self, key):
        ix = self._findPosition(key)
        assert ix is not None, "Llave inválida"
        self._listaEntries.pop(ix)

    def __iter__(self):
        return _MapIterator(self._listaEntries)

class _MapIterator:
    def __init__(self, mapa):
        self._mapaRef = mapa
        self._iActual = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._iActual < len(self._mapaRef):
            elemento = self._mapaRef[self._iActual]
            self._iActual += 1
            return elemento
        else:
            raise StopIteration

class _MapEntry:
    def __init__(self, key, value):
        self.key = key
        self.value = value