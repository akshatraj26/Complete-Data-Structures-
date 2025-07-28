def f(n):
    if n<= 1:
        return 1
    return f(n-1) + f(n-1)

c = f(34)
print(c)