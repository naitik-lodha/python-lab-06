import math


def factorial(n):
    return math.factorial(n)


def fibonacci(n):
    n1 = 0
    n2 = 1
    print(n1)
    print(n2)
    for i in range(n - 2):
        n3 = n1 + n2
        print(n3)
        n1 = n2
        n2 = n3
