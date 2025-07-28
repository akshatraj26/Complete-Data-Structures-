arr = [1,20,30, 44, 5, 56, 57, 8,9,10, 31, 12, 13, 58]

max_product = 0

for i in range(len(arr)):
    for j in range(i+1, len(arr)):
        running_product = arr[i] * arr[j]
        if running_product > max_product:
            max_product = running_product
            pairs = (arr[i] , arr[j])


print(max_product, pairs)