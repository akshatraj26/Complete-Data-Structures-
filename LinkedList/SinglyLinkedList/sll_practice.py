from intake.config import load_cond


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

    # Overriding the len method
    def __len__(self):
        node = self.head
        count = 0
        while node is not None:
            count += 1
            node = node.next
        return count

    # Insert a node at specific location
    # Time Complexity O(n)
    def insert_element(self, value, location):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node

        else:
            # Time Complexity O(1)
            if location == 0:
                new_node.next = self.head
                self.head = new_node
            # Time Complexity O(1)
            elif location == 1:
                new_node.next = None
                self.tail.next = new_node
                self.tail = new_node
            # Time Complexity O(N)
            # you can insert a node anywhere you want
            else:
                temp_node = self.head
                index = 0
                while index < location -1 :
                    # current node
                    temp_node = temp_node.next
                    index += 1
                next_node = temp_node.next
                temp_node.next = new_node
                new_node.next = next_node

    # Traversing all node of the SLL
    def traversing_element_sll(self):
        if self.head is None:
            print("This SLL does not exist.")
        else:
            node = self.head
            while node is not None:
                # print(node.value)
                print(f"| {node.value} | {id(node.next)} |")

                node = node.next

    # Searching a node in the Linked List
    # Time Complexity O(n)
    def search_element_sll(self, node_value):
        if self.head is None:
            return "SLL does not exist."

        else:
            node = self.head
            while node is not None:
                if node.value == node_value:
                    return node.value
                node = node.next
            return "The value does not exist in the SLL."

    # Deleting a node in the SLL

    def delete_element_sll(self, location):
        if self.head is None:
            return "SLL does not exist."
        else:
            if location == 0:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                else:

                    self.head =  self.head.next
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

            # Deleting a node from the anywhere in the sll
            else:
                temp_node = self.head
                index = 0

                while index < location - 1:
                    # current node
                    temp_node = temp_node.next
                    index += 1
                next_node = temp_node.next
                temp_node.next = next_node.next


    # Delete all the node from SLL
    def delete_sll(self):
        if self.head == self.tail:
            return "SLL does not exist."
        else:
            self.head = None
            self.tail = None









sll = SinglyLinkedList()
sll.insert_element(3, 0)
print([node.value for node in sll])
print("-"*100)

sll.insert_element(78, 0)
print([node.value for node in sll])
print("-"*100)

sll.insert_element(100, 1)
print([node.value for node in sll])
print("-"*100)

sll.insert_element(155, 1)
print([node.value for node in sll])
print("-"*100)

sll.insert_element(44, 2)
print([node.value for node in sll])
print("-"*100)


print(f"Length of the SLL :- {len(sll)}")
print("-"*100)


sll.traversing_element_sll()
print("-"*100)



print(sll.search_element_sll(100))
print("-"*100)


print(sll.search_element_sll(456))
print("-"*100)

print([node.value for node in sll])
sll.delete_element_sll(0)
print([node.value for node in sll])
print("-"*100)


sll.insert_element(2323, 3)
print([node.value for node in sll])
print("-"*100)


print([node.value for node in sll])
sll.delete_element_sll(1)
print([node.value for node in sll])
print("-"*100)


sll.insert_element(56, 3)
sll.insert_element(67, 0)
sll.insert_element(99, 1)
print([node.value for node in sll])
print("-"*100)


sll.delete_element_sll(4)
print([node.value for node in sll])
print("-"*100)


sll.delete_sll()
print([node.value for node in sll])
print("-"*100)