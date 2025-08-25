from queue import Queue

class Node:
    def __init__(self, data = None):
        self.data = data
        self.left = None
        self.right = None
        self.height = 1

    def __str__(self):
        return str(self.data)

class AVLTree:
    def __init__(self, root):
        self.root = Node(root)

    # Level Order Traversal
    # Time Complexity O(n)
    # Space Complexity O(n)
    def level_order_traversal(self, root_node):
        if root_node:
            queue = Queue()
            queue.enqueue(root_node)
            while not queue.is_empty():
                root = queue.dequeue()
                print(root.data, end= " | ")
                if root.left:
                    queue.enqueue(root.left)
                if root.right:
                    queue.enqueue(root.right)
        else:
            return "This AVL Tree is empty."

    # Searching a node in the AVL Tree
    def search(self, root_node, node_value):
        if root_node:
            if root_node.data == node_value:
                return "The Value is found in the AVL Tree."
            elif node_value < root_node.data:
                if node_value.left:
                    if root_node.left.data == node_value:
                        return "Value is found in the AVL Tree."
                    else:
                        self.search(root_node.left, node_value)
                else:
                    return "Value is not found in the AVL Tree."
            else:
                if root_node.right:
                    if root_node.right.data == node_value:
                        return "Value is found in the AVL Tree."
                    else:
                        self.search(root_node.right, node_value)
                else:
                    return "Value is not found in the AVL Tree."
        else:
            return "This AVL Tree is empty."


    def get_height(self, root_node):
        if not root_node:
            return 0
        return root_node.height


    def rotate_right(self, disbalanced_node):
        new_root = disbalanced_node.left
        disbalanced_node.left = disbalanced_node.left.right
        new_root.right = disbalanced_node
        # Update height of disbalanced node and new root
        disbalanced_node.height = 1 + max(self.get_height(disbalanced_node.left), self.get_height(disbalanced_node.right))
        new_root.height = 1 + max(self.get_height(new_root.left), self.get_height(new_root.right))

        return new_root

    def rotate_left(self, disbalanced_node):
        new_root = disbalanced_node.right
        disbalanced_node.right = disbalanced_node.right.left
        new_root.left = disbalanced_node
        # Update height of disbalanced node and new root
        disbalanced_node.height = 1 + max(self.get_height(disbalanced_node.left), self.get_height(disbalanced_node.right))
        new_root.height = 1 + max(self.get_height(new_root.left), self.get_height(new_root.right))
        return new_root

    def get_balance(self, root_node):
        if not root_node:
            return 0
        return self.get_height(root_node.left) - self.get_height(root_node.right)


    def insert_node(self, root_node, node_value):
        if not root_node:
            return Node(node_value)
        elif node_value < root_node.data:
            root_node.left = self.insert_node(root_node.left, node_value)
        else:
            root_node.right = self.insert_node(root_node.right, node_value)

        root_node.height = 1 + max(self.get_height(root_node.left), self.get_height(root_node.right))
        balance = self.get_balance(root_node)
        # Left left
        if balance > 1 and node_value < root_node.left.data:
            return self.rotate_right(root_node)

        # Left Right
        if balance > 1 and node_value > root_node.left.data:
            root_node.left = self.rotate_left(root_node.left)
            return self.rotate_right(root_node)

        # Right right
        if balance < -1 and node_value > root_node.right.data:
            return self.rotate_left(root_node)

        # Right left
        if balance < -1 and node_value < root_node.right.data:
            root_node.right = self.rotate_right(root_node.right)
            return self.rotate_left(root_node)

        return root_node


    def get_minimum(self, root_node):
        if root_node is None or root_node.left is None:
            return root_node
        return self.get_minimum(root_node.left)

    def delete_node(self, root_node, node_value):
        if not root_node:
            print("Root node has been checked")
            return root_node
        elif node_value < root_node.data:
            root_node.left = self.delete_node(root_node.left, node_value)
        elif node_value > root_node.data:
            root_node.right = self.delete_node(root_node.right, node_value)
        # root node has one child
        else:
            if root_node.left is None:
                temp = root_node.right
                root_node = None
                return temp
            elif root_node.right is None:
                temp = root_node.left
                root_node = None
                return temp
            # If root has 2 child
            successor = self.get_minimum(root_node.right)
            # tricky line root_node.data
            root_node.data = successor
            root_node.right = self.delete_node(root_node.right, successor.data)

        # When the rotation is required
        balance = self.get_balance(root_node)
        # LL condition
        if balance > 1 and self.get_balance(root_node.left) >= 0:
            return self.rotate_right(root_node)
        # RR
        if balance < -1 and self.get_balance(root_node.right) <= 0:
            return self.rotate_left(root_node)
        # Left Right condition
        if balance > 1 and self.get_balance(root_node.left) < 0:
            root_node.left = self.rotate_left(root_node.left)
            return self.rotate_right(root_node)
        # Right Left Condition
        if balance < -1 and self.get_balance(root_node.right) > 0:
            root_node.right = self.rotate_right(root_node.right)
            return self.rotate_left(root_node)
        return root_node

    def delete_entire_tree(self, root_node):
        if root_node is None:
            return "Why destroy an empty castle."
        else:
            root_node.data = None
            root_node.left = None
            root_node.right = None
            return "AVL Tree deletion is successfully done"



avl_tree = AVLTree(5)
avl_tree.root = avl_tree.insert_node(avl_tree.root, 10)
avl_tree.root = avl_tree.insert_node(avl_tree.root, 15)
avl_tree.root = avl_tree.insert_node(avl_tree.root, 20)
avl_tree.root = avl_tree.insert_node(avl_tree.root, 25)


print(avl_tree.search(avl_tree.root, 20))

print("\n" + "-"*100)
print(avl_tree.get_minimum(avl_tree.root))
print(f"Before Deleting {avl_tree.level_order_traversal(avl_tree.root)}")
# print("\n")
avl_tree.delete_node(avl_tree.root, 10)

print(f"After Deleting {avl_tree.level_order_traversal(avl_tree.root)}")


print(avl_tree.delete_entire_tree(avl_tree.root))

avl_tree.level_order_traversal(avl_tree.root)

print(avl_tree.delete_entire_tree(avl_tree.root))

