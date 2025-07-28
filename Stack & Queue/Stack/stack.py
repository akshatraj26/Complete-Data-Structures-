class Stack:
    def __init__(self):
        self.list = []


    def __str__(self):
        self.list.reverse()
        values = [str(x) for x in self.list]
        return "\n".join(values)

    # Check whether stack is empty
    def isEmpty(self):
        if self.list == []:
            return True
        else:
            return False

    def push(self, value):
        self.list.append(value)
        return "The element has been successfully inserted"

    # pop
    def pop(self):
        if self.isEmpty():
            return "There is not any element in the stack."
        else:
            return self.list.pop()
    # peek
    def peek(self):
        if self.isEmpty():
            return "There is not any element in the stack."
        else:
            return self.list[len(self.list)-1]

    # delete
    def delete(self):
        self.list = self.list.clear()



custom_stack = Stack()
print(custom_stack.isEmpty())

print("-"*100)
custom_stack.push(1)
custom_stack.push(2)
custom_stack.push(3)
custom_stack.push(5)
custom_stack.push(65)

# print(custom_stack)
print(f"Popped element:- {custom_stack.pop()}")
# print(f"Popped element:- {custom_stack.pop()}")


print("-"*100)
# print(custom_stack)


print(f"Peek:- {custom_stack.peek()}")


custom_stack.delete()

print("_"*100)
# print(custom_stack)
