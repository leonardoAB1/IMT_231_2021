def imprimirReverso(n):
    if n > 0:
        print(n)
        imprimirReverso(n-1)

# imprimirReverso(5)

def imprimirInc(n):
    if n > 0:
        imprimirInc(n-1)
        print(n)

# imprimirInc(5)

def factorial(n):
    assert n >= 0, "Factorial no está definido para números negativos"
    if n < 2:
        return 1
    else: # 2! = 2 * 1!
        return n * factorial(n-1)

# factorial(5)


# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...
def fibonacci(n):
    assert n >= 0, "Fibonacci no está definido para números negativos"
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

# fibonacci(6)

def recBinarySearch(objetivo, secuencia, inferior, superior):
    if inferior > superior: # caso base 1
        return False
    else:
        medio = (inferior + superior) // 2
        if secuencia[medio] == objetivo:
            return True # caso base 2
        elif objetivo < secuencia[medio]: # caso recursivo
            return recBinarySearch(objetivo, secuencia, inferior, medio - 1)
        else:
            return recBinarySearch(objetivo, secuencia, medio + 1, superior)

sec1 = [2, 4, 5, 10, 13, 21, 28, 34, 42, 50]
recBinarySearch(42, sec1, 0, len(sec1)-1)

# recBinarySearch(objetivo, secuencia, 0, 9) -> True
    # recBinarySearch(objetivo, secuencia, 5, 9) -> True
        # recBinarySearch(objetivo, secuencia, 8, 9) -> True