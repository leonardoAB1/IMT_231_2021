from Arrays import Array2D
from StackLinked import Stack

class Laberinto:
    PARED = "*"
    VISITADO = "x"
    SIN_SALIDA = "o"

    def __init__(self, numRows, numCols):
        self._laberinto = Array2D(numRows, numCols)
        self._entrada = None
        self._salida = None

    def numRows(self):
        return self._laberinto.numRows()

    def numCols(self):
        return self._laberinto.numCols()

    def crearPared(self, row, col):
        assert row >= 0 and row < self.numRows() and \
            col >= 0 and col < self.numCols(), "Celda fuera de rango"
        self._laberinto[row, col] = self.PARED

    def crearEntrada(self, row, col):
        assert row >= 0 and row < self.numRows() and \
            col >= 0 and col < self.numCols(), "Celda fuera de rango"
        self._entrada = _PosicionCelda(row, col)

    def crearSalida(self, row, col):
        assert row >= 0 and row < self.numRows() and \
            col >= 0 and col < self.numCols(), "Celda fuera de rango"
        self._salida = _PosicionCelda(row, col)

    def encontrarTrayectoria(self):
        # CREAR STACK
        # EMPEZAR EN LA ENTRADA
        # MARCAR CASILLA ACTUAL COMO VISITADA
        # SI ENCONTRAMOS LA SALIDA
        #    NOS DETENEMOS
        # SINO
        #    INTENTAR MOVERNOS EN UNA DIRECCION VALIDA
        #       SI NO HAY DIRECCION VALIDA, MARCAR COMO SIN SALIDA
        #           HACER POP DEL STACK Y DESHACER LA ULTIMA ACCION
        #       SI HAY DIRECCION VALIDA, LA EMPUJAMOS AL STACK
        #           TRATAMOS DE ENCONTRAR TRAYECTORIA A PARTIR DE LA NUEVA POSICION
        pass

    def reset(self):
        pass

    def dibujar(self):
        pass

    def _esMovidaValida(self, row, col):
        return row >= 0 and row < self.numRows() and \
            col >= 0 and col < self.numCols() and \
            self._laberinto[row, col] is None
    
    def _salidaEncontrada(self, row, col):
        return row == self._salida.row and \
            col == self._salida.col

    def _marcarSinSalida(self, row, col):
        self._laberinto[row, col] = self.SIN_SALIDA

    def _marcarTrayectoria(self, row, col):
        self._laberinto[row, col] = self.VISITADO

    
class _PosicionCelda:
    def __init__(self, row, col):
        self.row = row
        self.col = col
