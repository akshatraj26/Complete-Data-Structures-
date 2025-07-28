"""
Decimal to binary
12

12/2  6 remainder 0
6/2   3 remainder 0
3/2   1 remiander 1
1/2   0 remainder 1

f(n%2)
f(n)  = n mod 2 + 10 * f(n/2)
"""

print(1%2)

def decimalToBinary(n):
    assert  int(n) == n, "The Number should be an Integer only."
    if n  == 0:
        return 0
    else:
        print(n)
        return n % 2 + 10 * decimalToBinary(int(n/2))

print(decimalToBinary(12))
