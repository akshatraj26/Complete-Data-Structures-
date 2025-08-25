from queue import Queue

class BinaryNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.heap_size = 0


class Heap:
    def __init__(self, root):
        self.root = BinaryNode(root)

    def in_order_traversal(self, root_node):
        if root_node:
            self.in_order_traversal(root_node.left)
            print(root_node.data, end=" | ")
            self.in_order_traversal(root_node.right)

    def pre_order_traversal(self, root_node):
        if root_node:
            print(root_node.data, end=" | ")
            self.pre_order_traversal(root_node.left)
            self.pre_order_traversal(root_node.right)

    def post_order_traversal(self, root_node):
        if root_node:
            self.post_order_traversal(root_node.left)
            self.post_order_traversal(root_node.right)
            print(root_node.data, end=" | ")

    def level_order_traversal(self, root_node):
        if root_node:
            queue = Queue()
            queue.enqueue(root_node)
            while not queue.is_empty():
                root = queue.dequeue()
                print(root.data, end=" | ")
                if root.left:
                    queue.enqueue(root.left)
                if root.right:
                    queue.enqueue(root.right)
        else:
            print("Heap Tree is empty")

    # Time Complexity O(1)
    # Space Complexity O(1)
    # Return the root node
    def peek(self, root_node):
        if not root_node:
            return "The Heap tree is empty"
        else:
            return root_node.data

    # Time Complexity O(1)
    # Space Complexity O(1)
    def heap_size(self, root_node):
        if root_node.heap_size == 0:
            return "Heap is empty"
        else:
            return root_node.heap_size

    # Heapify Insert
    def heapify_insert(self, root_node, heap_type):
        pass




heap = Heap(34)
print(heap.peek(heap.root))

