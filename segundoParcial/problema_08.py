# Implemente el algoritmo Merge Sort para que funcione con una lista enlazada.

from LinkedList import LinkedList

class LinkedList(LinkedList):
    """
    >>> lista = LinkedList()

    >>> lista.append(10)
    >>> lista.append(23)
    >>> lista.append(51)
    >>> lista.append(18)
    >>> lista.append(4)
    >>> lista.append(31)
    >>> lista.append(13)
    >>> lista.append(5)
    
    >>> lista.traversal()
    10
    23
    51
    18
    4
    31
    13
    5
    >>> lista_ordenada=mergeSort(lista)
    >>> lista_ordenada.traversal()
    4
    5
    10
    13
    18
    23
    31
    51
    """
    def __init__(self):
        super().__init__()
    
    def mergeSort(self, head):
        """
        Ordena los nodos de la lista enlazada y retorna la nueva cabeza
        1) if head is None or len(linked_list)==1 -> return
        2) else divide linked list into two halves
        3) apply merge sort to both halves recursivamente
        4) Join groups
        """
        
        if head==None or head.next==None:
            return head
        
        middle=self._get_middle(head)
        next_to_middle=middle.next
        
        #set next to middle to None
        middle.next=None
        
        left=self.mergeSort(head)
        right=self.mergeSort(next_to_middle)
        
        sorted_list=self._join_groups(left, right)
        
        return sorted_list

    def _get_middle(self, head):
        """Devuelve el nodo central dada una cabeza o punto de inicio."""
        if head==None:
            return head
        
        slow = head
        fast = head

        while (fast.next is not None and fast.next.next is not None):
            fast = fast.next.next
            slow = slow.next
            
        return slow

    def _join_groups(self, a, b):
        """Une dos nodos o grupos de nodos"""
        result=None
        
        if a==None:
            return b
        if b==None:
            return a
        
        #ordenar recursivamente
        if a.data<=b.data:
            result=a
            result.next=self._join_groups(a.next, b)
        else:
            result=b
            result.next=self._join_groups(a, b.next)
            
        return result
    
#interfaz para simplificar el uso de merge sort con la lista enlazada
def mergeSort(lista:LinkedList):
    head=lista.mergeSort(lista._head)
    lista._head=head
    return lista

if __name__=="__main__":
    import doctest
    doctest.testmod(verbose=True)
