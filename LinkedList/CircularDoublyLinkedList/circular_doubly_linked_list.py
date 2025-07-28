class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None
        self.prev = None

class CircularDoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next
            if node == self.tail.next:
                break

    # Overriding the len method for linked list
    # Time Complexity O(n)
    def __len__(self):
        node = self.head
        count = 0
        while node:
            count += 1
            node = node.next
            if node == self.tail.next:
                break
        return count

    # Create circular Doubly Linked List
    # Time Complexity O(1)
    def create_circular_doubly_ll(self, node_value):
        new_node = Node(node_value)
        new_node.next = new_node
        new_node.prev = new_node
        self.head = new_node
        self.tail = new_node
        return "Circular Doubly Linked List is created"


    # Insert the node in the Circular Doubly Linked List
    # Time Complexity O(n)
    def insert_node_circular_doubly_ll(self, node_value, location):
        new_node = Node(node_value)
        if self.head is None:
            return "Circular Doubly Linked List does not exist."
        else:
            # Inserting a node at the start of the Circular Doubly Linked List
            # Time Complexity O(1)
            if location == 0:
                new_node.next = self.head
                new_node.prev = self.tail
                self.head.prev = new_node
                self.head = new_node
                self.tail.next = new_node
            # Inserting a node at the end of the Circular Doubly Linked List
            # Time Complexity O(1)
            elif location == 1:
                new_node.next = self.head
                new_node.prev = self.tail
                self.head.prev = new_node
                self.tail.next = new_node
                self.tail = new_node
            # Inserting a node at the specific location of the Circular Doubly Linked List
            # Time Complexity O(1)
            else:
                curr_node = self.head
                index = 0
                while index < location -1:
                    # Current node
                    curr_node = curr_node.next
                    index += 1
                next_node = curr_node.next
                new_node.next = next_node
                new_node.prev = curr_node
                next_node.prev = new_node
                curr_node.next = new_node
            return "The Node has been successfully inserted"

    # Traversing the node of the circular doubly linked list
    # Time Complexity O(n)

    def traversing_circular_doubly_linked_list(self):
        if self.head is None:
            return "There is no node to traverse"
        node = self.head
        while node:
            # print(f"{id(node.prev)} | {node.value} | {id(node.next)}")
            print(node.value)
            if node == self.tail:
                break
            node = node.next



    # Reverse Traversal of the Circular Doubly Linked List
    def reverse_traversing_circular_doubly_linked_list(self):
        if self.head is None:
            return "There is no node to traverse"
        else:
            node = self.tail
            while node:
                print(node.value)
                if node == self.head:
                    break
                node = node.prev

    # Searching for node in the Circular Doubly Linked List
    # Time Complexity O(n)
    def search_node_circular_doubly_linked_list(self, node_value):
        if self.head is None:
            return "There is no node to search anything."
        else:
            node = self.head
            while node:
                if node.value == node_value:
                    return node.value
                if node == self.tail:
                    break
                node = node.next

            return "There is no such node in the Linked List"

    # Delete a node from the Circular Doubly Linked List
    def delete_node_circular_doubly_linked_list(self, location):
        if self.head is None:
            return "There is no node to delete"
        else:
            if location == 0:
                if self.head == self.tail:
                    self.head.prev = None
                    self.tail.next = None
                    self.head = None
                    self.tail = None

                else:
                    self.head = self.head.next
                    self.head.prev = self.tail
                    self.tail.next = self.head

            elif location == 1:
                if self.head == self.tail:
                    self.head.prev = None
                    self.tail.next = None
                    self.head = None
                    self.tail = None
                else:
                    self.tail = self.tail.prev
                    self.tail.next = self.head
                    self.head.prev = self.tail

            else:
                curr_node = self.head
                index = 0
                while index < location - 1:
                    curr_node = curr_node.next
                    index += 1
                next_node = curr_node.next
                curr_node.next = next_node.next
                next_node.prev = curr_node
            return "The Node has been deleted successfully."

    # Delete Circular Doubly Linked List
    # Time Complexity O(n)
    def delete_circular_doubly_ll(self):
        if self.head is None:
            return "This Circular Doubly Linked List does not exist."

        else:
            self.tail.next = None
            node = self.head
            while node:
                node.prev = None
                node = node.next
            self.tail = None
            self.head = None
            print("Circular Doubly Linked List has been deleted successfully.")






circular_doubly_ll = CircularDoublyLinkedList()
print(circular_doubly_ll.create_circular_doubly_ll(34))
print([node.value for node in circular_doubly_ll])

print("-"*100)
circular_doubly_ll.insert_node_circular_doubly_ll(89, 0)
print([node.value for node in circular_doubly_ll])

print("-"*100)
circular_doubly_ll.insert_node_circular_doubly_ll(56, 0)
print([node.value for node in circular_doubly_ll])

print("-"*100)
circular_doubly_ll.insert_node_circular_doubly_ll(33, 1)
print([node.value for node in circular_doubly_ll])

print("-"*100)
circular_doubly_ll.insert_node_circular_doubly_ll(43, 1)
print([node.value for node in circular_doubly_ll])


print("-"*100)
circular_doubly_ll.insert_node_circular_doubly_ll(22, 2)
print([node.value for node in circular_doubly_ll])

print("-"*100)
circular_doubly_ll.insert_node_circular_doubly_ll(67, 3)
print([node.value for node in circular_doubly_ll])

print("-"*100)
print(f"Length :- {len(circular_doubly_ll)}")

print("-"*100)
print([node.value for node in circular_doubly_ll])
circular_doubly_ll.traversing_circular_doubly_linked_list()


print("-"*100)
print([node.value for node in circular_doubly_ll])
circular_doubly_ll.reverse_traversing_circular_doubly_linked_list()


print("_"*100)
print(circular_doubly_ll.search_node_circular_doubly_linked_list(89))

print("_"*100)
print(circular_doubly_ll.search_node_circular_doubly_linked_list(8))

print("_"*100)
print([node.value for node in circular_doubly_ll])
circular_doubly_ll.delete_node_circular_doubly_linked_list(0)
print([node.value for node in circular_doubly_ll])


print("_"*100)
print([node.value for node in circular_doubly_ll])
circular_doubly_ll.delete_node_circular_doubly_linked_list(1)
print([node.value for node in circular_doubly_ll])

print("_"*100)
print([node.value for node in circular_doubly_ll])
circular_doubly_ll.delete_node_circular_doubly_linked_list(2)
print([node.value for node in circular_doubly_ll])

print("_"*100)
print([node.value for node in circular_doubly_ll])
circular_doubly_ll.delete_circular_doubly_ll()
print([node.value for node in circular_doubly_ll])
