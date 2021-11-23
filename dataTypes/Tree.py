class BinaryTreeNode:
    def __init__(self, data):
        self.data=data
        self.left=None
        self.right=None
        
root=BinaryTreeNode("T")
root.left=BinaryTreeNode("X")
root.right=BinaryTreeNode("C")
root.right.left=BinaryTreeNode("J")
root.right.right=BinaryTreeNode("R")
root.left.left=BinaryTreeNode("B")
root.left.right=BinaryTreeNode("G")
root.left.right.left=BinaryTreeNode("Z")
root.right.right.right=BinaryTreeNode("M")
root.right.right.left=BinaryTreeNode("K")

#Preorder - Raiz primero, luego hijos
#Desde arriba a abajo
def preorder(root):
    if root is not None:
        print(root.data)
        preorder(root.left)
        preorder(root.right)
        
preorder(root)

#Inorder - Izquierda, raiz, derecha
def inorder(root):
    if root is not None:
        inorder(root.left)
        print(root.data)
        inorder(root.right)
print()
inorder(root)
      
#Post Order - Primero hijos, luego raiz
#Desde abajo hasta arriba
def postorder(root):
    if root is not None:
        postorder(root.left)
        postorder(root.right)
        print(root.data)
        
print()
postorder(root)