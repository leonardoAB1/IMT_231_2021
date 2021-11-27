class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self._head = None

    def __contains__(self, item):
        current = self._head
        while current is not None and current.data != item:
            current = current.next
        return current is not None

    def append(self, new_value):
        
        new_node = Node(new_value)

        if self._head is None:
            self._head = new_node
            return
        current = self._head
        while current.next is not None:
            current = current.next
        current.next = new_node

    def traversal(self):  # O(n)
        current = self._head
        while current is not None:
            print(current.data)
            current = current.next

    def remove(self, target):
        pred = None
        current = self._head
        while current is not None and current.data != target:
            pred = current
            current = current.next

        # saltar el node a eliminar
        if current is not None:
            if current is self._head:
                self._head = current.next
            else:
                pred.next = current.next
        return self._head