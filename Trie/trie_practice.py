class TrieNode:
    def __init__(self):
        self.children = {}
        self.end_of_string = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    # Time Complexity O(m)
    # Space Complexity O(m)
    def insert_string(self, word):
        current = self.root
        for i in word:
            ch = i
            node = current.children.get(ch)
            if node is None:
                node = TrieNode()
                current.children.update({ch: node})
            current = node
        current.end_of_string = True
        print("Successfully inserted")

    def search_string(self, word):
        current_node = self.root
        for i in word:
            node = current_node.children.get(i)
            if node is None:
                return False
            current_node = node

        if current_node.end_of_string is True:
            return True
        else:
            return False

    def delete_string(self, root, word, index):
        ch = word[index]
        current_node = root.children.get(ch)
        can_this_node_deleted = False
        if len(current_node.children) > 1:
            self.delete_string(current_node, word, index + 1)
            return False

        if index == len(word) - 1:
            if len(current_node.children) > 1:
                current_node.end_of_string = False
                return False
            else:
                root.children.pop(ch)
                return True

        if current_node.end_of_string is True:
            self.delete_string(current_node, word, index + 1)
            return False

        can_this_node_deleted = self.delete_string(current_node, word, index + 1)
        if can_this_node_deleted:
            root.children.pop(ch)
            return True
        else:
            return False



trie = Trie()
trie.insert_string("Akshat")
trie.insert_string("Abhinay")

trie.insert_string("Abhishek")

print(trie.search_string("Abhinay"))

trie.delete_string(trie.root, "Abhishek", 0 )

print(trie.search_string("Abhishek"))


