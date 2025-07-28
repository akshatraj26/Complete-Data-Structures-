from linked_list import LinkedList

ll = LinkedList()
ll.add(23)
ll.add(34)
ll.add(23)
ll.add(89)
ll.add(34)

print(f"Linked List:- {ll}")

set1 = set()

def remove_duplicates(ll):
    # Remove the duplicates from the Linked List
    # Time Complexity O(n)
    if ll.head is None:
        return
    else:
        curr_node = ll.head
        visited = {curr_node.value}

        while curr_node.next:
            next_node = curr_node.next
            if curr_node.next.value in visited:
                curr_node.next = next_node.next
            else:
                visited.add(next_node.value)
                curr_node = curr_node.next
        return ll


def remove_duplicates_without_buffer(ll):
    if ll.head is None:
        return
    curr_node = ll.head
    while curr_node:
        runner = curr_node
        while runner.next:
            if runner.next.value == curr_node.value:
                next_node = runner.next
                runner.next = next_node.next
            else:
                runner = runner.next
        curr_node = curr_node.next
    return ll


print(remove_duplicates(ll))

print(f"Without Buffer :- {remove_duplicates_without_buffer(ll)}")