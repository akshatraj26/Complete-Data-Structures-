"""
Design a stack which,in addition to push and pop, has a function min which returns the minimum element?
push, pop and min should all operate in O(1).
"""

class Node:
    def __init__(self, value = None):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __str__(self):
        pass

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next


class Stack:
    def __init__(self):
        self.ll = LinkedList()
        self.min_node = self.ll.head


    def __iter__(self):
        pass

    def __str__(self):
        values = [str(node.value) for node in self.ll]
        return "\n".join(values)

    def is_empty(self):
        if self.ll.head is None:
            return True
        else:
            return False

    # Add an element at the start of the Stack
    # Time Complexity O(1)
    def push(self, value):
        new_node = Node(value)

        if self.is_empty():
            self.ll.head = new_node
            self.ll.tail = new_node
        else:
            new_node.next = self.ll.head
            self.ll.head = new_node
            return "Insertion of the node is done successfully."

    # Deleting the latest element in the stack
    def pop(self):
        if self.is_empty():
            return "The Stack is empty."
        else:
            value = self.ll.head
            self.ll.head = self.ll.head.next
            return value

    def min(self):
        node = self.ll.head
        min_value = node.value
        while node:
            if min_value > node.value:
                min_value = node.value
            else:
                node = node.next
        return min_value


stack = Stack()
print(stack.is_empty())
print(stack.push(45))
print(stack.push(67))
print(stack.push(89))
print(stack.push(43))
print(stack.push(6))
print(stack.min())

print("_"*100)
stack.pop()
print(stack.min())

