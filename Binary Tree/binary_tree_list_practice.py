class BinaryTree:
    def __init__(self, size):
        self.custom_list = [None] * size
        self.last_used_index = 0
        self.max_size = size

    def __str__(self):
        values = [str(x) for x in self.custom_list if x is not None]
        return " -> ".join(values)

    def insert_node(self, value):
        if self.max_size == self.last_used_index + 1:
            return "The Binary Tree is full."
        else:
            self.custom_list[self.last_used_index + 1] = value
            self.last_used_index += 1
            return "Node inserted successfully."

    # Searching a node in the Binary Tree
    # Time Complexity O(n)
    def search(self, target):
        for i in range(1, self.last_used_index):
            if self.custom_list[i] == target:
                return "Success"
        return "Node found in the Binary Tree"

    # Traversing of the Binary Tree
    # In Order Traversal  left node -> root node -> right node
    # Time Complexity O(n)
    # Time Complexity O(n)
    def in_order_traversal(self, index):
        if index > self.last_used_index:
            return
        self.in_order_traversal(index * 2)
        print(self.custom_list[index], end=" | ")
        self.in_order_traversal(index * 2 + 1)

    # Pre Order Traversal  root node -> left node -> right node
    # Time Complexity O(n)
    # Time Complexity O(n)
    def pre_order_traversal(self, index):
        if index > self.last_used_index:
            return
        print(self.custom_list[index], end = ' | ')
        self.pre_order_traversal(index * 2)
        self.pre_order_traversal(index * 2 + 1)

    # Post Order Traversal  left node -> right node -> root node
    # Time Complexity O(n)
    # Space Complexity O(n)
    def post_order_traversal(self, index):
        if index > self.last_used_index:
            return
        self.post_order_traversal(index * 2)
        self.post_order_traversal(index * 2 + 1)
        print(self.custom_list[index], end=" | ")

    # Level Order Traversal
    # Time Complexity O(n)
    def level_order_traversal(self):
        for i in range(1, self.last_used_index + 1):
            print(self.custom_list[i], end = ' | ')

    # delete a node
    # We will use level order traversal for this
    # Time Complexity O(n)
    # Space Complexity O(1)
    def delete_node(self, target):
        for i in range(1, self.last_used_index + 1):
            if self.custom_list[i] == target:
                self.custom_list[i] = self.custom_list[self.last_used_index]
                self.custom_list[self.last_used_index] = None
                self.last_used_index -= 1
                return "Node deleted successfully"
        return "This node is not available in this BT"

    def delete_tree(self):
        self.custom_list = None
        self.last_used_index = 0
        return "The Binary Tree has been deleted Successfully"





tree = BinaryTree(8)
tree.insert_node("Drinks")
print(tree)

print("-"*100)
tree.insert_node("Hot")
tree.insert_node("Cold")
tree.insert_node("Tea")
tree.insert_node('Coffee')
tree.insert_node("Alcoholic")
print(tree)

print(tree.insert_node("Non-Alcoholic"))

print(tree)

print(tree.search(target="Coffee"))

print("-"*100)
print("In Order Traversal")
tree.in_order_traversal(1)

print("\n" + "-"*100)
print("In Order Traversal")
tree.pre_order_traversal(1)
print("\n")
print(tree)

print("\n" + "-"*100)
print("Post Order Traversal")
tree.post_order_traversal(1)
print("\n")
print(tree)

print("\n" + "-"*100)
print("Level Order Traversal")
tree.level_order_traversal()
print("\n")
print(tree)

print("\n" + "-"*100)
print("Delete a Node")
print(tree.delete_node('Coffee1'))
print("\n")
print(tree)


print("\n" + "-"*100)
print("Delete entire tree")
print(tree.delete_tree())
print("\n")
print(tree)
