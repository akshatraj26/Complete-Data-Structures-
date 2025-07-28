from nbformat.sign import yield_everything


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __str__(self):
        return str(self.value)

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
        return " -> ".join(values)

    # Check whether the queue is empty
    # Time Complexity O(1)
    def is_empty(self):
        if self.ll.head is None:
            return True
        else:
            return False

    # Adding an element to the end of the queue.
    # Time Complexity O(1)
    def enqueue(self, value):
        node = Node(value)
        if self.ll.head is None:
            self.ll.head = node
            self.ll.tail = node
        else:
            node.next = None
            self.ll.tail.next = node
            self.ll.tail = node

    # Removing the first element from the queue
    # Time Complexity O(1)
    def dequeue(self):
        if self.is_empty():
            return "There is no element to delete in the queue."
        else:
            if self.ll.head == self.ll.tail:
                self.ll.head = None
                self.ll.tail = None
            else:
                node_value = self.ll.head.value
                self.ll.head = self.ll.head.next
                return node_value

    # Show the first element from the queue
    # Time complexity O(1)
    def peek(self):
        if self.is_empty():
            return "There is no element to delete"
        else:
            node_value = self.ll.head.value
            return node_value

    def delete(self):
        self.ll.head = None
        self.ll.tail = None
        return "All element in the queue are deleted successfully."


queue = Queue()
print(queue.is_empty())
print("_"*100)

queue.enqueue(34)
queue.enqueue(45)
queue.enqueue(76)
queue.enqueue(87)

print(queue)
print("_"*100)

print(queue.dequeue())
print(queue)
print("_"*100)


print(queue.peek())
print(queue)
print("_"*100)


print(queue.delete())
print(queue)
print("_"*100)
