# hashable = int, float, str, tuple, None
# no hashable = list, dict, set

from Arrays import Array

class _MapEntry:
    def __init__(self, key, value):
        self.key = key
        self.value = value

class HashMap:
    VACIO = None
    PREV_OCUPADO = _MapEntry(None, None)

    def __init__(self):
        self._tabla = Array(7)
        self._conteo = 0
        self._maxConteo = len(self._tabla) - (len(self._tabla) // 4)

    def __len__(self):
        return self._conteo

    def __contains__(self, key):
        posicion = self._buscarPosicion(key, False)
        return posicion is not None

    def add(self, key, value):
        if key in self:
            posicion = self._buscarPosicion(key, False)
            self._tabla[posicion].value = value
            return False
        else:
            posicion = self._buscarPosicion(key, True)
            self._tabla[posicion] = _MapEntry(key, value)
            self._conteo += 1
            if self._conteo == self._maxConteo:
                self._rehash()
            return True

# INSERTAR  tabla[posicion]
# V         VACIO           return posicion X
# V         PREV_OCUPADO    return posicion X
# V         _MapEntry       next iter X
# F         VACIO           return None X
# F         PREV_OCUPADO    next iter X
# F         _MapEntry       compare key X

    def _buscarPosicion(self, key, insertar):
        posicion = self._hash1(key)
        paso = self._hash2(key)

        M = len(self._tabla)

        while self._tabla[posicion] is not self.VACIO:
                if insertar \
                    and self._tabla[posicion] is self.PREV_OCUPADO:
                    return posicion # INSERTAR Y PREV_OCUPADO
                elif not insertar \
                    and self._tabla[posicion] is not self.PREV_OCUPADO and self._tabla[posicion].key == key:
                    return posicion # NO INSERTAR Y MAPENTRY
                else:
                    posicion = (posicion + paso) % M # NO INSERTAR Y NO PREV_OCUPADO, INSERTAR Y NO PREV_OCUPADO

        if insertar and self._tabla[posicion] is self.VACIO:
            return posicion # INSERTAR Y VACIO

        return None # NO INSERTAR Y VACIO

        # if not insertar:
        #     while self._tabla[posicion] is not self.VACIO:
        #         if self._tabla[posicion] is not self.PREV_OCUPADO and self._tabla[posicion].key == key:
        #             return posicion # not insertar y _MapEntry.key == key
        #         else:
        #             posicion = (posicion + paso) % M # not insertar y PREV_OCUPADO o not insertar y _MapEntry.key != key
        #     return None # not insertar y VACIO
        # else:
        #     while self._tabla[posicion] is not self.VACIO and self._tabla[posicion] is not self.PREV_OCUPADO:
        #         posicion = (posicion + paso) % M # insertar y _MapEntry
        #     return posicion # insertar y VACIO o insertar y PREV_OCUPADO

    def _hash1(self, key):
        return abs(hash(key)) % len(self._tabla)

    def _hash2(self, key):
        return 1 + abs(hash(key)) % (len(self._tabla) - 2)

    def _rehash(self):
        tabla_original = self._tabla
        nuevo_len = len(self._tabla) * 2 + 1
        self._tabla = Array(nuevo_len)

        self._conteo = 0
        self._maxConteo = nuevo_len - (nuevo_len // 4)

        for entry in tabla_original:
            if entry is not self.VACIO or entry is not self.PREV_OCUPADO:
                posicion = self._buscarPosicion(entry.key, True)
                self._tabla[posicion] = entry
                self._conteo += 1

    def valueOf(self, key):
        posicion = self._buscarPosicion(key, False)
        assert posicion is not None, "Llave inválida"
        return self._tabla[posicion].value

    def remove(self, key): # 1. Implementar metodo remove
        pass

    def __iter__(self): # 2. Implementar un iterador
        pass

    # 3. Modificar la implementación para usar sondeo lineal modificado
    #    en lugar de double hashing


d = HashMap()
d.add(1, 'hola')
d.valueOf(1)
d.add(8, 'mundo')
d.valueOf(8)
d.valueOf(43)