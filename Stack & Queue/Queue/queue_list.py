

class Queue:
    def __init__(self):
        self.items = []

    def __str__(self):
        values = [str(x) for x in self.items]
        return " ".join(values)

    def isEmpty(self):
        if not self.items:
            return True
        else:
            return False

    # Adding element to the end of the queue.
    # Time Complexity O(amortized n)
    def enqueue(self, value):
        self.items.append(value)
        return 'The Element is inserted at the end of Queue.'

    # Removing the first element from the queue.
    # Time Complexity O(n)
    def dequeue(self):
        if self.isEmpty():
            return "There is no element to delete"
        else:
            return self.items.pop(0)

    # Peek method shows the first element from the queue
    # Time Complexity O(1)
    def peek(self):
        if self.isEmpty():
            return "There is no element to delete"
        else:
            return self.items[0]

    # delete the queue
    def delete(self):
        self.items = None
        return "Successfully deletion of the queue"

custom_queue = Queue()
print(custom_queue.isEmpty())
print("-"*100)

custom_queue.enqueue(23)
custom_queue.enqueue(67)
custom_queue.enqueue(55)
custom_queue.enqueue(98)
print(custom_queue)
print("-"*100)


print(custom_queue.dequeue())
print(custom_queue)
print("-"*100)

print(custom_queue.peek())
print("-"*100)

print(custom_queue.isEmpty())
print("-"*100)

print(custom_queue.delete())
print("-"*100)

