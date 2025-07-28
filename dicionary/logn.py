arr = [12,14, 15, 18, 40, 60]

left = 0
right = len(arr) - 1
# print(left, right)
target = 40
while left <= right:
    mid = (left + right) // 2

    if arr[mid] == target:
        print(f"index {mid}, value {arr[mid]}")
    if arr[mid] < target:
        left = mid + 1
    else:
        right = mid - 1

