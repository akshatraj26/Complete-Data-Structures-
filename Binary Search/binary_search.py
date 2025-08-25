from queue import Queue

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.data)


class BinarySearchTree:
    def __init__(self, root):
        self.root = Node(root)

    # Time Complexity O(logn)
    # Space Complexity O(logn)
    # node of the left will be smaller than parent node
    # node of the right will be larger than parent node
    def insert_node(self, root_node, node_value):
        if root_node.data is None:
            root_node.data = node_value
        else:
            if node_value <= root_node.data:
                if root_node.left is None:
                    root_node.left = Node(node_value)
                else:
                    self.insert_node(root_node.left, node_value)
            else:
                if root_node.right is None:
                    root_node.right = Node(node_value)
                else:
                    self.insert_node(root_node.right, node_value)
        return "Node successfully inserted."


    # Traversal
    # In Order Traversal :   left node -> root node -> right node
    # Time Complexity : O(n)
    # Space Complexity : O(n)
    def in_order_traversal(self, root_node):
        if root_node:
            self.in_order_traversal(root_node.left)
            print(root_node.data, end=" | ")
            self.in_order_traversal(root_node.right)

    # Pre Order Traversal :   root node -> left node -> right node
    # Time Complexity : O(n)
    # Space Complexity : O(n)
    def pre_order_traversal(self, root_node):
        if root_node:
            print(root_node.data, end=" | ")
            self.pre_order_traversal(root_node.left)
            self.pre_order_traversal(root_node.right)

    # Post Order Traversal :   left node -> right node -> root node
    # Time Complexity : O(n)
    # Space Complexity : O(n)
    def post_order_traversal(self, root_node):
        if root_node:
            self.post_order_traversal(root_node.left)
            self.post_order_traversal(root_node.right)
            print(root_node.data, end= " | ")

    # Level Order Traversal
    # Time Complexity O(n)
    # Space Complexity O(n)
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

    # Search node in the Binary Search Tree
    # Time Complexity O(logn)
    # Space Complexity O(logn)
    def search_node(self, root_node, target):
        if root_node:
            if root_node.data == target:
                print("The Value is found")

            elif target <= root_node.data:
                if root_node.left:
                    if root_node.left.data == target:
                        print("The Value is found")

                    else:
                        self.search_node(root_node.left, target)
                else:
                    print("The Value is not found")
            else:
                if root_node.right:
                    if root_node.right.data == target:
                        print("The Value is found")
                    else:
                        self.search_node(root_node.right, target)
                else:
                    print("The Value is not found")


    def min_value_node(self, root_node):
        current = root_node
        while current.left:
            current = current.left
        return current

    def delete_node(self, root_node, node_value):
        if root_node is None:
            return root_node
        if node_value < root_node.data:
            root_node.left = self.delete_node(root_node.left, node_value)
        elif node_value > root_node.data:
            root_node.right = self.delete_node(root_node.right, node_value)
        else:
            # When a node has one child
            if root_node.left is None:
                temp = root_node.right
                root_node = None
                return temp

            if root_node.right is None:
                temp = root_node.left
                root_node = None
                return temp

            # When a node has two children
            min_value = self.min_value_node(root_node.right)
            root_node.data = min_value
            root_node.right = self.delete_node(root_node.right, min_value.data)
        return  root_node


    # Delete entire Binary Search Tree
    def delete_entire_tree(self, root_node) -> str:
        root_node.data = None
        root_node.left = None
        root_node.right = None
        return "The Entire BST is deleted successfully"







bst = BinarySearchTree(None)
bst.insert_node(bst.root, 70)
bst.insert_node(bst.root, 50)
bst.insert_node(bst.root, 90)
bst.insert_node(bst.root, 30)
bst.insert_node(bst.root, 60)
bst.insert_node(bst.root, 80)
bst.insert_node(bst.root, 100)
bst.insert_node(bst.root, 20)
bst.insert_node(bst.root, 40)




print("_"*100, "In Order Traversal", sep='\n')
bst.in_order_traversal(bst.root)

print("\n", "_"*100, "Pre Order Traversal", sep="\n")
bst.pre_order_traversal(bst.root)

print("\n", "_"*100, "Post Order Traversal", sep="\n")
bst.post_order_traversal(bst.root)

print("\n", "_"*100, "Level Order Traversal", sep="\n")
bst.level_order_traversal(bst.root)

print("\n", "_"*100, "Search", sep="\n")
bst.search_node(bst.root, 345)


print(bst.min_value_node(bst.root))

print("\n", "_"*100, "Min Value", sep="\n")
bst.min_value_node(bst.root)


print("\n", "_"*100, "Delete a node", sep="\n")
bst.delete_node(bst.root, 20)
bst.level_order_traversal(bst.root)

print("\n", "_"*100, "Delete entire tree", sep="\n")
print(bst.delete_entire_tree(bst.root))
bst.level_order_traversal(bst.root)