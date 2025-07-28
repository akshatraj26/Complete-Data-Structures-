'''
 Write code to partition a linked list around a value x,
        such that all nodes  less than x come before all nodes greater than or equal to x.

'''

from linked_list import LinkedList


ll = LinkedList()
ll.add(11)
ll.add(3)
ll.add(9)
ll.add(10)
ll.add(15)

print(ll)


def partition_linkedll(ll, x):
    curr_node = ll.head
    ll.tail = ll.head

    while curr_node:
        next_Node = curr_node.next
        curr_node.next = None
        if curr_node.value < x:
            curr_node.next = ll.head
            ll.head = curr_node
        else:
            ll.tail.next = curr_node
            ll.tail = curr_node
        curr_node = next_Node

    if ll.tail.next is not None:
        ll.tail.next = None

        #     ll.tail = current_node
        # else:
        #     current_node.next = None

    return ll

print(partition_linkedll(ll, 10))
