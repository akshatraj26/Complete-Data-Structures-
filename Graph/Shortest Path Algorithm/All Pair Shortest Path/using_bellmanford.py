class Graph:
    def __init__(self, vertices):
        self.v = vertices
        self.graph = []
        self.nodes = []


    def add_node(self, value):
        self.nodes.append(value)

    def add_edge(self, s, d, w):
        self.graph.append([s, d, w])



    def bellman_ford(self):
        res = {}

        for src in self.nodes:
            dist = {key: float('inf') for key in self.nodes}

            dist[src] = 0

            for _ in range(self.v - 1):
                for s, d, w in self.graph:
                    if dist[s] != float('inf') and dist[s] + w < dist[d]:
                        dist[d] = dist[s] + w
            for s, d, w in self.graph:
                if dist[s] != float('inf') and dist[s] + w < dist[d]:
                    return "Graph contains negative cycle"

            res[src] = dist
        return  res

def print_solution(dist):
    for key, value in dist.items():
        print(f" {key} : {value}")

graph = Graph(5)

graph.add_node('A')
graph.add_node('B')
graph.add_node('C')
graph.add_node('D')
graph.add_node('E')

graph.add_edge('A', 'C', 6)
graph.add_edge('A', 'D', 6)
graph.add_edge('C', 'D', 1)
graph.add_edge('D', 'C', 2)
graph.add_edge('D', 'B', 1)
graph.add_edge('E', 'B', 4)
graph.add_edge('E', 'D', 2)
graph.add_edge('B', 'A', 3)


print_solution(graph.bellman_ford())