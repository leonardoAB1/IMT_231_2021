# hashable= int, float, str, tuple, None
# no hasheable= list, dict, set

from Arrays import Array

class _MapEntry:
    def __init__(self, key, value):
        self.key=key
        self.value=value

class HashMap:
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
    
    #INSERTAR _tabla[posicion]
    #T          VACIO               return posicion x
    #T          PREV_OCUPADO        return posicion x
    #T          _MapEntry           next iter x
    #F          VACIO               return None x
    #F          PREV_OCUPADO        next iter x
    #F          _MapEntry           compare key x
    
    def _findPosition(self, key, insert): #insert:bool-> to insert or not to?
        posicion=self._hash1(key)
        paso=self._hash2(key) #posicion nueva en función de la llave, en mod linear proving está en función de la posicion original
        
        M=len(self._tabla)
        #opcion mas probable

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
        
    def remove(self, key): #1 Implementar metodo remove
        pass
    
    def __iter__(self): #2 Implementar iterador
        pass
        
    #3. Modificar la  implmentación para usar sondeo lineal modificado en lugar de double hashing    
        
if __name__=="__main__":
    d=HashMap()
    d.add(1, "hola")
    print(d.valueOf(1))
    d.add(8, "mundo")
    print(d.valueOf(8))
    #d.valueOf(43)