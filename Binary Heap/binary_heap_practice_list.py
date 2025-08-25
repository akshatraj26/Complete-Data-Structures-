class Heap:
    def __init__(self, size):
        # Time Complexity O(1)
        # Space Complexity O(n)
        self.cuslist = (size + 1) * [None]
        self.max_size = size + 1
        self.heap_size = 0
        self.last_used_index = 0

    # Time Complexity O(1)
    # Space Complexity O(1)
    def peek(self):
        if self.heap_size == 0:
            return "Heap is empty"
        else:
            return self.cuslist[1]

    # Time Complexity O(1)
    # Space Complexity O(1)
    def size_of_heap(self):
        if self.heap_size == 0:
            return "Heap has no element."
        return self.heap_size

    def level_order_traversal(self):
        if self.heap_size == 0:
            return
        else:
            for index in range(1, self.heap_size + 1):
                print(self.cuslist[index], end=" | ")

    # Time Complexity O(n)
    # Space Complexity O(n)
    def in_order_traversal(self, index):
        if index > self.last_used_index:
            return
        self.in_order_traversal(2 * index)
        print(self.cuslist[index])
        self.in_order_traversal(index * 2 + 1)
    # Time Complexity O(n)
    # Space Complexity O(n)
    def pre_order_traversal(self, index):
        if index > self.last_used_index:
            return
        print(self.cuslist[index])
        self.pre_order_traversal(index * 2)
        self.pre_order_traversal(index * 2 + 1)

    # Time Complexity O(n)
    # Space Complexity O(n)
    def post_order_traversal(self, index):
        if index > self.last_used_index:
            return
        self.post_order_traversal(index * 2)
        self.post_order_traversal(index * 2 + 1)
        print(self.cuslist[index])


    # Time Complexity O(n)
    # Space Complexity O(n)
    def heapify_insert(self, index, heap_type):
        parent_index = int(index / 2)
        if index <= 1:
            return
        if heap_type == 'Min':
            if self.cuslist[index] < self.cuslist[parent_index]:
                temp = self.cuslist[index]
                self.cuslist[index] = self.cuslist[parent_index]
                self.cuslist[parent_index] = temp
            self.heapify_insert(parent_index, heap_type)

        elif heap_type == "Max":
            if self.cuslist[index] > self.cuslist[parent_index]:
                temp = self.cuslist[index]
                self.cuslist[index] = self.cuslist[parent_index]
                self.cuslist[parent_index] = temp
            self.heapify_insert(parent_index, heap_type)

    def insert_node(self, node_value, heap_type):
        if self.heap_size + 1 == self.max_size:
            return "The Heap Tree is full."
        self.cuslist[self.heap_size + 1] = node_value
        self.heap_size += 1
        self.last_used_index += 1
        self.heapify_insert(self.heap_size, heap_type)
        return "The Node has been successfully inserted"


    def heapify_extract(self, index, heap_type):
        left_index = 2 * index
        right_index = index * 2 + 1
        swap_child = 0
        # No child in the Heap Tree
        if self.heap_size < left_index:
            return
        # When only left child
        elif self.heap_size == left_index:
            if heap_type == 'Min':
                # If there is only left index
                if self.cuslist[index] > self.cuslist[left_index]:
                    temp = self.cuslist[index]
                    self.cuslist[index] = self.cuslist[left_index]
                    self.cuslist[left_index] = temp
                return
            else:
                # If there is only right index
                if self.cuslist[index] < self.cuslist[left_index]:
                    temp = self.cuslist[index]
                    self.cuslist[index] = self.cuslist[left_index]
                    self.cuslist[left_index] = temp
                return


        # If Both child is available
        else:
            if heap_type == "Min":
                if self.cuslist[left_index] < self.cuslist[right_index]:
                    swap_child = left_index
                else:
                    swap_child = right_index
                if self.cuslist[index] > self.cuslist[swap_child]:
                    temp = self.cuslist[index]
                    self.cuslist[index] = self.cuslist[swap_child]
                    self.cuslist[swap_child] = temp
            else:
                if self.cuslist[left_index] > self.cuslist[right_index]:
                    swap_child = left_index
                else:
                    swap_child = right_index
                if self.cuslist[index] < self.cuslist[swap_child]:
                    temp = self.cuslist[index]
                    self.cuslist[index] = self.cuslist[swap_child]
                    self.cuslist[swap_child] = temp
            self.heapify_insert(swap_child, heap_type)

    # Time Complexity O(logn)
    # Space Complexity O(logn)
    def extract_node(self, heap_type):
        if self.heap_size == 0:
            return "The Heap Tree is empty"
        else:
            extracted_node = self.cuslist[1]
            self.cuslist[1] = self.cuslist[self.heap_size]
            self.cuslist[self.heap_size] = None
            self.heap_size -= 1
            self.heapify_extract(1, heap_type)
            return extracted_node

    def delete_entire_heap(self):
        self.cuslist = None
        return  "Successfully deletion of the Heap Tree."




heap = Heap(5)
print(heap.peek())

print(heap.size_of_heap())

heap.insert_node(56, "Max")
heap.insert_node(34, "Max")
heap.insert_node(78, "Max")
heap.insert_node(2, "Max")
print(heap.insert_node(45, "Max"))
print(heap.insert_node(34, "Max"))


heap.level_order_traversal()



print(heap.extract_node( 'Max'))

heap.level_order_traversal()


print(heap.delete_entire_heap())
heap.level_order_traversal()


