array = [[1, 2,3], [4,5,6], [7,8,9]]

print(array)
def rotate_matrix_90(matrix):
    n = len(matrix)

    for layer in range(n//2):
        first = layer
        last = n - layer -1
        for i in range(first, last):
            # save the first value in tem variable
            top = matrix[layer][i]
            # print(f"Top element {top}")
            # move the bottom-left to first
            matrix[layer][i] = matrix[-i-1][layer]
            # print(f"Bottom-left element:- {matrix[layer][i]}")
            # move bottom-right element to bottom-left element
            matrix[-i-1][layer] = matrix[-layer-1][-i-1]
            # print(f"Bottom-right element:- {matrix[-i-1][layer]}")
            # move top-right element to bottom-right element
            matrix[-layer-1][-i-1] = matrix[i][-layer-1]
            # move bottom-right element to top-right element
            # print(f"Top-right element:- {matrix[-layer-1][-i-1]}")
            # move first element to top-right element
            matrix[i][-layer-1] = top
            # print(f"Top element:- {matrix[i][-layer-1]}")

        return matrix

print(rotate_matrix_90(array))