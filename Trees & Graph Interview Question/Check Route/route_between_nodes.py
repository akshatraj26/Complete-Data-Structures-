# Given a directed graph and two nodes (S and E), design an algorithm to find out whether there is a route from S to E.
from collections import defaultdict
class Graph:
    def __init__(self, gdict = None):
        if gdict is None:
            gdict = defaultdict(list)
        self.gdict = gdict

    def add_edge(self, vertex, edge):
        self.gdict[vertex].append(edge)


    def check_route(self, source, dest):
        visited = [source]
        queue = [source]
        path = False
        while queue:
            de_vertex = queue.pop(0)
            for adjacent_vertex in self.gdict[de_vertex]:
                if adjacent_vertex not in visited:
                    if adjacent_vertex == dest:
                        path = True
                        break
                    else:
                        visited.append(adjacent_vertex)
                        queue.append(adjacent_vertex)
        return path


graph = Graph()

graph.add_edge('E', 'A')
graph.add_edge('E', 'F')
graph.add_edge('F', 'I')
graph.add_edge('A', 'B')
graph.add_edge('A', 'C')
graph.add_edge('A', 'D')
graph.add_edge('B', 'J')
graph.add_edge('C', "G")
graph.add_edge('G', 'H')
graph.add_edge('G', 'D')

print(graph.check_route('S', 'E'))




