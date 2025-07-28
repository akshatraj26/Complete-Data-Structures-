import numpy as np

twoDArray = np.array([[11,15,10,6], [10, 14,11,5], [12,17,12,8], [15,18,14, 9]])

print(twoDArray)

# print(twoDArray.diagonal())

# Add as a column
newtwoDArray = np.insert(twoDArray,0, [[3, 6, 9,4]], axis=1)
# print(newtwoDArray)


# Add as a row
# np.insert(two2Array, row, values, axis = 0)
newtwoDArray = np.insert(twoDArray,0, [[3, 6, 9,4]], axis=0)
# print(newtwoDArray)


newtwoDArray = np.append(twoDArray, [[3, 6, 9,4]], axis = 0)
# print(newtwoDArray)


def accessElements(array, rowIndex, colIndex):
    l = len(array)
    if colIndex >= len(array[0]) and rowIndex >= l:
        print("Wrong index")
    else:
        print(array[rowIndex][colIndex])


# accessElements(twoDArray, 1,2)

def traversing2DArray(twoDArray):
    for row in range(len(twoDArray)):
        for col in range(len(twoDArray[0])):
            print(twoDArray[row][col])
        print("-"*20)

def search2DArray(array, target):
    for row in range(len(array)):
        for col in range(len(array[0])):
            if target == array[row][col]:
                return f"The values is located at {row}, {col}"
    return "The element is Not available"

print(search2DArray(twoDArray, 100))

new_array = np.delete(twoDArray, 2, axis = 0)

print(new_array)


