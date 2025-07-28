"""
Implement Queue Class which implements a queue using two stacks.
"""
class Stack:
    def __init__(self):
        self.list = []

    def __len__(self):
        return len(self.list)

    def __iter__(self):
       for i in range(len(self.list)):
           yield self.list[i]



    def push(self, item):
        self.list.append(item)

    def pop(self):
        if len(self.list) == 0:
            return "Stack is empty"
        else:
            return self.list.pop()

class QueueviaStack:
    def __init__(self):
        self.in_stack = Stack()
        self.out_stack = Stack()

    def __str__(self):
        values = [str(x) for x in self.in_stack]
        return " ".join(values)

    def enqueue(self, item):
        self.in_stack.push(item)

    def dequeue(self):
        while len(self.in_stack):
            self.out_stack.push(self.in_stack.pop())
        result = self.out_stack.pop()
        while len(self.out_stack):
            self.in_stack.push(self.out_stack.pop())
        return result

queue = QueueviaStack()
queue.enqueue(67)
queue.enqueue(78)
queue.enqueue(54)
queue.enqueue(98)
queue.enqueue(32)
print(queue)


print(queue.dequeue())
print(queue)

queue.enqueue(45)
print(queue.dequeue())
print(queue)



