from collections import defaultdict

class Graph:
    def __init__(self):
        self.nodes = set()
        self.edges = defaultdict(list)
        self.distances = {}

    def add_node(self, value):
        self.nodes.add(value)


    def add_edge(self, from_node, to_node, distance):
        self.edges[from_node].append(to_node)
        self.distances[(from_node, to_node)] = distance

def dijkstra(graph):
    result = {}
    for intial in graph.nodes:
        visited = {intial: 0}
        path = defaultdict(list)

        nodes = set(graph.nodes)

        while nodes:
            min_node = None
            for node in nodes:
                if node in visited:
                    if min_node is None:
                        min_node = node
                    elif visited[node] < visited[min_node]:
                        min_node = node

            if min_node is None:
                break

            nodes.remove(min_node)
            current_weight = visited[min_node]

            for edge in graph.edges[min_node]:
                weight = current_weight + graph.distances[(min_node, edge)]
                if edge not in visited or weight < visited[edge]:
                    visited[edge] = weight
                    path[edge].append(min_node)

        result[intial] = (visited, path)
    return result


graph = Graph()

graph.add_node('A')
graph.add_node('B')
graph.add_node('C')
graph.add_node('D')
graph.add_node('E')
graph.add_node('F')
graph.add_node('G')
print(graph.nodes)


graph.add_edge('A', 'B', 2)
graph.add_edge('B', 'E', 3)
graph.add_edge('B', 'D', 1)
graph.add_edge('B', 'E', 4)
graph.add_edge('B', 'C', 6)
graph.add_edge('A', 'C', 5)
graph.add_edge('C', 'F', 8)
graph.add_edge('F', 'G', 7)
graph.add_edge('E', 'G', 9)

# print(graph.edges)
# print(graph.distances)

print(dijkstra(graph))
