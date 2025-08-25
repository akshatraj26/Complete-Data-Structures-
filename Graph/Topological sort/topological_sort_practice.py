from collections import defaultdict

class Graph:
    def __init__(self, num_of_vertices):
        self.graph = defaultdict(list)
        self.num_of_vertices = num_of_vertices


    def add_edge(self, vertex, edge):
        self.graph[vertex].append(edge)

    def __topological_sort_util(self, v, stack, visited):
        visited.append(v)

        for i in self.graph[v]:
            if i not in visited:
                self.__topological_sort_util(i, stack, visited)

        stack.insert(0, v)

    def topological_sort(self):
        stack = []
        visited = []

        for vertex in list(self.graph):
            if vertex not in visited:
                self.__topological_sort_util(vertex, stack, visited)

        print(stack)


    # Time Complexity O(V+E)
    # Space Complexity O(V+E)
    def bfs(self, vertex):
        visited = [vertex]
        queue = [vertex]

        while queue:
            deq_vertex = queue.pop(0)
            print(deq_vertex, end=" ")
            for adjacent_vertex in self.graph[deq_vertex]:
                if adjacent_vertex not in visited:
                    visited.append(adjacent_vertex)
                    queue.append(adjacent_vertex)


    # Time Complexity O(V+E)
    # Space Complexity O(V+E)
    def dfs(self, vertex):
        visited = [vertex]
        stack = [vertex]

        while stack:
            pop_vertex = stack.pop()
            print(pop_vertex, end=" ")
            for adjacent_vertex in self.graph[pop_vertex]:
                if adjacent_vertex not in visited:
                    visited.append(adjacent_vertex)
                    stack.append(adjacent_vertex)


graph = Graph(8)
graph.add_edge('A', "C")
graph.add_edge('B', "C")
graph.add_edge('B', "D")
graph.add_edge('C', "E")
graph.add_edge('E', "F")
graph.add_edge('F', "G")
graph.add_edge('E', "H")
graph.add_edge('D', "F")

graph.topological_sort()


print("Breadth First Search")
graph.bfs('A')


print("\nDepth First Search")
graph.dfs('A')