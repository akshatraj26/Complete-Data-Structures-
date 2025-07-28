def ASCII_Hash(string, cellNumber):
    total = 0
    total = list((ord(i) for i in string))
    return total

print(ASCII_Hash("Abhinay", 32))

def ASCII_Hash(string, cellNumber):
    total = 0
    for i in string:
        total += ord(i)
    return total % cellNumber

print(ASCII_Hash("Abhinay", 32))