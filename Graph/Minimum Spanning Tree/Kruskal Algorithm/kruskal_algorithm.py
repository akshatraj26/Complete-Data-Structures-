from disjointset import DisJointSet

vertices = ['A', "B", "C", "D", "E", "F"]

class Graph:
    def __init__(self, vertices):
        self.v = vertices
        self.graph = []
        self.nodes = []
        self.mst = []

    def add_node(self, value):
        self.nodes.append(value)

    def add_edge(self, source, dest, weight):
        self.graph.append([source, dest, weight])

    def print_solution(self):
        for source, dest, weight in self.mst:
            print("%s - %s : %s " % (source, dest, weight))


    def kruskal(self):
        i, e = 0, 0
        ds = DisJointSet(self.nodes)
        self.graph = sorted(self.graph, key=lambda item: item[2])
        while e < self.v - 1:
            s, d, w = self.graph[i]
            i += 1
            x = ds.find(s)
            y = ds.find(d)

            if x != y:
                e += 1
                self.mst.append([s, d, w])
                ds.union(x, y)
        self.print_solution()


graph = Graph(5)

# Add all nodes
graph.add_node("A")
graph.add_node("B")
graph.add_node("C")
graph.add_node("D")
graph.add_node("E")

# Add edges
graph.add_edge('A', "B", 5)
graph.add_edge('A', "C", 13)
graph.add_edge('B', "D", 8)
graph.add_edge('E', "A", 15)
graph.add_edge('B', "C", 10)
graph.add_edge('D', "C", 6)
graph.add_edge('C', "E", 20)


graph.kruskal()



