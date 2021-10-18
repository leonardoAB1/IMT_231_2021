class Stack:
    def __init__(self): # O(1)
        self._elementos = list()

    def isEmpty(self): # O(1)
        return len(self) == 0

    def __len__(self): # O(1)
        return len(self._elementos)

    def peek(self): # O(1)
        assert not self.isEmpty(), "No se puede hacer peek en un stack vacío"
        return self._elementos[-1]

    def pop(self): # O(n)
        assert not self.isEmpty(), "No se puede hacer pop en un stack vacío"
        return self._elementos.pop()

    def push(self, e): # O(n)
        self._elementos.append(e)