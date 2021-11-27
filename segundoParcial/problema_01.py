#Realice el análisis de complejidad y explique en sus propias palabras por qué 
#nuestra implementación de Stack usando listas enlazadas tiene tiempo 
#constante para todos sus métodos.
#R.-    Tal y como se puede observar, nuestra implementación de stack presenta
#       tiempo constante en todos sus metodos porque solo se realizan operaciones
#       computacionales basicas como ser retorno de variables, asignacion de variables
#       y operaciones aritmeticas basicas.
class Stack:
    def __init__(self):
        self._top=None
        self._size=0
        
    def isEmpty(self): #O(1) Retorna un atributo de la clase
        return self._top is None
    
    def __len__(self): #O(1) Retorna un atributo de la clase
        return self._size
    
    def peek(self):#O(1) Retorna un atributo de la clase
        assert not self.isEmpty(), "No se puede hacer peek en un stack vacío"
        return self._top.data

    def pop(self): #O(1)
        assert not self.isEmpty(), "No se puede hacer pop en un stack vacío"
        nodo=self._top                      #O(1) asignacion
        self._top=self._top.next            #O(1) asignacion
        self._size -= 1                     #O(1) asignacion/operacion aritmetica
        return nodo.data                    #O(1) Retorna un atributo de la clase
    
    def push(self, e): #O(1)
        self._top=_StackNode(e, self._top)  #O(1) asignacion
        self._size +=1                      #O(1) asignacion/operacion aritmetica

class _StackNode:
    def __init__(self, value, next):
        self.data = value
        self.next = next