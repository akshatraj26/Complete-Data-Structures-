class Node:
    def __init__(self, value= None):
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
            # Time complexity O(1)
            # Insert a node at the start
            if location == 0:
                new_node.next = self.head
                self.head = new_node

            # Insert a node at the end of the SLL
            # Time Complexity O(1)
            elif location == 1:
                new_node.next = None
                self.tail.next = new_node
                self.tail = new_node

            # Insert a node at the location
            # Time Complexity O(n)
            else:
                temp_node = self.head
                index = 0
                while index < location -1:
                    # Current node
                    temp_node = temp_node.next
                    index += 1
                next_node = temp_node.next
                temp_node.next = new_node
                new_node.next = next_node

    # Override the Len function
    def __len__(self):
        node = self.head
        count = 0
        while node is not None:
            count += 1
            node = node.next
        return count

    # Traverse all element in the SLL
    # Time complexity O(N)
    def traversing_sll(self):
        node = self.head
        while node is not None:
            print(node.value)
            node = node.next

    # Search a node
    # Time Complexity O(n)
    def search_element_sll(self, nodevalue):
        if self.head is None:
            return "This Singly Linked List(SLL) is empty."
        else:
            node = self.head
            while node is not None:
                if node.value == nodevalue:
                    return node.value
                node = node.next
            return "This element is not in the SLL"


    # Deleting a node from sll
    def delete_element_sll(self, location):
        if self.head is None:
            return "The SLL does not exist."
        else:

            if location == 0:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                else:
                    self.head = self.head.next

            elif location == 1:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                else:
                    node = self.head
                    while node is not None:
                        if node.next == self.tail:
                            break
                        node = node.next
                    node.next = None
                    self.tail = node

            else:
                temp_node = self.head
                index = 0
                while index < location - 1:
                    # current node
                    temp_node = temp_node.next
                    index += 1
                next_node = temp_node.next
                temp_node.next = next_node.next

    # Clear the SLL
    def delete_entire_sll(self):
        if self.head is None:
            return "SLL does not exist."
        else:
            self.head  = None
            self.tail = None





sll = SinglyLinkedList()
sll.insert_sll(12, 0)
sll.insert_sll(345, 0)
sll.insert_sll(88, 0)
sll.insert_sll(86, 0)
print([node.value for node in sll])
sll.insert_sll(34, 1)
sll.insert_sll(45, 1)
print([node.value for node in sll])
sll.insert_sll(478, 3)
print([node.value for node in sll])

print("-"*100)
print(f"Length of the SLL :-  {len(sll)}")
print("-"*100)
sll.traversing_sll()
print("-"*100)
print(sll.search_element_sll(45))

print("-"*100)
sll.delete_element_sll( 0)
print([node.value for node in sll])

print("-"*100)
sll.delete_element_sll( 0)
print([node.value for node in sll])



print("-"*100)
sll.delete_element_sll(1)
print([node.value for node in sll])


print("-"*100)
sll.delete_element_sll(2)
print([node.value for node in sll])

print("-"*100)
sll.delete_entire_sll()
print([node.value for node in sll])

