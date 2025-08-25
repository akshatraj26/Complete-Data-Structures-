from sqlalchemy.sql.functions import current_user


class TrieNode:
    def __init__(self):
        self.children =  {}
        self.end_of_string = False

    def __str__(self):
        values = [i for i in self.children]
        return " -> ".join(values)

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


    # Time Complexity O(m)
    # Space Complexity O(1)
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
            self.delete_string(current_node, word, index+1)
            return False

        can_this_node_deleted = self.delete_string(current_node, word, index + 1)
        if can_this_node_deleted is True:
            root.children.pop(ch)
            return True
        else:
            return False






new_trie = Trie()
new_trie.insert_string("App")
new_trie.insert_string('Apps')


new_trie.delete_string(new_trie.root, "App", 0)
print(new_trie.search_string('App'))