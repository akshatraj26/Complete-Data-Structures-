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

    def enqueue(self, node_value):
        new_node = Node(node_value)
        if self.is_empty():
            self.ll.head = new_node
            self.ll.tail = new_node
        else:
            new_node.next = None
            self.ll.tail.next = new_node
            self.ll.tail = new_node


    def dequeue(self):
        if self.is_empty():
            return "There is no element to delete in Queue."

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
            return "There is no element to peek in Queue."

        else:
            value = self.ll.head.value
            return value

# cust_queue = Queue()
# assert cust_queue, "Something wrong when creating a queue"
# cust_queue.enqueue(45)
# print(cust_queue)
#
# cust_queue.enqueue(65)
# cust_queue.enqueue(98)
# cust_queue.enqueue(32)
#
# print(cust_queue)
#
# print(cust_queue.dequeue())
