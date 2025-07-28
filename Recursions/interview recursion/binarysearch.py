arr  = [23,45,78,89, 99]

def binary_search(data,left, right, item):
    if left <= right:
        mid = (left+right) // 2
        if item == data[mid]:
            return mid
        elif item < data[mid]:
            return binary_search(data, left, mid-1, item)
        else:
            return binary_search(data, mid+1, right, item)

    else:
        return -1



# index of the item
binary = binary_search(arr, 0, len(arr)-1, item=90)
print(binary)
