class Vector(object):
    def __init__(self, n=0, x=None):
        if n >= 0:
            self._data = [x for i in range(n)]
        else:
            raise Exception("Numero invalido de elementos")

    def __repr__(self):
        return str(self._data)

    def __str__(self):
        return str(f"Contenido: {str(self._data)}")

    def add(self, n):
        self._data.append(n)
        return self

    def insert(self, i, n):
        self._data.insert(i, n)

    def remove(self, n):
        pass

    def get(self, i):
        pass

    def set(self, i, n):
        pass

    def size(self):
        pass

    def isEmpty(self):
        pass

    def clear(self):
        pass
