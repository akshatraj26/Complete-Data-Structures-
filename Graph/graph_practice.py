from collections import defaultdict

class Graph:
    def __init__(self, gdict = None):
        if gdict is None:
            gdict = {}
        self.gdict = gdict

    def add_edge(self, vertex, edge):
        self.gdict[vertex].append(edge)

    # Time Complexity O(V+E)
    # Space Complexity O(V+E)
    def bfs(self, vertex):
        visited = [vertex]
        queue  = [vertex]

        while queue:
            que_vertex = queue.pop(0)
            print(que_vertex, end=" ")
            for adjacent_vertex in self.gdict[que_vertex]:
                if adjacent_vertex not in visited:
                    queue.append(adjacent_vertex)
                    visited.append(adjacent_vertex)

    # Time Complexity O(V+E)
    # Space Complexity O(V+E)
    def dfs(self, vertex):
        visited = [vertex]
        stack = [vertex]

        while stack:
            pop_vertex = stack.pop()
            print(pop_vertex, end=" ")
            for adjacency_vertex in self.gdict[pop_vertex]:
                if adjacency_vertex not in visited:
                    visited.append(adjacency_vertex)
                    stack.append(adjacency_vertex)



cust_graph = {"a": ['b', 'c'],
              "b": ["a", "d", 'e'],
              "c": ['a', 'e'],
              'd' : ["b", 'e', 'f'],
              'e': ['d', 'f'],
              'f' : ['d', 'e']}
graph = Graph(cust_graph)
# graph.add_edge('a', 'b')

print(graph.gdict)

print("Breadth First Search")
graph.bfs('a')


print("\nDepth First Search")
graph.dfs('a')