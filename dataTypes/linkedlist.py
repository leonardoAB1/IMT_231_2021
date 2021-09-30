#Single linked list

class Node:
    def __init__(self, data):
        self.data=data
        self.next=None

# Una lista enlazada es una colección de objetos, llamados nodos,
# que contienen datos y almenos una referencia al siguiente nodo,
# llamada ENLACE. En el caso particular de una lista enlazada, 
# los enlaces son lineales

# ptr=null

a=Node(35)
b=Node(52)
c=Node(73)

a.next=b
b.next=c

print(a.data)
print(a.next.data)
print(a.next.next.data)

#Doubly linked list




#Circular linked list




