arr = [2,6,4, 3, 9, 10, 7]

target = 6

def pair_sum(arr, target):
    all_pair = []
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i] == arr[j]:
                continue
            elif arr[i] + arr[j] == target:
                print(i, j)


    # return all_pair

pair_sum(arr, target)