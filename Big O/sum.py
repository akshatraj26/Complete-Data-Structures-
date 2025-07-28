def sum_f(n):
    if n <= 0:
        return 0
    else:
        print(n)
        return n + sum_f(n-1)

print(sum_f(12))