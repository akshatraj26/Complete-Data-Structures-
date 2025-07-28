class BinaryNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def __str__(self):
        return self.value

    def pre_order_traversal(self):
        print(self.value, end= " ")

        if self.left:
            self.left.pre_order_traversal()

        if self.right:
            self.right.pre_order_traversal()

binarytree = BinaryNode('Drinks')
binarytree.left = BinaryNode('Hot')
binarytree.right = BinaryNode('Cold')
binarytree.left.left = BinaryNode("Tea")
binarytree.left.right = BinaryNode("Coffee")
binarytree.right.left = BinaryNode("Alcoholic")
binarytree.left.left = BinaryNode("Non Alcoholic")

print(binarytree)
binarytree.pre_order_traversal()
