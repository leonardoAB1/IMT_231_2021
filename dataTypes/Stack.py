class Stack:
    def __init__(self): #O(1)
        """
        Crea un stack vacio
        """
        self._elements= list()
        
    def isEmpty(self): #O(1)
        """
        Retorna un booleano indicando si la estructura está vacia.
        """
        return len(self)==0
    
    def __len__(self): #O(1)
        """
        Retorna el numero de elementos contenidos.
        """
        return len(self._elements)
    
    def peek(self): # O(1)
        """
        Retorna una referencia al elemnto en la cima del stack 
        sin removerlo. No se puede hacer peek en un stack vacío 
        y no modifica los elementos contenidos.
        """
        assert not self.isEmpty(), "No se puede hacer peek en un stack vacío."
        return self._elements[-1]
    
    def pop(self): #O(n)
        """
        Remueve y retorna el elemento en la cima del stack si el stack no 
        está vacío. No se puede hacer pop en un stack vacío. Al hacer pop, 
        el siguiente elemento subre a la cima del stack.
        """
        assert not self.isEmpty(), "No se puede hacer pop en un stack vacío"
        return self._elements.pop()
    
    def push(self, e): #O(0)
        """
        Agrega el elemento a la cima del stack.
        """
        serlf._elements.append(e)