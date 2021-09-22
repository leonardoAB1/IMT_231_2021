"""
Problema 6
Complete el tipo de dato Set implementado en clase, 
implementado los métodos intersect() y difference().
"""
class Set:
    """
    >>> setA=Set()            
    >>> setB=Set()
    >>> setC=Set()
    >>> for i in range(12):
    ...     setA.add(i)
    ... 
    >>> for i in range(9,15):
    ...     setB.add(i)
    ...                     
    >>> for i in range(4,9):  
    ...     setC.add(i)
    ... 
    >>> setA
    {0,1,2,3,4,5,6,7,8,9,10,11}
    >>> setB
    {9,10,11,12,13,14}
    >>> setC
    {4,5,6,7,8}
    >>> setA==setB
    False
    >>> setC.isSubsetOf(setA)
    True
    >>> len(setA) 
    12
    >>> setA.union(setB) 
    {0,1,2,3,4,5,6,7,8,9,10,11,12,13,14}
    >>> setA.intersect(setB) 
    {9,10,11}
    >>> setA.difference(setB)
    {0,1,2,3,4,5,6,7,8,12,13,14}
    """
    def __init__(self):
        "Crea un nuevo conjunto inicializando a un conjunto vacio."
        self._elements=list()
        
    def __len__(self):
        """
        Retorna el numero de elementos en el conjunto(cardinalidad). 
        Se accede a este método a través de la funcion len()
        """
        return len(self._elements)
    
    def __repr__(self):
        "Returns a printable representational string of set."
        string="{"
        for i in self._elements:
            string+=f"{i},"
        return string[:-1]+"}"
    
    def __contains__(self, e):
        """
        Determina si el elemento es parte del conjunto y retorna el valor booleano apropiado. 
        Se accede a este método a través del operador `in`.
        """
        return e in self._elements
    
    def add(self, e):
        """
        Modifica el conjunto agregando ele elemento al conjunto si es que
        no es parte del mismo. Si el elemento no es unico, 
        no se realiza niniguna accion.
        """
        if e not in self:
            self._elements.append(e)
            
    def remove(self, e):
        """
        Remueve el elemento del conjunto si es que está contenido en el mismo, 
        sino levanta una excepcion.
        """
        assert e in self, "El elemento debe pertenecer al conjunto"
        self._elements.remove(e)
        
    def __eq__(self, setB):
        """
        Determina si un conjunto es igual a otro y retorna un booleano. 
        Dos conjuntos son iguales si contienen el mismo numero de elementos, 
        y todos los elementos del conjunto A están contenidos en el 
        conjunto B. Si ambos conjuntos estan vacios, los conjuntos son 
        iguales. Se accede a este metodo con los operadores `==` y `|=`.
        """
        if len(self) != len(setB):
            return False
        else:
            return self.isSubsetOf(setB)
        
    def isSubsetOf(self, setB):
        """
        Determina si el conjunto es un subconunto de otro conjunto y
        retorna un valor booleano. Para que A sea un subconjunto de B,
        todos los elelmtnos de A deben pertenecer tambien a B
        """
        for elemento in self:
            if elemento not in setB:
                return False
        return True
    
    def union(self, setB):
        """
        Crea y retorna un nuevo conjunto que es la unión de este conjunto
        y `setB`. El nuevo conjunto contiene todos los elementos mas los
        elementos de B que no pertenencen a A. Ninguno de los conjuntos A
        o B son modificados.
        """
        newSet=Set()
        newSet._elements.extend(self._elements)
        for element in setB:
            if element not in self:
                newSet._elements.append(element)
        return newSet
    
    def intersect(self, setB):
        """
        Crea y retorna un nuevo conjunto que es la interseccion 
        de este conjunto y `setB`. La interseccion A y B contiene 
        solo los elementos que pertenecen tanto a A como a B.
        """
        newSet=Set()
        for element in setB:
            if element in self:
                newSet._elements.append(element)
        return newSet
    
    def difference(self, setB):
        """
        Crea y retorna un nuevo conjunto que es la diferencia 
        de este conjunto con `setB`. La diferencia de 
        conjuntos $ A - B$, contiene solo los elementos de A 
        que no están en B. Ninguno de los conjuntos A o B 
        son modificados.
        """
        newSet=Set()
        for element in self._elements:
            if element not in setB:
                newSet._elements.append(element)
        for element in setB:
            if element not in self:
                newSet._elements.append(element)
        return newSet
    
    def __iter__(self):
        """
        Crea y retorna un iterador que puede ser usado para 
        iterara los elementos del conjunto.
        """
        return _SetIterator(self._elements)
    
class _SetIterator:
    def __init__(self, set):
        self._setRef=set
        self._iActual=0
        
    def __iter__(self):
        return self
    
    def __next__(self):
        if self._iActual<len(self._setRef):
            element=self._setRef[self._iActual]
            self._iActual+=1
            return element
        else:
            raise StopIteration
        
if __name__=="__main__":
    import doctest
    doctest.testmod(verbose=True)