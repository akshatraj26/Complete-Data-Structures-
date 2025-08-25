# Searching Algorithms :- Binary Search

# Time Complexity O(logn)
# Space Complexity O(1)
def binary_search(array, value):
    l = 0
    r = len(array) - 1
    middle = (l + r) // 2

    while l <= r:
        if value == array[middle]:
            return middle
        elif value < array[middle]:
            r = middle - 1
        else:
            l = middle + 1

    return -1


arr =  [4,6,7,32,5,8,9,3,2]

print(binary_search(arr, 5))
