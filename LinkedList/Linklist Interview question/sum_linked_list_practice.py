from sympy import resultant

from linked_list import LinkedList

ll1 = LinkedList()
# ll1.generate(3, 0, 9)
ll1.add(7)
ll1.add(1)
ll1.add(6)


ll2 = LinkedList()
ll2.add(5)
ll2.add(9)
ll2.add(2)


# ll2.generate(3, 0, 9)


def reverse_linked_list(ll):
    # Temporary linked list
    curr_node = ll.head
    stack = []

    while curr_node.next:
        stack.append(curr_node)
        curr_node = curr_node.next

    ll.head = curr_node

    while stack:
        curr_node.next = stack.pop()
        curr_node = curr_node.next

    curr_node.next = None

    return ll

def sum_linked_list(ll1, ll2):
    reverse_ll1 = reverse_linked_list(ll1)
    reverse_ll2 = reverse_linked_list(ll2)
    resultant = LinkedList()
    ll1_num, ll2_num = "", ""
    for node1, node2 in zip(reverse_ll1, reverse_ll2):
        ll1_num = str(node1.value) + ll1_num
        ll2_num = str(node2.value) + ll2_num
    sum_ll = str(int(ll1_num) + int(ll2_num))
    for element in sum_ll:
        resultant.add(element)
    return reverse_linked_list(resultant)

    # return reverse_ll1, reverse_ll2, sum_ll

# print(f"Linked List 1:- {ll1}")
# print(f"Linked List 2:- {ll2}")
print(f"Reverse LL1 :- {reverse_linked_list(ll1)}")
print(f"Reverse LL2 :- {reverse_linked_list(ll2)}")

# print(f"Linked List 1:- {ll1} | Reverse Linked List {sum_linked_list(ll1, ll2)[0]}" )
# print(f"Linked List 1:- {ll2} | Reverse Linked List {sum_linked_list(ll1, ll2)[1]}")
print(f"Sum Linked List:- {sum_linked_list(ll1, ll2)}")