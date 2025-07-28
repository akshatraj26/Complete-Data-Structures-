import queue as q

custom_queue = q.Queue(maxsize=3)

print(custom_queue.qsize())
print(custom_queue.empty())
custom_queue.put(45)
custom_queue.put(67)
custom_queue.put(98)

print(custom_queue.qsize())

print(custom_queue.full())

print(custom_queue.get())

print(custom_queue.qsize())

