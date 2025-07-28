class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next


sll = SinglyLinkedList()

node1 = Node(2)
node2 = Node(3)
node3 = Node(332)

sll.head = node1
sll.head.next = node2
sll.head.next.next = node3
sll.tail = node3

print([node.value for node in sll])

