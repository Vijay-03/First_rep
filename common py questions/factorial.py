def factorial(n):
    # n! can also be defined as n * (n-1)
    """" calculates n! recursively"""
    if n <= 1:
        return 1
    else:
        return n * factorial(n-1)


# print(factorial(5))
try:
    print(factorial(1000))
except RecursionError:
    print("This program can't calculate factirals that large")

print("Program terminating")
