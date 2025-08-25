from collections import defaultdict

class Graph:
    def __init__(self, graph = None):
        if graph is None:
            graph = defaultdict(list)
        self.graph = graph
        self.nodes = []

    def add_edge(self, source, dest):
        self.graph[source].append(dest)

    def add_node(self, value):
        self.nodes.append(value)

    def bfs(self, start, end):
        queue = [[start]]

        while queue:
            path = queue.pop(0)

            node = path[-1]
            if node == end:
                return path
            for adjacent in self.graph.get(node, []):
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
print(graph.bfs('a', 'd'))