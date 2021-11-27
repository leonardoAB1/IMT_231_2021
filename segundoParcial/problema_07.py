#Modifique el ADT HashMap para que utilice hashing abierto o chaining en lugar 
#de hashing cerrado.

# hashable= int, float, str, tuple, None
# no hasheable= list, dict, set

from LinkedList import LinkedList
from Arrays import Array

class MapEntry:
    def __init__(self, key, value):
        self.next = None
        self.key=key
        self.value=value
        self.data=self.value
        
class Chain(LinkedList):
    def __init__(self):
        self._head = None
        
    def append(self, key, new_value):
        
        new_node = MapEntry(key, new_value)
        
        if self._head is None:
            self._head = new_node
            return
        current = self._head
        while current.next is not None:
            current = current.next
        current.next = new_node
        
    def remove(self, key):
        pred = None
        current = self._head
        while current is not None and current.key != key:
            pred = current
            current = current.next

        # saltar el node a eliminar
        if current is not None:
            if current is self._head:
                self._head = current.next
            else:
                pred.next = current.next
        return self._head
        
    def __iter__(self):
        return _ChainIterator(self._head)

class _ChainIterator:
    def __init__(self, head):
        self._current_node = head

    def __iter__(self):
        return self

    def __next__(self):
        if self._current_node is None:
            raise StopIteration()
        else:
            item = self._current_node
            self._current_node = self._current_node.next
            return item

class LinkedHashMap:
    """
    >>> d=LinkedHashMap()
    
    >>> d.add(1, "hola")
    >>> d.add(8, "Pepito")
    >>> print(d.valueOf(1))
    hola
    >>> print(d.valueOf(8))
    Pepito
    >>> d.add(256, "mundo")
    >>> print(d.valueOf(256))
    mundo
    >>> d.remove(256)
    >>> try:
    ...     d.valueOf(256)
    ... except AssertionError:
    ...     pass
    """
    
    def __init__(self):
        self._tabla=Array(7)
        self._conteo=0
        
    def __len__(self):
        return conteo
    
    def __contains__(self, key):
        try:
            if self._findEntry(key) is not None:
                return True
        except AssertionError:
            False
    
    def _findEntry(self, key):
        posicion=self._hash1(key)
        assert self._tabla[posicion] is not None, "Llave Invalida"
        for entry in self._tabla[posicion]:
            if entry.key==key:
                return entry
    
    def add(self, key, value):
        posicion=self._hash1(key)
        if self._tabla[posicion] is None:
            self._tabla[posicion]=Chain()
            
        if key in self:
            entry=self._findEntry(key)
            entry.value=value
        else:
            self._tabla[posicion].append(key, value)
            self._conteo+=1
        
    def _hash1(self, key):
        return abs(hash(key)%len(self._tabla))
    
    def valueOf(self, key):
        assert key in self, "Llave invalida"
        value=self._findEntry(key).value
        return value
        
    def remove(self, key): 
        posicion=self._hash1(key)
        if key in self:
            self._tabla[posicion].remove(key)
    
    def __iter__(self):
        return _LinkedHashMapIterator(self._tabla)
           
        
class _LinkedHashMapIterator:
    def __init__(self, mapa):
        self._tabla=mapa
        self._iActual= 0
        
    def __iter__(self):
        return self
    
    def __next__(self):
        if self._iActual < len(self._tabla):
            element=self._tabla[self._iActual]
            self._iActual += 1
            return element
        else:
            raise StopIteration

if __name__=="__main__":
    import doctest
    doctest.testmod(verbose=True)
