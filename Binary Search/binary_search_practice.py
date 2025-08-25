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

    # def search(self, target):
    #     if self.root:
    #         if self.root.data > target:
    #             if self.root.left:
    #                 self.ro

    def insert_node(self, root_node, node_value):
        if root_node.data is None:
            root_node.data = node_value
        elif node_value <= root_node.data:
            if root_node.left is None:
                root_node.left = Node(node_value)
            else:
                self.insert_node(root_node.left, node_value)
        else:
            if root_node.right is None:
                root_node.right = Node(node_value)
            else:
                self.insert_node(root_node.right, node_value)

        return "Node has been successfully added"

    # Traversal
    # In Order Traversal :   left node -> root node -> right node
    # Time Complexity : O(n)
    # Space Complexity : O(n)
    def in_order_traversal(self, node):
        if node:
            self.in_order_traversal(node.left)
            print(node.data, end=" | ")
            self.in_order_traversal(node.right)

    # Pre Order Traversal :   root node -> left node -> right node
    # Time Complexity : O(n)
    # Space Complexity : O(n)
    def pre_order_traversal(self, node):
        if node:
            print(node.data, end=" | ")
            self.pre_order_traversal(node.left)
            self.pre_order_traversal(node.right)

    # Post Order Traversal :   left node -> right node -> root node
    # Time Complexity : O(n)
    # Space Complexity : O(n)
    def post_order_traversal(self, node):
        if node:
            self.post_order_traversal(node.left)
            self.post_order_traversal(node.right)
            print(node.data, end=" | ")

    # Level Order Traversal
    # Time Complexity O(n)
    # Space Complexity O(n)
    def level_order_traversal(self, node):
        if node:
            queue = Queue()
            queue.enqueue(node)
            while not queue.is_empty():
                root = queue.dequeue()
                print(root.data, end=" | ")
                if root.left:
                    queue.enqueue(root.left)
                if root.right:
                    queue.enqueue(root.right)
        else:
            return "This Binary Search Tree is empty."

    # Search node in the Binary Search Tree
    # Time Complexity O(logn)
    # Space Complexity O(logn)
    def search(self, root_node, node_value):
        if root_node:
            if node_value < root_node.data:
                if root_node.left:
                    if root_node.left.data == node_value:
                        print("The Value is found")
                    else:
                        self.search(root_node.left, node_value)
                else:
                    print("The Value is not found")
            else:
                if root_node.right:
                    if root_node.right.data == node_value:
                        print("The Value is found")
                    else:
                        self.search(root_node.right, node_value)
                else:
                    print("The Value is not found")

    # Minimum value in the Binary Search Tree
    # Time Complexity O(logn)
    def min_value_node(self, root_node):
        current = root_node
        while current.left:
            current = current.left
        return current

    # Delete a node
    def delete_node(self, root_node, node_value):
        if root_node is None:
            return root_node
        if node_value < root_node.data:
            root_node.left = self.delete_node(root_node.left, node_value)
        elif node_value > root_node.data:
            root_node.right = self.delete_node(root_node.right, node_value)

        else:
            # When root node has one child
            if root_node.left is None:
                temp = root_node.right
                root_node = None
                return temp
            if root_node.right is None:
                temp = root_node.left
                root_node = None
                return temp

            # When root node has two children
            min_node = self.min_value_node(root_node.right)
            root_node = min_node
            self.delete_node(root_node.right, min_node.data)

        return root_node

    def delete_entire_bst(self, root_node) -> str:
        root_node.data = None
        root_node.left = None
        root_node.right = None
        return "The BST is deleted successfully"







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
# bst.insert_node(bst.root, 79)



# print(bst.root)
# # print(bst.root.left)
# print(bst.root.right)
# print(bst.root.right.right)
print("_"*100, "In Order Traversal", sep='\n')
bst.in_order_traversal(bst.root)

print("\n", "_"*100, "Pre Order Traversal", sep="\n")
bst.pre_order_traversal(bst.root)

print("\n", "_"*100, "Post Order Traversal", sep="\n")
bst.post_order_traversal(bst.root)

print("\n", "_"*100, "Level Order Traversal", sep="\n")
bst.level_order_traversal(bst.root)


print("\n", "_"*100, "Search", sep="\n")
bst.search(bst.root, 60)

print("\n", "_"*100, "Minimum value node", sep="\n")
print(bst.min_value_node(bst.root).data)
bst.level_order_traversal(bst.root)

print("\n", "_"*100, "Delete  a node", sep="\n")
print(bst.delete_node(bst.root, 20))
bst.level_order_traversal(bst.root)

print("\n", "_"*100, "Delete  a node", sep="\n")
print(bst.delete_node(bst.root, 70))
bst.level_order_traversal(bst.root)


print("\n", "_"*100, "Delete  entire tree", sep="\n")
print(bst.delete_entire_bst(bst.root))
bst.level_order_traversal(bst.root)