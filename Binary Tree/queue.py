
class Node:
    def __init__(self, value=None):
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

class Queue:
    def __init__(self):
        self.ll = LinkedList()

    def __str__(self):
        values = [str(node.value) for node in self.ll]
        return " ".join(values)

    def is_empty(self):
        if self.ll.head is None:
            return True
        else:
            return False


    def enqueue(self, value):
        new_node = Node(value)
        if self.is_empty():
            self.ll.head = new_node
            self.ll.tail = new_node
        else:
            new_node.next = None
            self.ll.tail.next = new_node
            self.ll.tail = new_node

    def dequeue(self):
        if self.is_empty():
            return "This Queue is empty"
        else:
            value = self.ll.head.value
            if self.ll.head == self.ll.tail:
                self.ll.head = None
                self.ll.tail = None
                return value
            else:
                self.ll.head = self.ll.head.next
                return value

    def peek(self):
        if self.is_empty():
            return "This Queue is empty"
        else:
            return self.ll.head.value


que = Queue()
que.enqueue(45)
que.enqueue(67)
que.enqueue(89)
que.enqueue(98)
print(que.dequeue())
print(que)
