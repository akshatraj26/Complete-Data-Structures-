array = [1,5,8,9,11,13,15,19,21]

find = 2



def binary_search(array, target):
    left = 0
    right = len(array) - 1
    while left <= right:
        mid = (left  + right)//2

        if  array[mid] == target:
            return target
        if array[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1


print(binary_search(array, 4))



         