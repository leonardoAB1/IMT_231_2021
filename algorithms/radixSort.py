from Arrays import Array
from QueueLinked import Queue

def radix_sort(collection, digit_number): #O(n)*O(m); Requiere n espacios de memoria
    bins=Array(10)
    for k in range(10): #O(k)
        bins[k]=Queue()
            
    column=1
    
    for digit in range(digit_number): # O(m)
        for element in collection: #O(n)
            digit=(element//column)%10
            bins[digit].enqueue(element) #encolar
            
        i=0
        for bin in bins: #Este for loop es constante O(1) ya que depende del nro de canastas y estas son constantes ->O(n)
            while not bin.isEmpty(): #O(n); En el peor de los casos, todos los elemento estarian en una misma canasta
                collection[i]=bin.dequeue()
                i+=1
            
        column*=10 #discriminar entre unidades descenas, centenas, etc
    
if __name__=="__main__":
    lista=[10,23,51,18,4,31,13,5,48,62,29]
    print(lista)
    radix_sort(lista, 2)
    print(lista)