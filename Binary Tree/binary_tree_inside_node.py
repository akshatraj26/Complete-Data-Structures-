from boltons.urlutils import quote_query_part

from queue import Queue

class BinaryNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def __str__(self):
        return self.value


    # root node -> left node -> right node
    # Time Complexity O(n)
    # Space Complexity O(n)
    def pre_order_traversal(self):

        print(self.value, end= " | ")

        if self.left:
            self.left.pre_order_traversal()

        if self.right:
            self.right.pre_order_traversal()

    # left node -> root node -> right node
    # Time Complexity O(n)
    # Space Complexity O(n)
    def in_order_traversal(self):
        if self.left:
            self.left.in_order_traversal()
        print(self.value, end=" | ")
        if self.right:
            self.right.in_order_traversal()

    # left node -> right node -> root node
    # Time Complexity O(n)
    # Time Complexity O(n)
    def post_order_traversal(self):
        if self.left:
            self.left.post_order_traversal()
        if self.right:
            self.right.post_order_traversal()
        print(self.value, end=" | ")

    # Level Order Traversal
    def level_order_traversal(self):
        queue = Queue()
        queue.enqueue(self)
        while not queue.is_empty():
            root = queue.dequeue()
            print(root.value, end= " | ")
            if root.left:
                queue.enqueue(root.left)
            if root.right:
                queue.enqueue(root.right)

    # Searching
    # Time Complexity O(n)
    # Space Complexity O(n)
    def searching(self, target):
        queue = Queue()
        queue.enqueue(self)
        while not queue.is_empty():
            root = queue.dequeue()
            if root.value == target:
                return  f"Target found {root.value}"
            if root.left:
                queue.enqueue(root.left)
            if root.right:
                queue.enqueue(root.right)

        return  "Not Found"

    # Time Complexity O(n)
    # Space Complexity O(n)
    def insert_node(self, new_data):
        new_node = BinaryNode(new_data)
        if not self:
            self = new_node
        else:
            queue = Queue()
            queue.enqueue(self)
            while not queue.is_empty():
                root = queue.dequeue()
                if root.left:
                    queue.enqueue(root.left)
                else:
                    root.left = new_node
                    return "Successfully added"
                if root.right:
                    queue.enqueue(root.right)

                else:
                    root.right = new_node
                    return "Successfully added"

    # Time Complexity O(n)
    # Space Complexity O(n)
    # Get the deepest node
    def get_deepest_node(self):
        queue = Queue()
        queue.enqueue(self)
        while not queue.is_empty():
            root = queue.dequeue()
            if root.left:
                queue.enqueue(root.left)
            if root.right:
                queue.enqueue(root.right)
        deep_node = root
        return deep_node

    # Time Complexity O(n)
    # Space Complexity O(n)
    def delete_deepest_node(self, delete_node):
        if self:
            queue = Queue()
            queue.enqueue(self)
            while not queue.is_empty():
                root = queue.dequeue()
                if root is delete_node:
                    root = None
                    return
                if root.left:
                    if root.left is delete_node:
                        root.left = None
                        return
                    else:
                        queue.enqueue(root.left)
                if root.right:
                    if root.right is delete_node:
                        root.right = None
                        return
                    else:
                        queue.enqueue(root.right)
            return "Failed to delete"

    # Time Complexity O(n)
    # Space Complexity O(n)
    def delete_node(self, node):
        if self:
            queue = Queue()
            queue.enqueue(self)
            while not queue.is_empty():
                root = queue.dequeue()
                if root.value is node:
                    d_node = self.get_deepest_node()
                    root.value = d_node.value
                    self.delete_deepest_node(d_node)
                    return "The Node has been deleted successfully"
                if root.left:
                    queue.enqueue(root.left)
                if root.right:
                    queue.enqueue(root.right)
            return "Failed to delete"

    # Time Complexity O(1)
    # Space Complexity O(1)
    def delete_tree(self):
        self.value = None
        self.right = None
        self.left = None



class BinaryTree:
    def __init__(self, root):
        self.root = BinaryNode(root)

    def __str__(self):
        return self.root


binarytree = BinaryTree('Drinks')
binarytree.root.left = BinaryNode('Hot')
binarytree.root.right = BinaryNode('Cold')
binarytree.root.left.left = BinaryNode("Tea")
binarytree.root.left.right = BinaryNode("Coffee")
binarytree.root.right.left = BinaryNode("Alcoholic")
binarytree.root.right.right = BinaryNode("Non Alcoholic")

# print(binarytree)
print("\nPre Order Traversal")
binarytree.root.pre_order_traversal()
print("\nIn Order Traversal")
binarytree.root.in_order_traversal()
print("\nPost Order Traversal")
binarytree.root.post_order_traversal()
print("\nLevel Order Traversal")
binarytree.root.level_order_traversal()


print("\n")
print(binarytree.root.searching('Tea'))

# Inserting a node
print(binarytree.root.insert_node("Cola"))
print(binarytree.root.insert_node("Beverages"))
binarytree.root.level_order_traversal()


print("\n")
print(f"Deepest Node:- {binarytree.root.get_deepest_node()}")

deepest_node = binarytree.root.get_deepest_node()

# binarytree.root.delete_deepest_node(deepest_node)

binarytree.root.delete_node("Tea")
binarytree.root.level_order_traversal()
binarytree.root.delete_node("Drinks")
print("\n")
binarytree.root.level_order_traversal()

print("\n")
binarytree.root.delete_tree()
binarytree.root.level_order_traversal()







