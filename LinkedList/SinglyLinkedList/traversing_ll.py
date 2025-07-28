class Node:
    def __init__(self, value = None):
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

    def insert_sll(self, value, location):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            if location == 0:
                new_node.next = self.head
                self.head = new_node
            elif location == 1:
                new_node.next = None
                self.tail.next = new_node
                self.tail = new_node
            else:
                temp_node = self.head
                index = 0
                while index < location - 1:
                    temp_node = temp_node.next
                    index += 1
                next_node = temp_node.next
                temp_node.next = new_node
                new_node.next = next_node

    # Method Overriding the Length for SLL
    def __len__(self):
        node = self.head
        count = 0
        while node is not None:
            count += 1
            node = node.next
        return count

    # Traverse the Singly Linked List
    def traverse_sll(self):

        if self.head is None:
            print("The SLL has no element in it.")
        else:
            node = self.head
            while node is not None:
                print(node.value)
                node = node.next



sll = SinglyLinkedList()
sll.insert_sll(23, 0)
sll.insert_sll(45, 0)
sll.insert_sll(78, 0)
sll.insert_sll(34, 0)
print([node.value for node in sll])
sll.insert_sll(98, 1)
print([node.value for node in sll])

sll.insert_sll(67, 0)
sll.insert_sll(33, 0)
print([node.value for node in sll])
sll.insert_sll(66, 3)
print([node.value for node in sll])


print(f"The Length of the singly linked list {len(sll)}")
print("-"*100)
print("Traversing the SLL")
sll.traverse_sll()



