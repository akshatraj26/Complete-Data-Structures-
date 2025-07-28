dict1 = {"name": "Abhinay", 'age': 35}

dict1['age'] = 36
dict1['address'] = "Bhairach"

# print(dict1.popitem())
#assert dict1.pop('address'), "The key does not exist"
# dict1.popitem()
# dict1.clear()
del dict1['age']

f = dict1.copy()
f['age'] = 36
print(f)
print(f"dict1 {dict1}")

print(dict1.get('city', 2334))

print(dict1.setdefault('city', 'Uttar Pradesh'))
print(dict1.setdefault('city1', '3322'))

print(dict1)

boolen1 = {1: True, 2: True}
# print(all(boolen))

boolen = {0: False, 1: False}

boolen = {0: True, 1: False, 2: False}


print(all({}))

print(any(boolen1))

print(any({}))

dict = {'qa':2, 'dfff':34, 'ass':76, 'kjkff':90}

print(sorted(dict, key=len, reverse=True))
