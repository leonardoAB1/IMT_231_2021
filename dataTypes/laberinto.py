from Arrays import Array2D
from StackLinked import Stack

class Laberinto:
    PARED="*"
    VISITANDO="x"
    SIN_SALIDA="o"
    
    ARRIBA=(-1,0)
    ABAJO=(1,0)
    DERECHA=(0,1)
    IZQUIERDA=(0,-1)
    
    ACCIONES=[ARRIBA, DERECHA, ABAJO, IZQUIERDA]
    
    def __init__(self, numRows, numCols):
        """
        Crea un nuevo laberinto con todas las celdas inicializadas 
        como abiertas. La entrada y la salida no están definidas.
        """
        self._laberinto=Array2D(numRows, numCols)
        self._entrada=None
        self._salida=None
        
    def numRows(self):
        """Retorna el número de filas en el laberinto"""
        return self._laberinto.numRows()
    
    def numCols(self):
        """Retorna el número de columnas en el laberinto"""
        return self._laberinto.numCols()
    
    def crearPared(self, row, col):
        """
        Rellena la posición indicada por (r, c) con una pared (*). 
        Los índices deben estar dentro del rango válido.
        """
        assert row >= 0 and row < self.numRows() and \
            col >= 0 and col < self.numCols(), "Cell out of range"
        self._laberinto[row, col]=self.PARED
        
    def crearEntrada(self, row, col):
        """
         Asigna la entrada a la posición indicada por (r,c). 
         Los índices deben estar dentro del rango válido
        """
        assert row >= 0 and row < self.numRows() and \
            col >= 0 and col < self.numCols(), "Cell out of range"
        self._entrada=_PosicionCelda(row, col)
        
    def crearSalida(self, row, col):
        """
        Asigna la salida a la posición indicada por (r,c). 
        Los índices deben estar dentro del rango válido.
        """
        assert row >= 0 and row < self.numRows() and \
            col >= 0 and col < self.numCols(), "Cell out of range"
        self._salida=_PosicionCelda(row, col)  
        
    def encontrarTrayectoria(self):
        """
        Intenta resolver una trayectoria empezando desde la entrada hasta 
        encontrar la salida. Si una solución es encontrada la trayectoria 
        es marcada con x y retorna True. Para un laberinto sin solución, 
        retorna False y el laberinto queda en su estado original. 
        El laberinto debe contener una entrada y un salida.
        """
        #CREAR STACK
        trayectoria=Stack()
        #EMPEZAR EN LA ENTRADA
        posicion=self._entrada
        trayectoria.push(posicion)
        while not self._salidaEncontrada(posicion.row, posicion.col):
        #MARCAR CASILLA ACTUAL COMO VISITADA
            self._marcarTrayectoria(posicion.row, posicion.col)
            #SI ENCONTRAMOS LA SALIDA
            if self._salidaEncontrada(posicion.row, posicion.col):
                break
            #   NOS DETENEMOS
            else:
            #   SINO INTENTAR MOVERNOS EN UNA DIRECCION VALIDA
                for direccion in self.ACCIONES:
                    nueva_posicion=_PosicionCelda(posicion.row+direccion[0],posicion.col+direccion[1])
                    if self._esMovidaValida(nueva_posicion.row, nueva_posicion.col):
                        
            #       SI HAY DIRECCIÓN VALIDA, LA EMPUJAMOS AL STACK
                        trayectoria.push(nueva_posicion)
            #           TRATAMOS DE ENCONTRAR LA TRAYECTORIA A PARTIR DE LA NUEVA POSICION
                        posicion=nueva_posicion
                        break
            #       SI NO HAY DIRECCION VALIDA, MARCAR COMO SIN SALIDA, HACER POP DEL STACK Y VOLVER A LA POSICION PREVIA
                    elif  direccion==self.ACCIONES[-1]:
                        self._marcarSinSalida(posicion.row, posicion.col)
                        posicion=trayectoria.pop()

            #   SI TRAS PROBAR LOS CUATRO LADOS SE VUELVE A LA POSICION INICIAL, NO HAY SALIDA
                if posicion==self._entrada:
                    laberinto.reset()
                    return False
                
        self._marcarTrayectoria(posicion.row, posicion.col)
        return True
        
    
    def reset(self):
        """
        Reinicia el laberinto a su estado original quitando 
        cualquier marca realizada durante la operación de trayectoria.
        """
        for i in range(self._laberinto.numRows()):
            for j in range(self._laberinto.numCols()):
                value=self._laberinto[i, j]
                if value!=self.PARED:
                    self._laberinto[i, j]=None
                    
    
    def __str__(self):
        string="| "
        for i in range(self._laberinto.numRows()):
            for j in range(self._laberinto.numCols()):
                value=self._laberinto[i, j]
                if value is None:
                    value="."
                string+=f"{value} "
            string+="|\n| "
        string=string[:-3]
        return string
    
    def dibujar(self):
        """
        Imprime el laberinto en un formato legible usando caracteres 
        para representar paredes y la trayectoria en el laberinto. 
        También se indican la entrada y la salida
        """
        dibujo=f"Entrada:({self._entrada.row}, {self._entrada.col})\nSalida: ({self._salida.row}, {self._salida.col})\n{self}"
        print(dibujo)
    
    def _esMovidaValida(self, row, col):
        return row >= 0 and row < self.numRows() and \
            col >= 0 and col < self.numCols() and \
            self._laberinto[row, col] is None
            
    def _salidaEncontrada(self, row, col):
        return row==self._salida.row and \
            col==self._salida.col
        
    def _marcarSinSalida(self, row, col):
        self._laberinto[row, col]=self.SIN_SALIDA
        
    def _marcarTrayectoria(self, row, col):
        self._laberinto[row, col]=self.VISITANDO
        
        
class _PosicionCelda:
   def __init__(self, row, col):
       self.row=row
       self.col=col
       

def construirLaberinto(archivo):
    contenido = open(archivo, "r")

    nrows, ncols = leerPares(contenido)
    laberinto = Laberinto(nrows, ncols)

    row, col = leerPares(contenido)
    laberinto.crearEntrada(row, col)
    row, col = leerPares(contenido)
    laberinto.crearSalida(row, col)

    for row in range(nrows):
        linea = contenido.readline()
        for col in range(len(linea)):
            if linea[col] == "*":
                laberinto.crearPared(row, col)
    
    contenido.close()
    return laberinto


def leerPares(archivo):
    linea = archivo.readline()
    valR, valC = linea.split()
    return int(valR), int(valC)


if __name__=="__main__":
    laberinto = construirLaberinto("laberinto.txt")
    print("Resolver el siguiente laberinto:")
    laberinto.dibujar()
    if laberinto.encontrarTrayectoria():
        print("Trayectoria encontrada:")
        laberinto.dibujar()
    else:
        print("Trayectoria no encontrada")
    laberinto.reset()
    print("Reset Laberinto:")
    laberinto.dibujar()