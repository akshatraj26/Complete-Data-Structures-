
arr = ['i', 'am', 'into', 'mature']

def capitilize_first(arr):
    result = []
    if len(arr) == 0:
        return result
    result.append(arr[0][0].upper() + arr[0][1:])
    return result + capitilize_first(arr[1:])


print(capitilize_first(arr))

for i in range(len(arr)):
    arr[i] = arr[i].title()





print(arr)