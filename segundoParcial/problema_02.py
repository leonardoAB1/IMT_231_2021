#Diseñe e implemente un tipo de dato abstracto llamado Checklist en el que 
#cada task tenga una prioridad, y los ítems con prioridad mayor son mostrados 
#primero.

from PriorityQueue import PriorityQueue

class Checklist(PriorityQueue):
    """
    A list of tasks that need to be completed, 
    typically organized in order of priority.
    In this class, priority is set from lowest to highest
    Same priority task are sorted by precedence.
    
    >>> my_list=Checklist()
    >>> my_list.add_new_task("Jugar fútbol", 5)
    >>> my_list.add_new_task("Completar el examen", 1)
    >>> my_list.add_new_task("Estudiar", 3)
    >>> my_list.add_new_task("Almorzar", 0)
    >>> my_list.add_new_task("Avanzar con el proyecto", 1)
    >>> my_list.add_new_task("Jugar video juegos", 5)
    >>> my_list.add_new_task("Jugar en la piscina", 9)
    >>> my_list.show_tasks()
    1. Almorzar
    2. Completar el examen
    3. Avanzar con el proyecto
    4. Estudiar
    5. Jugar fútbol
    6. Jugar video juegos
    7. Jugar en la piscina
    >>> my_list.dequeue()
    'Almorzar'

    """
    
    def __init__(self):
        super().__init__()

    def add_new_task(self, e, p):
        self.enqueue(e, p)
    
    def __str__(self):
        string=""
        i=1
        tmp=self._qLista.copy()
        while not self.isEmpty():
            string+=f"{i}. {self.dequeue()}\n"
            i+=1
        self._qLista=tmp
        return string[:-1]
            
    def show_tasks(self):
        """Muestra una lista numerada de 
        las tareas almacenadas en la check-list"""
        print(self)


if __name__=="__main__":
    import doctest
    doctest.testmod(verbose=True)