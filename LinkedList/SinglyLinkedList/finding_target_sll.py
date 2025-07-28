from dicionary.logn import target


class Node:
    def __init__(self, value = None):
        self.value = value
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head  = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node:
            yield  node
            node = node.next

    # Inserting the element in the sll
    def insert_sll(self, value, location):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            # inserting the element at the start of the sll
            # Time complexity O(1) at the start

            if location == 0:
                new_node.next = self.head
                self.head = new_node
            # inserting the element at the end of the sll
            elif location == 1:
                new_node.next = None
                self.tail.next = new_node
                self.tail  = new_node
            # Time complexity O(1) at the end

            # inserting the element at the specific location
            else:
                temp_node = self.head
                index = 0
                while index < location - 1:
                    # current node
                    temp_node = temp_node.next
                    index += 1
                next_node = temp_node.next
                temp_node.next = new_node
                new_node.next = next_node
            # Time complexity O(n)

    # Overriding the len
    def __len__(self):
        node = self.head
        count = 0
        while node is not None:
            count += 1
            node = node.next

        return count

    # Traversing the SLL
    def traversing_sll(self):
        node = self.head
        while node is not None:
            print(node.value)
            node = node.next
    # Time complexity O(n)


    # Finding the element in SLL. I will use Linear Search
    def search_sll(self, target):
        if self.head is None:
            return "There is no element in the SLL"
        else:
            node = self.head
            while node is not None:
                if node.value == target:
                    return node.value
                node = node.next
            return "The Element does not exist in the SLL"
    # Time complexity O(n)






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
print(sll.search_sll(45))
