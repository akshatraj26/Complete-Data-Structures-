class Node:
    def __init__(self, value = None):
        self.value = value
        self.next = None

class StackLinkedList:
    def __init__(self):
        self.tail = None
        self.head = None

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next

    def __str__(self):
        pass

    # Check whether stack is empty or not
    def isEmpty(self):
        if self.head is None:
            return True
        else:
            return False

    # Push the value in stack
    def push(self, value):
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node

        return self.head

    # pop
    def pop(self):
        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            temp_node = self.head
            self.head = self.head.next
            return temp_node.value


    # Peek to look at the last element
    def peek(self):
        if self.head is None:
            return "There is no element in the stack"
        else:
            return self.head.value

    # delete
    def delete(self):
        self.head = None
        self.tail = None
        return "The Stack & Queue deletion successfully."

stack_ll = StackLinkedList()
print(stack_ll.isEmpty())

stack_ll.push(34)
stack_ll.push(65)
stack_ll.push(45)
stack_ll.push(43)
stack_ll.push(87)


print([node.value for node in stack_ll])
print("-"*100)
print(f"Peek :- {stack_ll.peek()}")

print("-"*100)
print(f"Pop :- {stack_ll.pop()}")
print(f"Pop :- {stack_ll.pop()}")
print([node.value for node in stack_ll])
print("-"*100)

print(f"Delete :- {stack_ll.delete()}")
print([node.value for node in stack_ll])
print("-"*100)

