def sumOfDigits(n):
    assert n>= 0 and int(n) == n, "The number must be positive number"
    if n == 0:
        return 0
    else:
        return n%10 + sumOfDigits(n//10)


print(sumOfDigits(54))
print(3//10, 3%10)