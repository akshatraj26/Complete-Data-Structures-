from collections import deque

custom_queue = deque(maxlen=3)
print(custom_queue)


custom_queue.append(34)
custom_queue.append(67)
custom_queue.append(76)
print(custom_queue)

print("_"*100)
custom_queue.append(23)
print(custom_queue)

custom_queue.append(80)
print(custom_queue)

print("_"*100)
print(custom_queue.popleft())
print(custom_queue)


print("_"*100)
print(custom_queue.clear())
print(custom_queue)
