'''
 Write code to partition a linked list around a value x,
        such that all nodes  less than x come before all nodes greater than or equal to x.

'''

from linked_list import LinkedList


ll = LinkedList()
ll.generate(10, 0, 99)

print(ll)

def partition(ll, partition_value):
    curr_node = ll.head
    ll.tail = ll.head

    while curr_node:
        next_node = curr_node.next
        curr_node.next = None

        if curr_node.value < partition_value:
            curr_node.next = ll.head
            ll.head = curr_node
        else:
            curr_node.next = None
            ll.tail.next = curr_node
            ll.tail = curr_node
        curr_node = next_node

    if ll.tail.next is not None:
        ll.tail.next = None

partition(ll, 45)

print(ll)
