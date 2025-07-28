import sys
sys.setrecursionlimit(10000)
def factorial(n):
    assert n >= 0 and int(n) == n, "The number will be whole number"
    if n == 0:
        return  1
    else:
        print(n)
        return n * factorial(n-1)

# def factorial(n):
#     print(n)
#     n * factorial(n-1)
print(factorial(5))