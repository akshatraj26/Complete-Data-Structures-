from linked_list import LinkedList

ll = LinkedList()

ll.generate(10, 10, 99)
print(ll)

def nth_to_last_node(ll, n):
    pointer1 = ll.head
    pointer2 = ll.head

    for _ in range(n):
        if pointer2 is None:
            return None
        pointer2 = pointer2.next

    while pointer2:
        pointer1 = pointer1.next
        pointer2 = pointer2.next
    return pointer1

print(nth_to_last_node(ll, 4))