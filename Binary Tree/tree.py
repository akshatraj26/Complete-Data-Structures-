class TreeNode:
    def __init__(self, value, children = []):
        self.value = value
        self.children = children

    def __str__(self, level = 0):
        ret = " " * level + str(self.value)  + "\n"
        for child in self.children:
            ret += child.__str__(level + 1)
        return ret

    def add_child(self, TreeNode):
        self.children.append(TreeNode)


############################################################################

tree = TreeNode('Drinks', [])


############################################################################
wine = TreeNode("Wine", [])
beer = TreeNode("Beer", [])
alcoholic = TreeNode("Alcoholic", [])
alcoholic.add_child(wine)
alcoholic.add_child(beer)
############################################################################
cola = TreeNode("Cola", [])
fanta = TreeNode("Fanta", [])
soda = TreeNode("Soda", [])
non_alcoholic = TreeNode("Non-Alcoholic", [])
non_alcoholic.add_child(cola)
non_alcoholic.add_child(fanta)
non_alcoholic.add_child(soda)
############################################################################
black = TreeNode("Black", [])
green = TreeNode("Green", [])
tea = TreeNode("Tea", [])
tea.add_child(black)
tea.add_child(green)
############################################################################
cappuccino = TreeNode("Cappuccino", [])
latte = TreeNode("Latte", [])
americano = TreeNode("Americano", [])
coffee = TreeNode("Coffee", [americano, latte, cappuccino])

############################################################################
hot = TreeNode("Hot", [])
hot.add_child(tea)
hot.add_child(coffee)

cold = TreeNode('Cold', [])
cold.add_child(alcoholic)
cold.add_child(non_alcoholic)

tree.add_child(cold)
tree.add_child(hot)



print(tree)