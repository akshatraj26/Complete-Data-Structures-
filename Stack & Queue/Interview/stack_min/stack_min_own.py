class Node:
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next

class Stack:
    def __init__(self):
        self.head = None
        self.min_node = None

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next

    def push(self, value):
        if self.min_node and (self.min_node.value < value):
            self.min_node = Node(value=self.min_node.value, next = self.min_node)
        else:
            self.min_node = Node(value=value, next=self.min_node)
        self.head =  Node(value=value, next=self.head)

    def pop(self):
        if not self.head:
            return None
        else:
            self.min_node = self.min_node.next
            item = self.head.value
            self.head = self.head.next
            return item

    def min(self):
        if not self.min_node:
            return None
        else:
            return self.min_node.value


stack = Stack()
# print(stack.is_empty())
stack.push(45)
print(stack.min())
print([node.value for node in stack])
print("_"*100)

stack.push(67)
stack.push(89)
# print(stack.min())
print([node.value for node in stack])
print("_"*100)

stack.push(43)
print(stack.min())
print([node.value for node in stack])
print("_"*100)



print(stack.pop())
print(stack.min())
print([node.value for node in stack])
