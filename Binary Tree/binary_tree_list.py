class BinaryTree:
    def __init__(self, size):
        self.customList = size * [None]
        self.last_used_index = 0
        self.max_size = size

    def __str__(self):
        values = [str(x) for x in self.customList if x is not None]
        return " -> ".join(values)

    def insert_node(self, value):
        if self.last_used_index + 1 == self.max_size:
            return "The Binary Tree is full"
        else:
            self.customList[self.last_used_index+1] = value
            self.last_used_index += 1
            return "The Value Inserted Successfully"

    def searching(self, target):
        for index in range(len(self.customList)):
            ti = target.title()
            if self.customList[index] == ti:
                return "Success"
        return "Element not available in the BT"

    # Pre-Order Traversal
    # root node -> left node -> right node
    # Time Complexity O(n)
    # Space Complexity O(n)
    def pre_order_traversal(self, index):
        if index > self.last_used_index:
            return
        print(self.customList[index], end = " | ")
        self.pre_order_traversal(index * 2)
        self.pre_order_traversal(2 * index + 1)

    # In Order Traversal
    # left node -> root node -> right node
    # Time Complexity O(n)
    # Space Complexity O(n)
    def in_order_traversal(self, index):
        if index > self.last_used_index:
            return
        self.in_order_traversal(index * 2)
        print(self.customList[index], end=" | ")
        self.in_order_traversal(index * 2 + 1)

    # post order traversal
    # left node -> right node -> root node
    # Time Complexity O(n)
    # Space Complexity O(n)
    def post_order_traversal(self, index):
        if index > self.last_used_index:
            return
        self.post_order_traversal(index * 2)
        self.post_order_traversal(index * 2 + 1)
        print(self.customList[index], end=" | ")

    # Visit tree level wise
    # Time Complexity O(n)
    # Space Complexity O(1)
    def level_order_traversal(self, index):
        for i in range(index, self.last_used_index + 1):
            print(self.customList[i], end= " | ")

    # Time Complexity O(n)
    # Space Complexity O(n)
    def delete_node(self, value):
        if self.last_used_index == 0:
            return "There is no node to delete"
        for i in range(1, self.last_used_index+1):
            if self.customList[i] == value:
                self.customList[i] = self.customList[self.last_used_index]
                self.customList[self.last_used_index] = None
                self.last_used_index -= 1
                return "Note has been successfully deleted"
        return "This node is not available in Binary Tree"

    # Deleting the Binary Tree
    def deleting_binary_tree(self):
        self.customList = None
        return "The BT has been deleted successfully"

new_binary_tree = BinaryTree(9)
print(new_binary_tree.insert_node("Drinks"))
print(new_binary_tree.insert_node("Hot"))
print(new_binary_tree.insert_node("Cold"))
new_binary_tree.insert_node("Tea")
new_binary_tree.insert_node('Coffee')



print(new_binary_tree)

print(new_binary_tree.searching("cold"))


# Traversal
print("-"*100)
print("Pre Order Traversal")
new_binary_tree.pre_order_traversal(1)

print("\n","-"*100)
print("In Order Traversal")
new_binary_tree.in_order_traversal(1)

print("\n" +"-"*100)
print("Post Order Traversal")
new_binary_tree.post_order_traversal(1)
print("\n", new_binary_tree)

print("\n" +"-"*100)
print("Level Order Traversal")
new_binary_tree.level_order_traversal(1)
# print("\n", new_binary_tree)



print("\n" +"-"*100)
print("Delete Node")
print(new_binary_tree.delete_node("Fan"))
print("\n", new_binary_tree)

print("\n" +"-"*100)
print("Delete Binary Tree")
print(new_binary_tree.deleting_binary_tree())
print("\n", new_binary_tree)