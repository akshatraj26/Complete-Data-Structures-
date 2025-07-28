class CircularQueue:
    def __init__(self, capacity):
        self.capacity = capacity
        self.items = [None] * capacity
        self.start = -1
        self.top = -1

    def __str__(self):
        values = [str(x) for x in self.items]
        return " | ".join(values)

    # Check if the queue is full
    # Time Complexity O(1)
    def is_full(self):
        if self.top + 1 == self.start:
            return True
        elif self.start == 0 and self.top + 1 == self.capacity:
            return True
        else:
            return False

    # Check if the queue is empty
    # Time Complexity O(1)
    def is_empty(self):
        if self.top == -1:
            return True
        else:
            return False

    # Insert the element at the end of the queue
    def enqueue(self, value):
        if self.is_full():
            return "The Queue is full"
        else:
            if self.top + 1 == self.capacity:
                self.top = 0
            else:
                self.top += 1
                if self.start == -1:
                    self.start = 0
            self.items[self.top] = value
            return "The Value is added at the end of the Queue."

    # Delete the first element in the Queue
    # Time Complexity O(1)
    def dequeue(self):
        if self.is_empty():
            return "The Queue is empty"
        else:
            first_value = self.items[self.start]
            start = self.start
            if self.start == self.top:
                self.start = -1
                self.top = -1
            elif self.start + 1 == self.capacity:
                self.start = 0
            else:
                self.start += 1
            self.items[start] = None
            return first_value

    # Look the first element of the queue
    def peek(self):
        if self.is_empty():
            return "There is no element in the Queue."
        else:
            return self.items[self.start]

    # Delete all element in the Queue
    def delete(self):
        self.items = [None] * self.capacity
        self.start = -1
        self.top = -1
        return "Successfully deletion of all element in the Queue"





custom_queue = CircularQueue(5)
print(custom_queue.is_full())
print(custom_queue.is_empty())

print("_"*100)
print(custom_queue.enqueue(45))
print(custom_queue.enqueue(56))
print(custom_queue.enqueue(32))
print(custom_queue)
print("_"*100)

print(custom_queue.dequeue())
print(custom_queue.dequeue())
print(custom_queue)
print("_"*100)

print(custom_queue.enqueue(43))
print(custom_queue)

print("_"*100)
print(custom_queue.peek())
print(custom_queue)

print("_"*100)
print(custom_queue.delete())
print(custom_queue)

