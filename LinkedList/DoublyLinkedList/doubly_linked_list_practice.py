class Node:
    def __init__(self, value = None):
        self.value = value
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next

    # Override the Len method
    def __len__(self):
        node = self.head
        count = 0
        while node:
            count += 1
            node = node.next
        return count

    # Create a Doubly Linked List
    # Time Complexity O(1)
    def create_linked_list(self, value):
        new_node = Node(value)
        new_node.next = None
        new_node.prev = None
        self.head = new_node
        self.tail = new_node
        return "Doubly Linked List Created"

    # Inserting a node in the Doubly Linked List
    # Time Complexity O(n)
    def insert_node_doubly_ll(self, value, location):
        new_node = Node(value)
        if self.head is None:
            print("Node cannot be inserted. Doubly Linked list does not exist. First create doubly linked list")
        else:
            # Inserting a node at the start
            if location == 0:
                new_node.next = self.head
                new_node.prev = None
                self.head.prev = new_node
                self.head = new_node
            # Inserting a node at the end
            elif location == 1:
                new_node.next = None
                new_node.prev = self.tail
                self.tail.next = new_node
                self.tail = new_node
            # Inserting a node at the specific location
            else:
                temp_node = self.head
                index = 0
                while index < location - 1:
                    # Current node
                    temp_node = temp_node.next
                    index += 1
                next_node = temp_node.next
                new_node.next = next_node
                new_node.prev = temp_node
                next_node.prev = new_node
                temp_node.next = new_node


    # Traverse the node of the Linked List
    # Time Complexity O(n)
    def traversing_node(self):
        if self.head is None:
            print("There is no node to traverse")
        else:
            node = self.head
            while node:
                print(f"| {node.prev} | {node.value} | {node.next} |", end=" = ")
                node = node.next

    # Reverse Traversing the node of the Linked List
    # Time Complexity O(n)
    def reverse_traversing(self):
        if self.head is None:
            print("There is no node to traverse")
        else:
            node = self.tail
            print("Reverse Traversing")
            while node:
                print(node.value)
                node = node.prev

    # Searching of a Node in the Doubly Linked List
    # Time Complexity O(n)
    def search_node_doubly_ll(self, node_value):
        if self.head is None:
            print("There is no node to search")

        node = self.head
        while node:
            if node.value == node_value:
                return node.value
            node = node.next
        return "This node does not exist in the Doubly Linked List."


    # Delete a node from the Doubly Linked List
    # Time Complexity O(n)
    def delete_node_doubly_ll(self, location):
        if self.head is None:
            return "There is no node to search in the Doubly Linked List"
        else:
            # Deleting a node from start
            # Time Complexity O(1)
            if location == 0:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                else:
                    self.head = self.head.next
                    self.head.prev = None

            # Deleting a node from end
            # Time Complexity O(1)
            elif location == 1:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                else:
                    self.tail = self.tail.prev
                    self.tail.next = None

            # Deleting a node from specific location
            # Time Complexity O(n)

            else:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                else:
                    temp_node = self.head
                    index = 0
                    while index < location - 1:
                        # Current node
                        temp_node = temp_node.next
                        index += 1
                    next_node = temp_node.next
                    temp_node.next = next_node.next
                    next_node.prev = temp_node





    # Clear the Doubly Linked List
    def clear_doubly_linked_list(self):
        self.head = None
        self.tail= None






doubly_ll = DoublyLinkedList()
doubly_ll.create_linked_list(34)
print([node.value for node in doubly_ll])
doubly_ll.create_linked_list(65)
print([node.value for node in doubly_ll])

doubly_ll.create_linked_list(87)
print([node.value for node in doubly_ll])

doubly_ll.create_linked_list(98)
print([node.value for node in doubly_ll])

doubly_ll.create_linked_list(42)
print([node.value for node in doubly_ll])
print("-"*100)

doubly_ll.insert_node_doubly_ll(56, 0)
print([node.value for node in doubly_ll])
print("-"*100)

doubly_ll.insert_node_doubly_ll(89, 0)
print([node.value for node in doubly_ll])
print("-"*100)

doubly_ll.insert_node_doubly_ll(68, 1)
print([node.value for node in doubly_ll])
print("-"*100)

doubly_ll.insert_node_doubly_ll(58, 1)
print([node.value for node in doubly_ll])
print("-"*100)

doubly_ll.insert_node_doubly_ll(99, 2)
print([node.value for node in doubly_ll])
print("-"*100)

doubly_ll.insert_node_doubly_ll(59, 2)
print([node.value for node in doubly_ll])
print("-"*100)

doubly_ll.insert_node_doubly_ll(97, 2)
print([node.value for node in doubly_ll])
print("-"*100)

doubly_ll.insert_node_doubly_ll(101, 2)
print([node.value for node in doubly_ll])
print("-"*100)

doubly_ll.insert_node_doubly_ll(123, 3)
print([node.value for node in doubly_ll])
print("-"*100)


doubly_ll.insert_node_doubly_ll(343, 4)
print([node.value for node in doubly_ll])
print("-"*100)

print(f"Length of the Doubly Linked List:- {len(doubly_ll)}")
print("-"*100)

print(doubly_ll.traversing_node())

print("-"*100)
print(doubly_ll.reverse_traversing())

print("-"*100)
print(f"Found {doubly_ll.search_node_doubly_ll(101)}")
print("-"*100)


print("-"*100)
print(doubly_ll.search_node_doubly_ll(500))
print("-"*100)

print("Deleting node from the Doubly Linked List")
print([node.value for node in doubly_ll])

doubly_ll.delete_node_doubly_ll(0)
print([node.value for node in doubly_ll])
print("-"*100)


# doubly_ll.delete_node_doubly_ll(0)
# print([node.value for node in doubly_ll])
# print("-"*100)


doubly_ll.delete_node_doubly_ll(1)
print([node.value for node in doubly_ll])
print("-"*100)

doubly_ll.delete_node_doubly_ll(1)
print([node.value for node in doubly_ll])
print("-"*100)


doubly_ll.delete_node_doubly_ll(2)
print([node.value for node in doubly_ll])
print("-"*100)

doubly_ll.delete_node_doubly_ll(2)
print([node.value for node in doubly_ll])
print("-"*100)

print("Clear the entire doubly linked list")
doubly_ll.clear_doubly_linked_list()
print([node.value for node in doubly_ll])
print("-"*100)



