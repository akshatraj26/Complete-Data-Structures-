class MultiStack:
    def __init__(self, stack_size):
        self.no_stack = 3
        self.stack_size = stack_size
        self.custlist = [0] * (self.no_stack * self.stack_size)
        self.sizes = [0] * self.no_stack

    def __str__(self):
        lis = [str(x) for x in self.custlist]
        return " ".join(lis)

    def is_full(self, stack_num):
        if self.sizes[stack_num] == self.stack_size:
            return True
        else:
            return False

    def is_empty(self, stack_num):
        if self.sizes[stack_num] == 0:
            return True
        else:
            return False

    def index_of_top(self, stack_num):
        offset = stack_num * self.stack_size
        return offset + self.sizes[stack_num] - 1

    def push(self, item, stack_num):
        if self.is_full(stack_num):
            return "The Stack is full"
        else:
            self.sizes[stack_num] += 1
            self.custlist[self.index_of_top(stack_num)] = item

    def pop(self, stack_num):
        if self.is_empty(stack_num):
            return 'This stack is empty'
        else:
            value = self.custlist[self.index_of_top(stack_num)]
            self.custlist[self.index_of_top(stack_num)] = 0
            self.sizes[stack_num] -= 1

            return value

    def peek(self, stack_num):
        if self.is_empty(stack_num):
            return "The Stack is empty"
        else:
            value = self.custlist[self.index_of_top(stack_num)]
            return value

multi_stack = MultiStack(4)
print("-"*100)
print(multi_stack.is_empty(0))
print(multi_stack.is_full(0))
print("-"*100)
multi_stack.push(45, 0)
print(f"After Adding element in 1st stack: - {multi_stack.is_empty(0)}")

multi_stack.push(34, 1)
multi_stack.push(76, 1)
multi_stack.push(89, 1)
multi_stack.push(98, 1)
print(multi_stack.is_full(1))

print(multi_stack.pop(1))
print(f"After Adding element in 2nd stack: - {multi_stack.is_empty(1)}")

print(f"{multi_stack.is_empty(2)}")

print(multi_stack)


