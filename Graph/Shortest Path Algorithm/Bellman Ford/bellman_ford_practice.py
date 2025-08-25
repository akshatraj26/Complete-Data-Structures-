class Graph:
    def __init__(self, vertices):
        self.v = vertices
        self.nodes = []
        self.graph = []

    def add_node(self, value):
        self.nodes.append(value)

    def add_edge(self, source, dest, weight):
        self.graph.append([source, dest, weight])


    def print_solution(self, dist):
        print("Source Distance from Vertex")
        for key, value in dist.items():
            print(f" {key} : {value}")


    def bellmanford(self, source):
        dist = {node: float("inf") for node in self.nodes}

        dist[source] = 0

        for _ in range(self.v - 1):
            for source, dest, weight in self.graph:
                if dist[source] != float('inf') and dist[source] + weight < dist[dest]:
                    dist[dest] = dist[source]  + weight

        for source, dest, weight in self.graph:
            if dist[source] != float('inf') and dist[source] + weight < dist[dest]:
                # dist[dest] = -float("inf")
                print("Graph contains negative cycle")

        self.print_solution(dist)


graph = Graph(5)

graph.add_node('A')
graph.add_node('B')
graph.add_node('C')
graph.add_node('D')
graph.add_node('E')

graph.add_edge('A', 'C', 6)
graph.add_edge('A', 'D', -6)
graph.add_edge('C', 'D', 1)
graph.add_edge('D', 'C', 2)
graph.add_edge('D', 'B', 1)
graph.add_edge('E', 'B', 4)
graph.add_edge('E', 'D', 2)
graph.add_edge('B', 'A', 3)

graph.bellmanford('E')


"""
ertex Distance from Source
 A  :  6
 B  :  3
 C  :  4
 D  :  2
 E  :  0

Process finished with exit code 0

"""