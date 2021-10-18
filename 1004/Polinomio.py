class Polinomio:
    def __init__(self, grado=None, coeficiente=None):
        if grado is None:
            self._polyHead = None
        else:
            self._polyHead = _PolyTermNode(grado, coeficiente)
        self._polyTail = self._polyHead

    def grado(self):
        if self._polyHead is None:
            return -1
        else:
            return self._polyHead.grado
    
    def __getitem__(self, grado):
        assert self.grado() >= 0, "Operación no permitida en un polinomio sin términos"
        nodo_actual = self._polyHead
        while nodo_actual is not None and nodo_actual.grado > grado:
            nodo_actual = nodo_actual.next
        
        if nodo_actual is None or nodo_actual.grado != grado:
            return 0.0
        else:
            return nodo_actual.coeficiente

    def evaluar(self, x):
        assert self.grado() >= 0, "Sólo se pueden evaluar polinomios con términos"
        resultado = 0.0
        nodo_actual = self._polyHead
        while nodo_actual is not None:
            resultado += nodo_actual.coeficiente*(x**nodo_actual.grado)
            nodo_actual = nodo_actual.next
        return resultado

    def _agregarTermino(self, grado, coeficiente):
        if coeficiente != 0:
            nuevoTermino = _PolyTermNode(grado, coeficiente)
            if self._polyHead is None:
                self._polyHead = nuevoTermino
            else:
                self._polyTail.next = nuevoTermino
            self._polyTail = nuevoTermino

    def __add__(self, rhsPoli):
        assert self.grado() >= 0 and rhsPoli.grado() >= 0, "La suma es sólo permitida entre polinomios con términos"
        nuevoPoli = Polinomio()
        nodoA = self._polyHead
        nodoB = rhsPoli._polyHead


        while nodoA is not None and nodoB is not None:
            if nodoA.grado > nodoB.grado:
                grado = nodoA.grado
                coeficiente = nodoA.coeficiente
                nodoA = nodoA.next
            elif nodoA.grado < nodoB.grado:
                grado = nodoB.grado
                coeficiente = nodoB.coeficiente
                nodoB = nodoB.next
            else:
                grado = nodoA.grado
                coeficiente = nodoA.coeficiente + nodoB.coeficiente
                nodoA = nodoA.next
                nodoB = nodoB.next
            nuevoPoli._agregarTermino(grado, coeficiente)

        while nodoA is not None:
            nuevoPoli._agregarTermino(nodoA.grado, nodoA.coeficiente)
            nodoA = nodoA.next

        while nodoB is not None:
            nuevoPoli._agregarTermino(nodoB.grado, nodoB.coeficiente)
            nodoB = nodoB.next

        return nuevoPoli

class _PolyTermNode:
    def __init__(self, grado, coeficiente):
        self.grado = grado
        self.coeficiente = coeficiente
        self.next = None

# poly = Polinomio(3, 5)
# poly._agregarTermino(2, 3)
# print(poly[3])