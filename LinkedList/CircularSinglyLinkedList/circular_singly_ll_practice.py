class Node:
    def __init__(self, value = None):
        self.value = value
        self.next = None

class CircularSinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None


    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next
            if node == self.tail.next:
                break


    # creation of circular linked list
    def create_circular_sll(self, node_value):
        node = Node(node_value)
        node.next = node
        self.head  = node
        self.tail = node
        return "The Circular Singly Linked List is created"

    # Inserting the element in Circular Singly Linked List
    def insert_node_csll(self, value, location):
        new_node = Node(value)

        if self.head is None:
            new_node.next = self.head
            self.head = new_node
            self.tail = new_node


        else:
            if location == 0:
                new_node.next = self.head
                self.head = new_node
                self.tail.next = self.head

            elif location == 1:
                new_node.next = self.tail.next
                self.tail.next = new_node
                self.tail = new_node

            else:
                temp_node = self.head
                # Change the index to 1 so that element will added at that location
                index = 1
                while index < location - 1:
                    # current node
                    temp_node = temp_node.next
                    index += 1
                next_node = temp_node.next
                temp_node.next = new_node
                new_node.next = next_node

    # Traverse element of the Circular Singly Linked List
    def traversal_circular_sll(self):
        if self.head is None:
            print("There is no element to traverse.")
        else:
            node = self.head
            while node:
                print(node.value)
                node = node.next
                if node == self.tail.next:
                    break

    # Search element in the Circular Linked List
    def search_node_circular_sll(self, node_value):
        if self.head is None:
            return "There is no element to search."
        else:
            node = self.head
            while node:
                if node.value == node_value:
                    return node.value
                node = node.next
                if node == self.tail.next:
                    break
            return "This element does not exist in CSLL"

    # Deleting element form the CSLL
    def delete_node_circular_sll(self, location):
        if self.head is None:
            return "Circular SLL does not exist"
        # Deleting a node from the start of the CSLL
        else:
            if location == 0:
                if self.head == self.tail :
                    self.head = None
                    self.tail = None
                    self.head.next = None

                else:
                    node = self.head
                    self.head = self.head.next
                    self.tail.next = node.next
            # Deleting a node from the end of the CSLL
            elif location == 1:
                if self.head == self.tail :
                    self.head = None
                    self.tail = None
                    self.head.next = None

                else:
                    node = self.head
                    while node is not None:
                        if node.next == self.tail:
                            break
                        node = node.next

                    node.next = self.head
                    self.tail = node
            else:
                temp_node = self.head
                index = 1
                while index < location - 1:
                    # Current Node
                    temp_node = temp_node.next
                    index += 1
                next_node = temp_node.next
                temp_node.next = next_node.next


    # Clear the Circular Singly Linked List
    def delete_circular_sll(self):
        if self.head is None:
            return "Circular SLL does not exist"
        else:
            self.head = None
            self.tail.next = None
            self.tail = None




circular_sll = CircularSinglyLinkedList()
circular_sll.insert_node_csll(34, 0)
circular_sll.insert_node_csll(46, 0)
circular_sll.insert_node_csll(56, 0)
circular_sll.insert_node_csll(78, 0)
print([node.value for node in circular_sll])
print("-"*100)


circular_sll.insert_node_csll(32, 2)
print([node.value for node in circular_sll])
print("-"*100)

circular_sll.insert_node_csll(23, 2)
print([node.value for node in circular_sll])
print("-"*100)


circular_sll.insert_node_csll(67, 1)
print([node.value for node in circular_sll])
print("-"*100)

circular_sll.insert_node_csll(87, 3)
print([node.value for node in circular_sll])
print("-"*100)


circular_sll.insert_node_csll(99, 4)
print([node.value for node in circular_sll])
print("-"*100)



circular_sll.traversal_circular_sll()
print("-"*100)


print(circular_sll.search_node_circular_sll(34))
print("-"*100)

print(circular_sll.search_node_circular_sll(1223))
print("-"*100)

print([node.value for node in circular_sll])
circular_sll.delete_node_circular_sll(0)
print([node.value for node in circular_sll])
print("-"*100)



circular_sll.delete_node_circular_sll(1)
print([node.value for node in circular_sll])
print("-"*100)

circular_sll.delete_node_circular_sll(3)
print([node.value for node in circular_sll])
print("-"*100)

circular_sll.delete_circular_sll()
print([node.value for node in circular_sll])
print("-"*100)