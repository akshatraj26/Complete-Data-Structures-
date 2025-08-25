import math

# Time Complexity O(n^2)
# Space Complexity O(1)
def bubble_sort(array):
    print("Bubble Sort")
    n = len(array)
    for i in range(n):
        for j in range(n-i-1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
    return array

# Time Complexity O(n^2)
# Space Complexity O(1)
def selection_sort(array):
    print("Selection Sort")
    n = len(array)
    for i in range(n):
        min_index = i
        for j in range(i+1, n):
            if array[min_index] > array[j]:
                min_index = j
        array[min_index], array[i] = array[i], array[min_index]

    return array

# Time Complexity O(n^2)
# Space Complexity O(1)
def insertion_sort(array):
    print("Insertion Sort")
    n = len(array)
    for i in range(n):
        key = array[i]
        j = i - 1
        while  j >= 0 and key < array[j]:
            array[j+1] = array[j]
            j -= 1
        array[j+1] = key
    return array


# Time Complexity O(n^2)
# Space Complexity O(n)
def bucket_sort(array):
    print("Bucket Sort")
    n = len(array)
    number_of_buckets = round(math.sqrt(n))
    max_value = max(array)

    # Create number of buckets
    arr = []
    for _ in range(number_of_buckets):
        arr.append([])

    # print("Array:- ", arr)
    # Add value to buckets
    for i in array:
        index_b = math.ceil(i * number_of_buckets / max_value)
        arr[index_b - 1].append(i)

    # print("After Adding element", arr)

    # Sort the Sub array
    for i in range(number_of_buckets):
        arr[i] = selection_sort(arr[i])

    # print('After Sorting element ', arr)

    # Merge the Sub array
    k = 0
    for i in range(number_of_buckets):
        for j in range(len(arr[i])):
            array[k] = arr[i][j]
            k += 1

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

def heap_sort(array):
    print("Heap Sort")
    n = len(array)
    for i in range(int(n/2)-1, -1, -1):
        heapify(array, n, i)

    for i in range(n-1, 0, -1):
        array[i], array[0] = array[0], array[i]
        heapify(array, n, 0)


# Helper function for Quick sort
def partition(array, low, high):
    i = low - 1
    pivot = array[high]
    for j in range(low, high):
        if array[j] <= pivot:
            i += 1
            array[i], array[j] = array[j], array[i]
    array[i+1], array[high] = array[high], array[i+1]
    return i+1

def quick_sort(array, low, high):
    if low < high:
        pi = partition(array, low, high)
        quick_sort(array, low, pi - 1)
        quick_sort(array, pi + 1, high)
    return array




list1 = [5, 6,8,10,2,3,6,8]


print(bubble_sort(list1))
print(selection_sort(list1))
print(insertion_sort(list1))
print(bucket_sort(list1))

heap_sort(list1)
print(list1)



print("Quick Sort")
print(quick_sort(list1, 0, len(list1) -1))