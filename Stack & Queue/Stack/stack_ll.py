class Node:
    def __init__(self, value = None):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next

class Stack:
    def __init__(self):
        self.linked_list = LinkedList()

    def __str__(self):
        values = [str(x.value) for x in self.linked_list]
        return "\n".join(values)

    # Is Empty
    def isEmpty(self):
        if self.linked_list.head is None:
            return True
        else:
            return False

    # push
    def push(self, value):
        new_node = Node(value)
        new_node.next = self.linked_list.head
        self.linked_list.head = new_node
        return "The element inserted successfully"

    # pop
    def pop(self):
        if self.isEmpty():
            return "There is no element to delete"
        else:
            temp_node = self.linked_list.head
            self.linked_list.head = self.linked_list.head.next
            return temp_node.value

    # peek
    def peek(self):
        if self.linked_list.head is None:
            return "There is no element in the stack."
        else:
            return self.linked_list.head.value

    # delete
    def delete(self):
        self.linked_list.head = None
        self.linked_list.tail = None
        return "Deletion of stack successfully"



custom_stack = Stack()
print(custom_stack.isEmpty())

custom_stack.push(34)
custom_stack.push(56)
custom_stack.push(23)
custom_stack.push(89)
custom_stack.push(43)

print("_"*100)
print(custom_stack)
print("_"*100)

print(f"Pop element:- {custom_stack.pop()}")
print("_"*100)
print(custom_stack)


print("_"*100)
print(custom_stack.peek())


print("_"*100)
print(custom_stack.delete())

