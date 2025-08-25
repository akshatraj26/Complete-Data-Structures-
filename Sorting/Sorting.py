import math


# Time Complexity O(n^2)
# Space Complexity O(1)
def bubble_sort(array):
    print("Bubble Sort")
    length = len(array)
    for i in range(length - 1):
        for j in range(length - i -1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]

    return array

# Time Complexity O(n^2)
# Space Complexity O(1)
def selection_sort(array):
    print("Selection Sort")
    length = len(array)
    for i in range(length):
        min_index = i
        for j in range(i+1, length):
            if array[min_index] > array[j]:
                min_index = j
        array[min_index], array[i] = array[i], array[min_index]
    return array


# Time Complexity O(n^2)
# Space Complexity O(1)
def insertion_sort(custom_array):
    n = len(custom_array)
    for i in range(n):
        key = custom_array[i]
        j = i - 1
        while j >= 0 and key < custom_array[j]:
            custom_array[j+1]= custom_array[j]
            j  = j - 1
        custom_array[j+1] = key

    return custom_array


# Time Complexity O(n^2)
# Space Complexity O(n)
def bucket_sort(custom_array):
    print("Bucket Sort")
    n = len(custom_array)
    number_of_buckets = round(math.sqrt(n))
    max_value = max(custom_array)
    arr = []

    for i in range(number_of_buckets):
        arr.append([])

    # print(arr)
    for j in custom_array:
        index_b = math.ceil((j * number_of_buckets)/max_value)
        arr[index_b-1].append(j)

    # print(arr)
    for i in range(number_of_buckets):
        arr[i] = insertion_sort(arr[i])

    k = 0
    for i in range(number_of_buckets):
        for j in range(len(arr[i])):
            custom_array[k] = arr[i][j]
            k += 1

    return custom_array


def merge(array, l, m, r):
    n1 = m - l + 1
    n2 = r - m

    L = [0] * n1
    R = [0] * n2

    for i in range(0, n1):
        L[i] = array[l + i]

    for j in range(0, n2):
        R[j] = array[m+1+j]

    i = 0
    j = 0
    k = l

    while i < n1 and j < n2:
        if L[i] <= R[j]:
            array[k] = L[i]
            i += 1
        else:
            array[k] = R[j]
            j += 1
        k += 1

    while i < n1:
        array[k] = L[i]
        i += 1
        k += 1

    while j < n2:
        array[k] = R[j]
        j += 1
        k += 1

# Time Complexity O(nlogn)
# Space Complexity O(n)
def merge_sort(array, l, r):
    if l < r:
        m = (l + (r - 1)) // 2
        merge_sort(array, l, m)
        merge_sort(array, m+1, r)
        merge(array, l, m, r)

    return array

# Helper function for Quick Sort
def partition(array, low, high):
    i = low - 1
    pivot = array[high]
    for j in range(low, high):
        if array[j] <= pivot:
            i += 1
            array[i], array[j] = array[j], array[i]
    array[i+1], array[high] = array[high], array[i+1]
    return i+1

# Time Complexity O(nlog(n)
# SPace Complexity O(n)
def quick_sort(array, low, high):
    if low < high:
        pi = partition(array, low, high)
        quick_sort(array, low, pi-1)
        quick_sort(array, pi+1, high)
    return array


def heapify(array, n, i):
    smallest = i
    l = 2 * i + 1
    r = 2 * i + 2
    if l < n and array[l] < array[smallest]:
        smallest = l
    if r < n and array[r] < array[smallest]:
        smallest = r

    if smallest != i:
        array[i], array[smallest] = array[smallest], array[i]
        heapify(array, n, smallest)

# Time Complexity O(nlogn)
# Space Complexity O(1)
def heap_sort(array):
    print("Heap Sort")
    n = len(array)
    for i in range(int(n/2)-1, -1, -1):
        heapify(array, n, i)

    for i in range(n-1, 0, -1):
        array[i], array[0] = array[0], array[i]
        heapify(array, i, 0)
    # array.reverse()
    array.reverse()





lis = [4,5,7,2,9,8,3,6,1]
lis = [2,1,7,6,5,3,4,9,8]

# list1 = [5, 6,8,10,2,3,6,8, 98, 100]

print(bubble_sort(lis))

print(selection_sort(lis))

print("Insertion Sort")
print(insertion_sort(lis))

print(bucket_sort(lis))


print("Merge Sort")
print(merge_sort(lis, 0, len(lis) - 1))



print("Quick Sort")
print(quick_sort(lis, 0, len(lis)-1))

heap_sort(lis)
print(lis)
