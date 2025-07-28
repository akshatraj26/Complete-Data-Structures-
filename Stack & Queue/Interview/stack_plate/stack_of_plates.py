"""
Imagine a (literal) stack of plates. If the stack gets too high, it might topple.
Therefore, in real life, we would likely start a new stack when the previous stack exceeds some threshold.
Implement a data structure SetOfStacks that mimics this. SetOfStacks should be composed of several stacks
 and should create a new stack once the previous one exceeds capacity, SetOfStacks.push() and SetOfStacks.pop()
should behave identically to a single stack (that is, pop() should return the same values as it would if
 there were just a single stack).

Follow Up:
Implement a function popAt (int index) which performs a pop operation on a specific substack.
"""

class PlateStack:
    def __init__(self, capacity):
        self.capacity = capacity
        self.stacks = []

    def __str__(self):
        return self.stacks

    def push(self, item):
        if len(self.stacks)> 0 and (len(self.stacks[-1])) <  self.capacity:
            self.stacks[-1].append(item)
        else:
            self.stacks.append([item])

    def pop(self):
        while len(self.stacks) and len(self.stacks[-1]) == 0:
            return self.stacks.pop()
        if len(self.stacks) == 0:
            return None
        else:
            return self.stacks[-1].pop()


    def pop_at(self, stack_number):
        if len(self.stacks[stack_number]) > 0:
            return self.stacks[stack_number].pop()
        else:
            return "No element in the Stack"

stack = PlateStack(4)
stack.push(3)
stack.push(6)
stack.push(5)
stack.push(8)
stack.push(9)
stack.push(8)

print(stack.pop())
print(stack.pop_at(1))
# print(stack)

