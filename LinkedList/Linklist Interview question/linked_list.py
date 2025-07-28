from random import randint
class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None
        self.prev = None

    def __str__(self):
        return f"{self.value}"

class LinkedList:
    def __init__(self, values = None):
        self.head = None
        self.tail = None

    def __iter__(self):
        curr_node = self.head
        while curr_node:
            yield curr_node
            curr_node = curr_node.next

    def __str__(self):
        values = [str(x.value) for x in self]
        return " -> ".join(values)

    def __len__(self):
        node = self.head
        count = 0
        while node:
            count += 1
            node = node.next

        return count

    def add(self, value):
        if self.head is None:
            new_node = Node(value)
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = Node(value)
            self.tail = self.tail.next
        return self.tail

    def generate(self, n, min_value, max_value):
        self.head = None
        self.tail = None
        for _ in range(n):
            self.add(randint(min_value, max_value))
        return self


# ll = LinkedList()
# print(ll.generate(6, 30, 50))
#
# print(len(ll))