class Queue:
    def __init__(self, maxSize):
        self.items = maxSize * [None]
        self.maxSize = maxSize
        self.start = -1
        self.top = -1

    def __str__(self):
        values = [str(x) for x in self.items]
        return " ".join(values)

    # Check whether the queue is full or not
    # Time Complexity O(1)
    def isFull(self):
        if self.top + 1 == self.start:
            return True
        elif self.start == 0 and self.top + 1 == self.maxSize:
            return True
        else:
            return False

    # check whether the queue is empty or not
    # Time Complexity O(1)
    def isEmpty(self):
        if self.top == -1:
            return True
        else:
            return False

    # Insert the element at the end of the queue
    # Time Complexity O(1)
    def enqueue(self, value):
        if self.isFull():
            return "The Queue is full"
        else:
            if self.top + 1 == self.maxSize:
                self.top = 0
            else:
                self.top += 1
                if self.start == -1:
                    self.start = 0
            self.items[self.top] = value
            return "The element is inserted at the end of the Queue"

    # Delete the first element from the queue
    # Time Complexity O(1)
    def dequeue(self):
        if self.isEmpty():
            return "There is not any element in the Queue."
        else:
            firstElement = self.items[self.start]
            start = self.start
            if self.start == self.top:
                self.start = -1
                self.top = -1
            elif self.start + 1 ==  self.maxSize:
                self.start =  0
            else:
                self.start += 1
            self.items[start] = None
            return firstElement

    # See the first element
    def peek(self):
        if self.isEmpty():
            return "There is not any element in the Queue"
        else:
            return self.items[self.start]

    # Delete all the element in the queue.
    # Time Complexity O(1)
    def delete(self):
        self.items = self.maxSize * [None]
        self.start = -1
        self.top = -1
        return "Now all the element in the queue is deleted"



custom_queue = Queue(3)
print(f"isEmpty :- {custom_queue.isEmpty()}")
print(custom_queue.enqueue(56))
print(custom_queue.enqueue(67))
print(custom_queue.enqueue(45))
print(f"isFull:-  {custom_queue.isFull()}")
print("_"*100)

print(custom_queue)

print("-"*100)
print(f"Dequeue element {custom_queue.dequeue()}")
print(custom_queue)

print("_"*100)
print(f"Dequeue element {custom_queue.dequeue()}")
print(custom_queue)

print("_"*100)
print(f"Dequeue element {custom_queue.dequeue()}")
print(custom_queue)
print(f"isEmpty :- {custom_queue.isEmpty()}")

print("_"*100)
print(custom_queue.enqueue(23))

print(custom_queue)

print(custom_queue.peek())

print("_"*100)
print(custom_queue.enqueue(76))
print(custom_queue)
print(custom_queue.delete())
print(custom_queue)
print(custom_queue.isEmpty())
