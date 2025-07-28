class Stack:
    def __init__(self, maxSize):
        self.maxSize = maxSize
        self.list = []

    def __str__(self):
        self.list.reverse()
        values = [str(x) for x in self.list]
        return "\n".join(values)

    # isEmpty
    def isEmpty(self):
        if not self.list:
            return True
        else:
            return False

    # isFull
    def isFull(self):
        if len(self.list) == self.maxSize:
            return True
        else:
            return False

    # push
    def push(self, value):
        if self.isFull():
            return "The stack is full"
        else:
            self.list.append(value)
            return "The element has been successfully inserted."

    # pop
    def pop(self):
        if self.isEmpty():
            return "There is no element in the stack"
        else:
            return self.list.pop()

    # peek
    def peek(self):
        if self.isEmpty():
            return "There is no element in the stack"
        else:
            return self.list[len(self.list)-1]

    # delete
    def delete(self):
        return self.list.clear()
custom_stack = Stack(4)
print(custom_stack.isEmpty())
print(custom_stack.isFull())

print(custom_stack.push(23))
print(custom_stack.push(45))
print(custom_stack.push(76))
print(custom_stack.push(55))
print("_"*100)

# print(custom_stack)
print(custom_stack.isEmpty())
print(custom_stack.isFull())

print(f"Popped Element :- {custom_stack.pop()}")


print(custom_stack)
print("_"*100)
print(custom_stack.peek())

print("_"*100)
print(custom_stack.delete())
print(custom_stack)

