from collections import defaultdict

class Graph:
    def __init__(self, no_of_vertices):
        self.graph = defaultdict(list)
        self.no_of_vertices = no_of_vertices

    def add_edge(self, vertex, edge):
        self.graph[vertex].append(edge)


    def topological_sort_util(self, v, visited, stack):
        visited.append(v)

        for i in self.graph[v]:
            if i not in visited:
                self.topological_sort_util(i, visited, stack)

        stack.insert(0, v)

    # Time Complexity O(V+E)
    # Space Complexity O(V+E)
    def topological_sort(self):
        visited = []
        stack = []

        for k in list(self.graph):
            if k not in visited:
                self.topological_sort_util(k, visited, stack)

        print(stack)


custom_graph = Graph(8)

custom_graph.add_edge("A", "C")
custom_graph.add_edge("B", "C")
custom_graph.add_edge("B", "D")
custom_graph.add_edge("C", "E")
custom_graph.add_edge("D", "F")
custom_graph.add_edge("E", "H")
custom_graph.add_edge("E", "F")
custom_graph.add_edge("F", "G")

print(custom_graph.graph)

custom_graph.topological_sort()

