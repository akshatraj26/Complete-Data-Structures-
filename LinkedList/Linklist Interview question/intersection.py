"""
Given two (singly) linked lists, determine if the two lists intersect. Return the intersecting node.
Note that the intersection is defined based on reference, not value. That is, if the kth node of
the first linked list is the exact same node (by reference) as the jth node of the second linked list.
then they are intersecting.
"""

from linked_list import LinkedList, Node

# Time Complexity O(A + B)
def intersection(llA, llB):
    if llA.tail is not llB.tail:
        return False
    lenA = len(llA)
    lenB = len(llB)
    longer = llA if lenA > lenB else llB
    shorter = llB if lenB < lenA else llA

    diff = len(longer) - len(shorter)
    longerNode = longer.head
    shorterNode = shorter.head

    for _ in range(diff):
        longerNode = longerNode.next

    while longerNode is not shorterNode:
        longerNode = longerNode.next
        shorterNode = shorterNode.next
    return longerNode

# Add Helper Function
def addSameNode(llA, llB, value):
    new_node = Node(value)
    llA.tail.next = new_node
    llA.tail = new_node

    llB.tail.next = new_node
    llB.tail = new_node

llA = LinkedList()
llA.generate(3, 1, 9)
llB = LinkedList()
llB.generate(5, 1, 9)

print("Before Adding a Same Node")
print(f"Linked List A :- {llA}")
print(f"Linked List B :- {llB}")

addSameNode(llA, llB, 100)
addSameNode(llA, llB, 67)
addSameNode(llA, llB, 87)

print("After Adding a Same Node")
print(f"Linked List A :- {llA}")
print(f"Linked List B :- {llB}")

# Finding the Intersection Node
print(intersection(llA, llB))