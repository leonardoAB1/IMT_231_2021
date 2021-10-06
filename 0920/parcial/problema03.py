"""
Problema 3
Escriba una función llamada es_1_a_1 que acepte un diccionario cuyas llaves y valores son strings y 
retorne True si no hay dos llaves que estén mapeadas al mismo valor. 
Por ejemplo, para el siguiente diccionario tu función debería retornar False porque "Hawking" y "Newton" mapean al mismo valor:
{"Marty": "206-9024",
"Hawking": "123-4567",
"Smith": "949-0504",
"Newton": "123-4567"}

Pero para el siguiente diccionario debe retornar True porque cada llave está mapeada a un valor único:
{"Marty": "206-9024",
"Hawking": "555-1234",
"Smith": "949-0504",
"Newton": "123-4567"}

Un diccionario vacío es considerado 1-a-1 y retorna True.
"""

#Solucion:
#Como las llaves son unicas por definicion, solo se debe chequear si los valores se repiten
#En otras palabras, si el tamaño set de los valores será diferente de un set de llaves(recordemos que en los sets los elementos son unicos).s

def es_1_a_1(dictionary: dict)->bool:
    """
    >>> es_1_a_1({"Marty": "206-9024","Hawking": "123-4567","Smith": "949-0504","Newton": "123-4567"})
    False
    >>> es_1_a_1({"Marty": "206-9024","Hawking": "555-1234","Smith": "949-0504","Newton": "123-4567"})
    True
    """
    return len(set(dictionary.keys()))==len(set(dictionary.values()))

if __name__=="__main__":
    import doctest
    doctest.testmod(verbose=True)
    
