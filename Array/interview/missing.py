list1 = [1,2,3,4,5,7,8,9,10, 11,12,13,14,15,16,17, 18]


def missingNum(list1, num):
    length = max(list1)
    series_sum = length * (length + 1)/2
    sum_arr = sum(list1)
    return series_sum - sum_arr

print(missingNum(list1, 3))