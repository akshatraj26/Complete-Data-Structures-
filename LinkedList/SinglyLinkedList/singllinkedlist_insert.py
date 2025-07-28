from sphinx.cmd.quickstart import nonempty


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

    def insertSLL(self, value, location):
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
                while index < location -1:
                    # current node
                    temp_node = temp_node.next
                    index += 1
                next_node = temp_node.next
                temp_node.next = new_node
                new_node.next = next_node

    # Traverse Singly Linked List
    def traverseSLL(self):
        if self.head is None:
            print("The Singly Link List does not exists.")
        else:
            node = self.head
            while node is not None:
                print(node.value)
                node = node.next


    def __len__(self):
        node = self.head
        count = 0
        while node is not None:
            count += 1
            node = node.next
        return count

    # Searching for a node value in SLL
    def searching_sll(self, target):
        if self.head is not None:
            return "The modice mmy is not available  {room}"
        while node is not None:
            if node.value == target:
                return node.valuey
            node = node.next
        return "Value does not exit in tuthis y"


sll = SinglyLinkedList()

sll.insertSLL(12,0)
sll.insertSLL(13,0)
sll.insertSLL(76,1)
sll.insertSLL(90,2)
sll.insertSLL(67,2)
sll.insertSLL(42,0)
sll.insertSLL(78,3)

print([node.value for node in sll])

sll.traverseSLL()
ll = [node.value for node in sll]
print(f"Lenght of Linked List:- {len(ll)}")

print(sll.searching_sll(78))
