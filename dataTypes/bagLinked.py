class Bag:
    def __init__(self): #O(n)
        self._head = None
        self._size = 0
        self._tail = None

    def __len__(self):  #O(1)
        return self._size

    def __contains__(self, target): # O(n)
        current_node=self._head
        while current_node is not None and current_node.data != target:
            current_node = current_node.next
        return current_node is not None

    def add(self, item):   #O(1) prepend
        new_node=_BagNode(item)
        new_node.next=self._head
        self._head = new_node
        self._size+=1

    """
    def append(self, item): #O(1)
        new_node = _BagNode(item)
        if self._head is None:
            self.head = new_node
        else:
            self._tail.next = new_node
        self._tail = new_node
    
    
    def remove(self, item):
        pred = None
        current_node = self._head
        while current_node is not None and current_node!=item:
            pred = current_node
            current_node = current_node.next
        if current_node is not None:
            if  current_node is self._head:
                self._head= current_node.next
            else:
                pred.next = current_node.next
            if current_node is self._tail:
                self._tail = pred
    """
    
    def remove(self, item): #O(n)
        pred = None
        current_node = self._head
        while current_node is not None and current_node.data != item:
            pred = current_node
            current_node = current_node.next
        assert current_node is not None, "Item not in bag"
        
        self._size -= 1
        if current_node is self._head:
            self._head = current_node.next
        else:
            pred.next =current_node.next
        return current_node.data

    def __iter__(self):
        return _BagIterator(self._head)

    #   traversal O(n)

class _BagIterator:
    def __init__(self, head):
        self._current_node = head

    def __iter__(self):
        return self

    def __next__(self):
        if self._current_node is None:
            raise StopIteration()
        else:
            item = self._current_node.data
            self._current_node = _current_node.next
            return item
        
        
class _BagNode(object):
    def __init__(self, item):
        self.data = item
        self.next = Node
