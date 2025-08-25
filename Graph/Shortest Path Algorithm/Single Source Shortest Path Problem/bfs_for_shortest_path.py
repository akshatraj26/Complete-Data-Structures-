from collections import defaultdict

class Graph:
    def __init__(self, gdict= None):
        if gdict is None:
            gdict = defaultdict(list)
        self.gdict = gdict


    # Time Complexity O(E)
    # Space Complexity O(E)
    def bfs(self, start, end):
        queue = [[start]]
        while queue:
            # print(queue)

            path = queue.pop(0)
            node = path[-1]
            if node == end:
                return path
            for adjacent in self.gdict.get(node, []):
                new_path = list(path)
                new_path.append(adjacent)
                queue.append(new_path)

custom_dict = {
    "a": ['b', 'c'],
    'b': ['d', 'g'],
    'c': ['d', 'e'],
    'd': ['f' ],
    'e': ['f'],
    'g': ['f']

}

graph = Graph(custom_dict)
print(graph.bfs('a', 'e'))

d = list(range(20))

