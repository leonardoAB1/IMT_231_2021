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

fibonacci(6)
