"""
You have two numbers represented by a linked list, where each node contains a single digit.
The digits are stored in reverse order, such that the 1's digit is at the head of the list.
Write a functions that the two numbers and returns the sum as a linked list.
"""

from linked_list import LinkedList

ll1 = LinkedList()

ll1.add(7)
ll1.add(1)
ll1.add(6)

# number 617
print(ll1)

ll2 = LinkedList()
ll2.add(5)
ll2.add(9)
ll2.add(2)
print(ll2)
# 295
# add 295 + 617
print(295+617)
# Sum linked list 2 -> 1 -> 9

def sum_ll(ll1, ll2):
    n1 = ll1.head
    n2 = ll2.head
    carry = 0
    ll = LinkedList()

    while n1 or n2:
        result = carry
        print(f"Carry {carry}")
        if n1:
            result += n1.value
            print("Result1:- ", result)
            n1 = n1.next
        if n2:
            result += n2.value
            print("Result2:- ", result)

            n2 = n2.next
        print(f"Overall :- {result}")
        ll.add(int(result % 10))
        carry = int(result / 10)

    return ll

print(sum_ll(ll1, ll2))