class Queue:
    def __init__(self):
        self._conteo = 0
        self._qhead = None
        self._qtail = None

    def isEmpty(self):
        return self._qhead is None

    def __len__(self):
        return self._conteo

    def enqueue(self, e):
        item = _QueueNode(e)
        if self.isEmpty():
            self._qhead = item
        else:
            self._qtail.next = item

        self._qtail = item
        self._conteo += 1

    def dequeue(self):
        assert not self.isEmpty(), "No se puede hacer dequeue en una cola vacía"
        item = self._qhead
        if self._qhead is self._qtail:
            self._qtail = None
        self._qhead = self._qhead.next
        self._conteo -= 1
        return item.data

class _QueueNode:
    def __init__(self, data):
        self.data = data
        self.next = None