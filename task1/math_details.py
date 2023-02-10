# Can also use builtin math functions for permutation combination and factorial
def permutation(n, r):
    return factorial(n) // factorial(n - r)


def combination(n, r):
    return factorial(n) // (factorial(r) * factorial(n - r))


def factorial(n):
    product = 1
    for i in range(1, n + 1):
        product = product * i
    return product


def armstrong(n):
    temp = str(n)
    sums = 0
    while n > 0:
        rem = n % 10
        sums = sums + (rem ** len(temp))
        n = n // 10
    n = int(temp)
    if n == sums:
        return "Armstrong"
    return "Not Armstrong"


def reverse(n):
    sums = 0
    while n > 0:
        rem = n % 10
        sums = sums * 10 + rem
        n = n // 10
    return sums
