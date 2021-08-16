# class Vector {

#     Vector Vector(int n) {

#     }

#     Vector Vector(int n, int valor) {

#     }
# }

# int nombreFuncion(int args) {
#     return variable # TIENE QUE SER DEL TIPO INT
# }

# class MiClase:
#     def __init__(self, valor):
#         self.valor = valor

#     def printInfo(self):
#         print(f'Valor: {self.valor}')
#         print(f'self: {self}')
#         print(f'Direccion: {hex(id(self))}')

# for (int i=0; i<=size; i++) {

# }

# for element in vector {

# }




class Vector(object):
    def __init__(self, n=0, x=None):
        self._data = list()
        if n >= 0:
            self._data = [x for i in range(n)]
        #     for i in range(n):
        #         self._data.append(x)
        else:
            raise Exception("Número inválido de elementos")

    def __repr__(self): # v1 == v1.__repr__()
        return str(self._data)

    def __str__(self): # print(v1) == v1.__str__()
        return f'Contenido: {str(self._data)}'

    def add(self, n):
        self._data.append(n)
    
    def insert(self, i, n):
        self._data.insert(i, n)

    def remove(n):
        pass

    def get(i):
        pass

    def set(i, n):
        pass

    def size():
        pass

    def isEmpty():
        pass

    def clear():
        pass
