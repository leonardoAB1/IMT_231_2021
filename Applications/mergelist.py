listaA=[2,8,15,23,37]
listaB=[4,6,15,20]

#Opcion 1
#[2,8,15,23,37,4,6,15,20] O(n^2)

#Opcion 2
#[2,8,15,23,37,4] O(n^3)

#Opcion 3
#Aprovechar lo que está hecho, en caso de que esten ordenadas
#Comparar y agregar a lista

def mergeSortedLists(listaA, listaB):
    nuevaLista=list()
    indexA=0
    indexB=0
    
    while indexA < len(listaA) and indexB<len(listaB):
        if listaA[indexA]<listaB[indexB]:
            nuevaLista.append(listaA[indexA])
        else:
            nuevaLista.append(listaB[indexB])
            indexB+=1
            
    while indexA< len(listaA):
        nuevaLista.append(listaA[indexA])
        indexA+=1
        
    while indexB < len(listaB):
        nuevaLista.append(listaB[indexB])
        indexB+=1
        
    return nuevaLista

nuevaLista=mergeSortedLists(listaA, listaB)
print(nuevaLista)
