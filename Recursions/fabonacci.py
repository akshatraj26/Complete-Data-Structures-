num = [0, 1]
# 0,1 1, 2, 3, 5, 8, 13, 21, 34, 55, 89,
def fibonacci(n):
    assert n >= 0 and int(n) == n, "The number must be positive integer"
    if n in num:
        return n
    else:
        #print(n, end='-')
        return fibonacci(n-1) + fibonacci(n-2)

fibonacci(6)

for i in range(10):
    print(fibonacci(i), end=" ")