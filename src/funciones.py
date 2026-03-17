def suma(a, b):
    return a+b

def factorial(n):
    if n < 0:
        raise ValueError("No definido para negativos")
    if n == 0:
        return 1
    return n * factorial(n - 1)

def combinatoria(n, k):
    if k > n:
        return 0
    from math import factorial
    return factorial(n) // (factorial(k) * factorial(n - k))