from linked_list import LinkedList

ll1 = LinkedList()
ll1.add(7)
ll1.add(1)
ll1.add(6)
print(ll1)

ll2 = LinkedList()
ll2.add(5)
ll2.add(9)
ll2.add(2)
print(ll2)

# Time Complexity O(n)
# Space Complexity O(n)

def sum_linked_list(ll1, ll2):
    n1 = ll1.head
    n2 = ll2.head
    carry = 0
    ll = LinkedList()

    while n1 or n2:
        result = carry
        if n1:
            result += n1.value
            n1 = n1.next
        if n2:
            result += n2.value
            n2 = n2.next

        ll.add(int(result % 10))
        carry = int(result / 10)

    return ll

print(sum_linked_list(ll1, ll2))