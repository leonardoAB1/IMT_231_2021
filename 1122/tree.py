class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.izquierda = None
        self.derecha = None


raiz = BinaryTreeNode('T')
raiz.izquierda = BinaryTreeNode('X')
raiz.derecha = BinaryTreeNode('C')
raiz.derecha.izquierda = BinaryTreeNode('J')
raiz.derecha.derecha = BinaryTreeNode('R')
raiz.izquierda.izquierda = BinaryTreeNode('B')
raiz.izquierda.derecha = BinaryTreeNode('G')
raiz.izquierda.derecha.izquierda = BinaryTreeNode('Z')
raiz.derecha.derecha.derecha = BinaryTreeNode('M')
raiz.derecha.derecha.izquierda = BinaryTreeNode('K')



#              T
#       X            C
# B          G  J           R
#        Z             K         M

# RECORRIDOS // TRAVERSALS

# Depth first traversals

# Preorder - Raiz primero, luego hijos
def preorder(raiz):
    if raiz is not None:
        print(raiz.data)
        preorder(raiz.izquierda)
        preorder(raiz.derecha)

# preorder(raiz) # T -> X -> B -> G -> Z -> C -> J -> R -> K -> M


# In order - Izquierda, raíz, derecha
def inorder(raiz):
    if raiz is not None:
        inorder(raiz.izquierda)
        print(raiz.data)
        inorder(raiz.derecha)

# inorder(raiz)  # B -> X -> Z -> G -> T -> J -> C -> K -> R - M

# Post order - Primero hijos, luego raíz
def postorder(raiz):
    if raiz is not None:
        postorder(raiz.izquierda)
        postorder(raiz.derecha)
        print(raiz.data)

# postorder(raiz) # B -> Z -> G -> X -> J -> K -> M -> R -> C -> T

# Breadth first traversal

# si el queue no esta vacio
#   extraemos el nodo
#   si el nodo tiene hijos
#       los agregamos al queue
#   imprimimos el nodo

from QueueLinked import Queue

def breadthFirstTraversal(raiz):
    if raiz is not None:
        q = Queue()
        q.enqueue(raiz)

        while not q.isEmpty():
            nodo_actual = q.dequeue()
            if nodo_actual.izquierda is not None:
                q.enqueue(nodo_actual.izquierda)
            if nodo_actual.derecha is not None:
                q.enqueue(nodo_actual.derecha)
            print(nodo_actual.data)

breadthFirstTraversal(raiz) # T -> X -> C -> B -> G -> J -> R -> Z -> K -> M