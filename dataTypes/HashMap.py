# hashable= int, float, str, tuple, None
# no hasheable= list, dict, set

from Arrays import Array

class HashMap:
    PREV_OCUPADO=None
    VACIO=_MapEntry(None, None)
    
    def __init__(self):
        self._tabla=Array(7)
        self._conteo=0
        self._maxConteo=len(self._tabla)-len(self._tabla)//4
        
    def __len__(self):
        return conteo
    
    def __contains__(self, key):
        posicion=self._findPosition(key, False)
        return posicion is not None
    
    def _findPosition(self, key, insert):
        posicion=self._hash1(key)
        paso=self.hash2(key)
        
        M=len(self._tabla)
        
        while self.tabla[posicion] is self.VACIO or self._tabla[posicion] is self.PREV_OCUPADO:
            if insert:
                return posicion
            elif not insert:
                if self._tabla[posicion] is not self.VACIO and self._tabla[posicion].key==key:
                    return  posicion
                elif self._tabla[posicion] is self.VACIO: 
                    return 
            else:
                #Modified Linear Probing
                posicion=(posicion+paso)%M
             
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
    
    def _hash2(self, key):
        return 1+abs(hash(key))%(len(self._tabla)-2)
    
    def _rehash(self):
        tabla_original=self._tabla
        nuevo_len=len(self._tabla)*2+1
        self._tabla=Array(nuevo_len)
        
        self._conteo=0
        self._maxConteo=nuevo_len-nuevo_len//4
        
        for entry in tabla_original:
            if entry is not self.VACIO or entry is not self.PREV_OCUPADO:
                posicion=self._findPosition(entry.key, True)
                self._tabla[posicion]=entry
                self.conteo+=1
                        
    def valueOf(self, key):
        posicion=self._buscarPosicion(key, False)
        assert posicion is not None, "Llave inválida"
        return self._tabla[posicion].value
        
    def remove(self, key):
        ix=self._findPosition(key)
        assert ix is not None, "Llave Invalida"
        self._listaEntries.pop(ix)
        
class _MapEntry:
    def __init__(self, key, value):
        self.key=key
        self.value=value
        
if __name__=="__main__":
    d=HashMap()
    d.add(1, "hola")