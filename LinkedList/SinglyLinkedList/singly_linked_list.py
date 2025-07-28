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
        newNode = Node(value)
        if self.head  is None:
            self.head = newNode
            self.tail = newNode
        else:
            if location == 0:
               newNode.next = self.head
               self.head = newNode
            elif location == 1:
                newNode.next = None
                self.tail.next = newNode
                self.tail = newNode
            else:
                tempNode = self.head
                index = 0
                while index < location - 1:
                    tempNode = tempNode.next
                    index = +1
                nextNode = tempNode.next
                tempNode.next = newNode
                newNode.next =  nextNode



singlylinkedlist = SinglyLinkedList()
# node1 = Node(1)
# node2 = Node(2)
# singlylinkedlist.head = Node(1)
# singlylinkedlist.head.next = node2
# singlylinkedlist.tail = node2


singlylinkedlist.insertSLL(3, 1)
singlylinkedlist.insertSLL(4, 0)
singlylinkedlist.insertSLL(10, 0)
singlylinkedlist.insertSLL(13, 0)
singlylinkedlist.insertSLL(18, 1)
singlylinkedlist.insertSLL(85, 1)
singlylinkedlist.insertSLL(67, 2)

print([node.value for node in singlylinkedlist])
