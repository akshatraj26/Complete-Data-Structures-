class PlateStack:
    def __init__(self, capacity):
        self.capacity =capacity
        self.stacks = []

    def push(self, item):
        if len(self.stacks) > 0 and len(self.stacks[-1]) < self.capacity:
            self.stacks[-1].append(item)
        else:
            self.stacks.append([item])

    def pop(self):
        while len(self.stacks) and len(self.stacks[-1]) == 0:
            self.stacks.pop()
        if len(self.stacks) == 0:
            return "There is no element in the stack"
        else:
            return self.stacks[-1].pop()

    def pop_at(self, stack_num):
        if len(self.stacks[stack_num]) > 0:
            return self.stacks[stack_num].pop()
        else:
            return "There is no any element"


plate_stack = PlateStack(3)
plate_stack.push(545)
plate_stack.push(45)
plate_stack.push(80)
plate_stack.push(89)
plate_stack.push(98)
plate_stack.push(23)

print(plate_stack.pop())
print(plate_stack.pop())
# print(plate_stack.pop())
print(plate_stack.pop_at(1))
