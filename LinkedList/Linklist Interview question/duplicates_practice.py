from linked_list import LinkedList

ll = LinkedList()

# Remove duplicate node from the linked list7
# Time Complexity O(n)
def remove_duplicates(ll):
    curr_node = ll.head
    visited = {curr_node.value}

    while curr_node.next :
        if curr_node.next.value in visited:
            next_node = curr_node.next
            curr_node.next = next_node.next
        else:
            visited.add(curr_node.next.value)
            curr_node = curr_node.next
    return ll

# Without using any buffer
# Time Complexity O(n^2)
def remove_duplicates_without_buffer(ll):
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

ll.add(34)
ll.add(21)
ll.add(45)
ll.add(2781)
ll.add(34)
ll.add(67)
ll.add(21)


print(ll)

print(remove_duplicates(ll))

print(f"Without Buffer :- {remove_duplicates_without_buffer(ll)}")
