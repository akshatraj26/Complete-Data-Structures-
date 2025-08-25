
arr =  [4,6,7,32,5,8,9,3,2]


# Searching Algorithms :- Linear Search
# Time Complexity O(n)
# Space Complexity O(1)
def linear_search(array, value):
    for i in range(len(arr)):
        if array[i] == value:
            return i
    return -1






print(linear_search(arr, 23))

print("Binary Search")

