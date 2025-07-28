"""
Design a stack which,in addition to push and pop, has a function min which returns the minimum element?
push, pop and min should all operate in O(1).
"""

class Node:
    def __init__(self, value = None):
        self.value = value
        self.next = None


class Stack:
    def __init__(self):
        self.head = None
        self.tail = None
        self.min_node = self.head

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next


    # Add an element at the start of the Stack
    # Time Complexity O(1)
    def push(self, value):
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
            self.tail = new_node

        else:
            new_node.next = self.head
            self.head = new_node
            # For the min_node
            if self.min_node and (self.min_node.value < value):
                self.min_node = Node(value=self.min_node.value)
            else:
                self.min_node = Node(value=value)


            return "Insertion of the node is done successfully."

    # Deleting the latest element in the stack
    def pop(self):
        if not self.head:
            return "The Stack is empty."
        else:
            value = self.head
            self.head = self.head.next

            return value

    def min(self):
        if not self.min_node:
            return None
        return self.min_node.value


# stack = Stack()
# print(stack.push(45))
# print(stack.push(67))
# print(stack.push(89))
# print(stack.push(43))
# print(stack.push(78))
#
# print(stack.min())

stack = Stack()

stack.push(45)
print([node.value for node in stack])
print("_"*100)
print(stack.min())

stack.push(67)
stack.push(89)
print(stack.min())
print([node.value for node in stack])
print("_"*100)

stack.push(43)
print(stack.min())
print([node.value for node in stack])
print("_"*100)



# print(stack.pop())
# print(stack.min())
# print([node.value for node in stack])
#
#
# print(stack)
#
#
#
#
