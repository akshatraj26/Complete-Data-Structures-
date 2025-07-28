arr = [1,2,4,5,7,9]

# for i in range(0, int(len(arr)/2)):
#     other = len(arr) - i - 1
#     print(f"Other: {other}")
#     temp = arr[i]
#     arr[i] = arr[other]
#     arr[other] = temp
# print(arr)


for i in range(0, int(len(arr)/2)):
    other = len(arr) - i - 1
    print(i, other)
    arr[other], arr[i] = arr[i], arr[other]

print(arr)