class Heap:
    def __init__(self, size):
        # Time Complexity O(1)
        # Space Complexity O(n)
        self.cust_list = (size + 1) * [None]
        self.max_size = size + 1
        self.heap_size = 0
        self.last_index = 0

    # Time Complexity O(1)
    # Space Complexity O(1)
    def peek(self, root_node):
        if not root_node:
            return "Heap is empty"
        else:
            return self.cust_list[1]

    # Time Complexity O(1)
    # Space Complexity O(1)
    def size_of_heap(self, root_node):
        if not root_node:
            return
        else:
            return self.heap_size

    # Time Complexity O(n)
    # Space Complexity O(n)
    def level_order_traversal(self, root_node):
        if not root_node:
            return
        else:
            for i in range(1, root_node.heap_size+1):
                print(self.cust_list[i], end=" | ")

    # Time Complexity O(logn)
    # Space Complexity O(logn)
    def heapifytreeinsert(self, root_node, index, heap_type):
        parent_index = int(index / 2)
        if index <= 1:
            return
        if heap_type == 'Min':
            if root_node.cust_list[index] < root_node.cust_list[parent_index]:
                temp = root_node.cust_list[index]
                root_node.cust_list[index] = root_node.cust_list[parent_index]
                root_node.cust_list[parent_index] = temp
            self.heapifytreeinsert(root_node, parent_index, heap_type)


        elif heap_type == "Max":
            if root_node.cust_list[index] > root_node.cust_list[parent_index]:
                temp = root_node.cust_list[index]
                root_node.cust_list[index] = root_node.cust_list[parent_index]
                root_node.cust_list[parent_index] = temp

            self.heapifytreeinsert(root_node, parent_index, heap_type)


    # Inserting in the Heap Tree
    # Time Complexity O(n)
    # Space Complexity O(n)
    def insert_node(self, root_node, node_value, heap_type):
        if root_node.heap_size + 1 == root_node.max_size:
            return "The Binary Heap is full."
        root_node.cust_list[self.heap_size + 1] = node_value
        root_node.heap_size += 1
        self.heapifytreeinsert(root_node, root_node.heap_size, heap_type)
        return "The Value has been inserted successfully"


    def last_node(self):
        return self.cust_list[1]

    def heap_tree_extract(self, root_node, index, heap_type):
        left_index = 2 * index
        right_index = 2 * index + 1
        swap_child = 0
        if root_node.heap_size < left_index:
            return
        elif root_node.heap_size == left_index:
            if heap_type == "Min":
                if root_node.cust_list[index] > root_node.cust_list[left_index]:
                    temp = root_node.cust_list[index]
                    root_node.cust_list[index] = root_node.cust_list[left_index]
                    root_node.cust_list[left_index] = temp
                return
            else:
                if root_node.cust_list[index] < root_node.cust_list[right_index]:
                    temp = root_node.cust_list[index]
                    root_node.cust_list[index] = root_node.cust_list[right_index]
                    root_node.cust_list[right_index] = temp
                return

        else:
            if heap_type == "Min":
                if root_node.cust_list[left_index] < root_node.cust_list[right_index]:
                    swap_child = left_index
                else:
                    swap_child = right_index
                if root_node.cust_list[index] > root_node.cust_list[swap_child]:
                    temp = root_node.cust_list[index]
                    root_node.cust_list[index] = root_node.cust_list[swap_child]
                    root_node.cust_list[swap_child] = temp
            else:
                if root_node.cust_list[left_index] > root_node.cust_list[right_index]:
                    swap_child = left_index
                else:
                    swap_child = right_index
                if root_node.cust_list[index] < root_node.cust_list[swap_child]:
                    temp = root_node.cust_list[index]
                    root_node.cust_list[index] = root_node.cust_list[swap_child]
                    root_node.cust_list[swap_child] = temp
            self.heap_tree_extract(root_node, swap_child, heap_type)


    def extract_node(self, root_node, heap_type):
        if self.heap_size == 0:
            return "The Heap Tree is empty."
        else:
            extracted_node = root_node.cust_list[1]
            root_node.cust_list[1] = root_node.cust_list[self.heap_size]
            root_node.cust_list[self.heap_size] = None
            self.heap_size -= 1
            self.heap_tree_extract(root_node, 1, heap_type)
            return extracted_node


    # Time Complexity O(1)
    # Space Complexity O(1)
    def delete_entire_binary_heap(self, root_node):
        root_node.cust_list = None






heap = Heap(5)
print(heap.insert_node(heap, 5, "Max"))
print(heap.insert_node(heap, 1, "Max"))
print(heap.insert_node(heap, 2, "Max"))
print(heap.insert_node(heap, 6, "Max"))
heap.level_order_traversal(heap)

print("\n", heap.extract_node(heap, "Max"))
heap.level_order_traversal(heap)


heap.delete_entire_binary_heap(heap)
heap.level_order_traversal(heap)






