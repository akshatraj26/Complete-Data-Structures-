from queue import Queue

class AVLTree:
    def __init__(self, data = None):
        self.data = data
        self.left = None
        self.right = None
        self.height = 1


    def __str__(self):
        return str(self.data)



# Traversing the node in the avl
# Pre Order Traversal :- root node -> left node -> right node
# Time Complexity O(n)
# Space Complexity O(n)
def pre_order_traversal(root_node):
    if root_node:
        print(root_node.data, end= " | ")
        pre_order_traversal(root_node.left)
        pre_order_traversal(root_node.right)
    else:
        print("There is no element to traverse")

# In Order Traversal :- left node -> root node -> right node
# Time Complexity O(n)
# Space Complexity O(n)
def in_order_traversal( root_node):
    if root_node:
        in_order_traversal(root_node.left)
        print(root_node.data, end= " | ")
        in_order_traversal(root_node.right)
    else:
        print("There is no element to traverse")

# Post Order Traversal :- left node -> right node -> root node
# Time Complexity O(n)
# Space Complexity O(n)
def post_order_traversal( root_node):
    if root_node:
        post_order_traversal(root_node.left)
        post_order_traversal(root_node.right)
        print(root_node.data, end= " | ")
    else:
        print("There is no element to traverse")

# Level Order Traversal
# Time Complexity O(n)
# Space Complexity O(n)
def level_order_traversal( root_node):
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


# Searching of a node in AVL tree
# Time Complexity O(logn)
# Space Complexity O(logn)
def search( root_node, node_value):
    if root_node:
        if node_value == root_node.data:
            return "The value is found in the AVL Tree"
        elif node_value < root_node.data:
            if root_node.left:
                if root_node.left.data == node_value:
                    return "The value is found in the AVL Tree"
                else:
                    search(root_node.left, node_value)
            else:
                return "This value is not available in the AVL Tree"
        else:
            if root_node.right:
                if root_node.right.data == node_value:
                    return "The value is found in the AVL Tree"
                else:
                    search(root_node.right, node_value)
            else:
                return "This value is not available in the AVL Tree"


def get_height(root_node):
    if root_node:
        return root_node.height
    return 0


def rotate_right( disbalanced_node):

    new_root = disbalanced_node.left
    disbalanced_node.left = disbalanced_node.left.right
    new_root.right = disbalanced_node
    # Update height of disbalanced node and new root
    disbalanced_node.height = 1 + max(get_height(disbalanced_node.left), get_height(disbalanced_node.right))
    new_root.height = 1 + max(get_height(new_root.letf), get_height(new_root.right))

    return new_root

def rotate_left( disbalanced_node):
    new_root = disbalanced_node.right
    disbalanced_node.right = disbalanced_node.right.left
    new_root.left = disbalanced_node
    # Update height of disbalanced node and new root
    disbalanced_node.height = 1 + max(get_height(disbalanced_node.left), get_height(disbalanced_node.right))
    new_root.height = 1 + max(get_height(new_root.left), get_height(new_root.right))
    return new_root

def get_balance(root_node):
    if not root_node:
        return 0
    return get_height(root_node.left) - get_height(root_node.right)


def insert_node(root_node, node_value):
    if not root_node:
        return AVLTree(node_value)
    elif node_value < root_node.data:
        root_node.left = insert_node(root_node.left, node_value)
    else:
        root_node.right = insert_node(root_node.right, node_value)

    root_node.height = 1 + max(get_height(root_node.left), get_height(root_node.right))
    balance = get_balance(root_node)
    if balance > 1 and node_value < root_node.left.data:
        return rotate_right(root_node)

    if balance > 1 and node_value > root_node.left.data:
        root_node.left = rotate_left(root_node.left)
        return rotate_right(root_node)

    if balance < -1 and node_value > root_node.right.data:
        return rotate_left(root_node)
    if balance < -1 and node_value < root_node.right.data:
        root_node.right = rotate_right(root_node.right)
        rotate_left(root_node)

    return root_node

avl_tree = AVLTree(5)
avl_tree = insert_node(avl_tree, 10)
avl_tree = insert_node(avl_tree, 15)
avl_tree = insert_node(avl_tree, 20)
level_order_traversal(avl_tree)
