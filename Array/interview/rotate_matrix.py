array = [[1, 2,3], [4,5,6], [7,8,9]]


print(array)
def rotateMatrix(matrix):
    n = len(matrix)
    for layer in range(n//2):
        first = layer # 0
        last = n - layer - 1 # 1
        for i in range(first, last):
            # save top element
            top = matrix[layer][i]
            # move left element to top
            matrix[layer][i] = matrix[-i-1][layer]
            # move bottom element to left
            matrix[-i-1][layer] = matrix[-layer-1][-i-1]
            # move right to bottom
            matrix[-layer-1][-i-1] = matrix[i][-layer-1]
            # move top to right
            matrix[i][-layer-1] = top
        return matrix
print(rotateMatrix(array))
#
# n = len(array)
# print(n)
# for layer in range(n//2):
#     first = layer
#     last = n - layer - 1
#     # print(f"first:- {first}, layer:- {layer}  last = {last} :- { n- layer - 1}")
#     for i in range(first, last):
#         print(f"i {i}")
#         print("-"*100)
#         top = array[layer][i]
#         print(f"{top}")
#         print(array[-i-1][layer])
#         print(array[-layer-1][-i-1])
#         print(array[i][-layer-1])
#         # break
#         top = array[layer][i]
#         array[-i-1][layer] =array[-layer-1][-i-1]
#         array[-layer-1][-i-1] = array[i][-layer-1]
#
#

# print(len(array)//2)