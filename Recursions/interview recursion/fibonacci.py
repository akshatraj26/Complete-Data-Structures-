
def fibonnaci(num):
    if num < 2:
        return num
    return fibonnaci(num - 1) + fibonnaci(num - 2)

for i in range(10):
    print(fibonnaci(i))