#Diseñe e implemente una función recursiva para computar el máximo común 
#divisor de dos valores enteros.
#greatest common divisor
def compute_GCD(num_1:int, num_2:int):
    """
    >>> print(compute_GCD(120, 360))
    120
    >>> print(compute_GCD(5, 0))
    5
    >>> print(compute_GCD(12, 5))
    1
    """
    if num_2==0:
        return num_1
    else:
        remainder=num_1%num_2
        return compute_GCD(num_2, remainder)

if __name__=="__main__":
    import doctest
    doctest.testmod(verbose=True)
    