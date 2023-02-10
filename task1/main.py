import math_details

n = int(input("Enter n: "))
r = int(input("Enter r: "))
print("Permutation: ", math_details.permutation(n, r))
print("Combination: ", math_details.combination(n, r))
print(f"Factorial of {n}: ", math_details.factorial(n))
print(f"{n} is {math_details.armstrong(n)}")
print(f"Reverse of {n} is: ", math_details.reverse(n))
