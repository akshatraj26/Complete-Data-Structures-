from linked_list import LinkedList

ll = LinkedList()

ll.add(45)
ll.add(55)
ll.add(66)
ll.add(76)
ll.add(56)
ll.add(45)
ll.add(56)

print(ll)

print(len(ll))
# print(ll[0])


def nth_last_node(ll, k):
    pointer1 = ll.head
    pointer2 = ll.head

    for i in range(k):
        if pointer2 is None:
            return None
        pointer2 = pointer2.next

    while pointer2:
        pointer1  = pointer1.next
        pointer2 = pointer2.next
    return pointer1


print(nth_last_node(ll, 3))

