def capitalizeWord(arr):
    result = []
    if len(arr) == 0:
        return result
    result.append(arr[0].upper())
    return result + capitalizeWord(arr[1:])






arr = ['i', "am", 'into', 'mature']

print(capitalizeWord(arr))

print(arr)
# arr = [element.upper() for element in arr]
# print(arr)