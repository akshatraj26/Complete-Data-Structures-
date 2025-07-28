from multiprocessing import Queue

custom_queue = Queue(maxsize=4)
# Add a element
custom_queue.put(20)
# To delete element
print(custom_queue.get())