def permutation(list1, list2):
    if len(list1) != len(list2):
        return False
    list1 = list1.sort()
    list2 = list2.sort()
    if list1 == list2:
        return True
    else:
        return False
lis1 = 'run'.split()
list2 = 'unr'.split()

print(permutation(lis1, list2))