#Implemente los métodos remove, __iter__ del tipo de dato abstracto HashMap 
#implementado en clase.

#Nota: La implementacion del metodo __str__ de HashMap hace uso del iterador implementado en HashMap

from Arrays import Array

class _MapEntry:
    def __init__(self, key, value):
        self.key=key
        self.value=value

    def __str__(self):
        if (self.key and self.value) is not None:
            return f"{self.key}:{self.value}"
        else:
            return "▲"

class HashMap:
    """
    >>> d=HashMap()
    >>> d.add(1, "hola")
    True
    >>> d.add(2, "mundo")
    True
    >>> d.add(8, "soy una llave")
    True
    >>> print(d)
    {None, 1:hola, 2:mundo, None, None, 8:soy una llave, None}
    >>> d.add(2, "Juan")
    False
    >>> d.remove(8)
    >>> print(d)
    {None, 1:hola, 2:Juan, None, None, 8:▲, None}
    """
    PREV_OCUPADO=_MapEntry(None, None)
    VACIO=None
    
    def __init__(self):
        self._tabla=Array(7)
        self._conteo=0
        self._maxConteo=len(self._tabla)-(len(self._tabla)//4)
        
    def __len__(self):
        return conteo
    
    def __contains__(self, key):
        posicion=self._findPosition(key, False)
        return posicion is not None
    
    def __str__(self):
        string="{"
        for i in self:
            if i is not None:
                string+=f"{i.__str__()}, "
            else:
                string+="None, "
        string=string[:-2]
        return string+"}"
    
    #INSERTAR _tabla[posicion]
    #T          VACIO               return posicion x
    #T          PREV_OCUPADO        return posicion x
    #T          _MapEntry           next iter x
    #F          VACIO               return None x
    #F          PREV_OCUPADO        next iter x
    #F          _MapEntry           compare key x
    
    def _findPosition(self, key, insert): #insert:bool-> to insert or not to?
        posicion=self._hash1(key)
        paso=self._hash2(key) 
        
        M=len(self._tabla)

        while self._tabla[posicion] is not self.VACIO:
            if insert\
                and self._tabla[posicion] is self.PREV_OCUPADO:
                return posicion #INSERTAR Y PREV_OCUPADO
            elif not insert\
                and self._tabla[posicion] is not self.PREV_OCUPADO and self._tabla[posicion].key==key:
                return posicion #NO INSERTAR Y MAPENTRY
            else:
                #Modified Linear Probing
                posicion=(posicion+paso)%M #NO INSERTAR Y NO PREV_OCUPADO
        
        if insert and self._tabla[posicion] is self.VACIO:
            return posicion #INSERTAR Y VACIO
        
        return #NO INSERTAR Y VACIO
    
    
    def add(self, key, value):
        if key in self:
            posicion=self._findPosition(key, False)
            self._tabla[posicion].value=value
            return False 
        else:
            posicion=self._findPosition(key, True)
            self._tabla[posicion]=_MapEntry(key, value)
            self._conteo+=1
            if self._conteo==self._maxConteo:
                self._rehash()
            return True
        
        
    def _hash1(self, key):
        return abs(hash(key)%len(self._tabla))
    
    def _hash2(self, key): #en mod linear proving se llamará "función de sondeo" f(self, original_slot)
        return 1+abs(hash(key))%(len(self._tabla)-2)
    
    def _rehash(self):
        tabla_original=self._tabla
        new_len=len(self._tabla)*2+1
        self._tabla=Array(new_len)
        
        self._conteo=0
        self._maxConteo=new_len-(new_len//4)
        
        for entry in tabla_original:
            if entry is not self.VACIO or entry is not self.PREV_OCUPADO:
                posicion=self._findPosition(entry.key, True)
                self._tabla[posicion]=entry
                self.conteo+=1
                        
    def valueOf(self, key):
        posicion=self._findPosition(key, False)
        assert posicion is not None, "Llave inválida"
        return self._tabla[posicion].value
        
    def remove(self, key):
        posicion=self._findPosition(key, False)
        assert self._tabla[posicion].value is not (self.VACIO or self.PREV_OCUPADO), "Llave Invalida"
        self._tabla[posicion].value=self.PREV_OCUPADO
    
    def __iter__(self):
        return _HashMapIterator(self._tabla)
         
        
class _HashMapIterator:
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
