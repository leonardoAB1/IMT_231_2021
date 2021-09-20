class Set:
    def __init__(self):
        self._elementos = list()

    def __len__(self):
        return len(self._elementos)

    def __contains__(self, e):
        ix = self._findPosition(e)
        return ix < len(self._elementos) and self._elementos[ix] == e

    def _findPosition(self, e):
        inferior = 0
        superior = len(self._elementos) - 1
        while inferior <= superior:
            medio = inferior + superior // 2
            if self._elementos[medio] == e:
                return medio
            elif e < self._elementos[medio]:
                superior = medio - 1
            else:
                inferior = medio + 1
        return inferior

    def add(self, e):
        if e not in self:
            ix = self._findPosition(e)
            self._elementos.insert(ix, e)

    def remove(self, e):
        pass

    def __eq__(self, setB):
        if len(self) != len(setB):
            return False
        else:
            for i in range(len(self)):
                if self._elementos[i] != setB._elementos[i]:
                    return False
            return True    
