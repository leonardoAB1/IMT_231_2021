from QueueLinked import Queue

class _ExpTreeNode:
    def __init__(self, data):
        self.data = data
        self.izquierda = None
        self.derecha = None

class ExpressionTree:
    def __init__(self, expresion): # 5
        self._expTree = None # _ExpTreeNode()
        self._construirArbol(expresion)

    def __str__(self):
        return self._construirString(self._expTree)

    def toString(self):
        print(self._construirString(self._expTree))

    def eval(self, varsDict=dict()): # exp1.eval({"a": 5, "b": 8})
        return self._evaluarArbol(self._expTree, varsDict)

    def _construirArbol(self, expresion):
        expQ = Queue()
        for caracter in expresion:
            expQ.enqueue(caracter)

        self._expTree = _ExpTreeNode(None)
        self._recConstruirArbol(self._expTree, expQ)

    def _recConstruirArbol(self, nodo_actual, queue):
        caracter = queue.dequeue() # (8*5)
        if caracter == "(":
            nodo_actual.izquierda = _ExpTreeNode(None)
            self._recConstruirArbol(nodo_actual.izquierda, queue)

            nodo_actual.data = queue.dequeue()
            nodo_actual.derecha = _ExpTreeNode(None)
            self._recConstruirArbol(nodo_actual.derecha, queue)
            queue.dequeue() # ")"
        else:
            nodo_actual.data = caracter

    def _evaluarArbol(self, subarbol, varsDict=dict()):
        # Si el nodo es hoja, retornar el valor numerico
        if subarbol.izquierda is None and subarbol.derecha is None:
            # el operando es de un digito?
            if subarbol.data >= "0" and subarbol.data <= "9":
                return int(subarbol.data)
            else:
                assert subarbol.data in varsDict, "Variable inválida"
                return varsDict[subarbol.data]

        # Si no es una hoja, hay que computar el operador
        else:
            valor_izquierda = self._evaluarArbol(subarbol.izquierda, varsDict)
            valor_derecha = self._evaluarArbol(subarbol.derecha, varsDict)
            return self._computarOp(valor_izquierda, subarbol.data, valor_derecha)
            
    def _computarOp(self, izquierda, operador, derecha):
        if operador == "+":
            return izquierda + derecha
        elif operador == "-":
            return izquierda - derecha
        elif operador == "*":
            return izquierda * derecha
        elif operador == "/":
            return izquierda / derecha
        elif operador == "%":
            return izquierda % derecha
        else:
            raise Exception("Operador invalido")

    def _construirString(self, raiz):
        # si el nodo es hoja, es operando
        if raiz.izquierda is None and raiz.derecha is None:
            return str(raiz.data)
        else:
            strExpr = "("
            strExpr += self._construirString(raiz.izquierda)
            strExpr += str(raiz.data)
            strExpr += self._construirString(raiz.derecha)
            strExpr += ")"
            return strExpr


# 8*5+9/(7-4)

#           +
#     *           /
#   8    5     9     -
#                  7   4

# 8 5 * 9 7 4 - / +  postfix notation
# 8 * 5 + 9 / 7 - 4  infix notation
# ((8*5)+(9/(7-4)))
# NODO ACTUAL
#       x='*'   RAIZ
#  y=8      z=5



exp = '((8*5)+(9/(7-4)))'
exp_tree = ExpressionTree(exp)
exp_tree.toString()
print(exp_tree.eval())

exp_2 = '((x*5)+(9/(y-4)))'
exp_tree_2 = ExpressionTree(exp_2)
exp_tree_2.toString()
print(exp_tree_2.eval({'x':8, 'y':7}))


