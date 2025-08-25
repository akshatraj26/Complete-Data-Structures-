

from queue import Queue

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def __str__(self):
        return self.data

class BinaryTree:
    def __init__(self, root):
        self.root = Node(root)

    def __str__(self):
        if self.root:
            queue = Queue()
            queue.enqueue(self.root)
            while not queue.is_empty():
                root = queue.dequeue()
                print(str(root.data), end=" | ")
                if root.left:
                    queue.enqueue(root.left)
                if root.right:
                    queue.enqueue(root.right)
        else:
            return


    # root node -> left node -> right node
    # Time Complexity O(n)
    # Space Complexity O(n)
    def pre_order_traversal(self, node):
        if node:
            print(node.data, end = " | ")
            self.pre_order_traversal(node.left)
            self.pre_order_traversal(node.right)

    # left node -> root node -> right node
    # Time Complexity O(n)
    # Space Complexity O(n)
    def in_order_traversal(self, node):
        if node:
            self.in_order_traversal(node.left)
            print(node.data, end = " | ")
            self.in_order_traversal(node.right)

    # left node -> right node -> root node
    # Time Complexity O(n)
    # Space Complexity O(n)
    def post_order_traversal(self, node):
        if node:
            self.post_order_traversal(node.left)
            self.post_order_traversal(node.right)
            print(node.data, end = " | ")

    # Time Complexity O(n)
    # Space Complexity O(1)
    def level_order_traversal(self, node):
        if node:
            queue = Queue()
            queue.enqueue(node)
            while not queue.is_empty():
                root = queue.dequeue()
                print(root.data, end = " | ")
                if root.left:
                    queue.enqueue(root.left)
                if root.right:
                    queue.enqueue(root.right)
        else:
            return

    # Time Complexity O(n)
    def search_node(self, node, node_value):
        if not node:
            return "Binary Tree does not exist."
        else:
            queue = Queue()
            queue.enqueue(node)
            while not queue.is_empty():
                root = queue.dequeue()
                if root.data == node_value:
                    return "Success"
                if root.left:
                    queue.enqueue(root.left)
                if root.right:
                    queue.enqueue(root.right)
            return "Not Found"

    # Time Complexity O(n)
    # Space Complexity O(n)
    def insert_node(self, root_node, new_node):
        if not root_node:
            root_node = new_node

        else:
            queue = Queue()
            queue.enqueue(root_node)
            while not queue.is_empty():
                root = queue.dequeue()
                if root.left:
                    queue.enqueue(root.left)
                else:
                    root.left = new_node
                    return "Successfully inserted"
                if root.right:
                    queue.enqueue(root.right)
                else:
                    root.right = new_node
                    return "Successfully inserted"

    # Time Complexity O(n)
    # Space Complexity O(n)
    def get_deepest_node(self, root_node):
        if root_node:
            queue = Queue()
            queue.enqueue(root_node)
            while not queue.is_empty():
                root = queue.dequeue()
                if root.left:
                    queue.enqueue(root.left)
                if root.right:
                    queue.enqueue(root.right)
            last_node = root
            return last_node
        else:
            return

    # Time Complexity O(n)
    # Space Complexity O(n)
    def delete_deepest_node(self, root_node, deep_node):
        root = None
        if root_node:
            queue = Queue()
            queue.enqueue(root_node)
            while not(queue.is_empty()):
                root = queue.dequeue()
                if root is deep_node:
                    root.data = None
                    return
                if root.left:
                    if root.left is deep_node:
                        root.left = None
                        return
                    else:
                        queue.enqueue(root.left)

                if root.right:
                    if root.right is deep_node:
                        root.right = None
                        return
                    else:
                        queue.enqueue(root.right)
        else:
            return

    # Time Complexity O(n)
    # Space Complexity O(n)
    def delete_node(self, root_node, node):
        if not root_node:
            return "The BT does not exist"
        else:
            queue = Queue()
            queue.enqueue(root_node)
            while not queue.is_empty():
                root = queue.dequeue()
                if root.data == node:
                    d_node = self.get_deepest_node(root_node)
                    print("Last Node:- ",d_node)
                    root.data = d_node.data
                    self.delete_deepest_node(root_node, d_node)
                    return "The Node has been deleted successfully."

                if root.left:
                    queue.enqueue(root.left)
                if root.right:
                    queue.enqueue(root.right)
            return "Failed to delete"

    # Time Complexity O(1)
    # Space Complexity O(1)
    def delete_tree(self, root_node):
        root_node.data = None
        root_node.left = None
        root_node.right = None



binarytree = BinaryTree('Drinks')
binarytree.root.left = Node('Hot')
binarytree.root.right = Node('Cold')
binarytree.root.left.left = Node("Tea")
binarytree.root.left.right = Node("Coffee")
binarytree.root.right.left = Node("Alcoholic")
binarytree.root.right.right = Node("Non Alcoholic")

# print("Pre Order Traversal")
# binarytree.pre_order_traversal(binarytree.root)
#
#
# print("\nIn Order Traversal")
# binarytree.in_order_traversal(binarytree.root)
#
#
# print("\nPost Order Traversal")
# binarytree.post_order_traversal(binarytree.root)
#
#
# print("\nLevel Order Traversal")
# binarytree.level_order_traversal(binarytree.root)
#
# print("\n")
# print(binarytree.search_node(binarytree.root, "Tea"))
cola = Node("Cola")
beverages = Node("Beverages")

# Inserting a node
print(binarytree.insert_node(binarytree.root, cola))
print(binarytree.insert_node(binarytree.root, beverages))
binarytree.level_order_traversal(binarytree.root)


deepest_node = binarytree.get_deepest_node(binarytree.root)
print("\nDeepest node:- ", deepest_node)
# binarytree.delete_deepest_node(binarytree.root, deepest_node)


binarytree.delete_node(binarytree.root, 'Tea')
# print("\n")
binarytree.level_order_traversal(binarytree.root)