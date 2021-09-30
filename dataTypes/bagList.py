class Bag:
    def __init__(self): #O(n)
        self._elements = list()

    def __len__(self):  #O(1)
        return len(self._elements)

    def __contains__(self, e): # O(n)
        return e in self._elements

    def add(self, e):   #O(n)
        self._elements.append(e)

    def remove(self, e): #O(n)
        assert e in self._elements, "element not in collection"
        index = self._elements.index(e)
        return self._elements.pop(index)

    def __iter__(self):
        return _BagIterator(self._elements)

    #   traversal O(n)

class _BagIterator:
    def __init__(self, collection):
        self._bagElements = collection
        self._current = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._current < len(self._bagElements):
            element = self._bagElements[self._current]
            self._current += 1
            return element
        else:
            raise StopIteration()
