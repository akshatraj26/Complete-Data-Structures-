# Prims Algorithm
import sys

class Graph:
    def __init__(self, nu_of_vertex, edges, nodes):
        self.edges = edges
        self.nodes = nodes
        self.v = nu_of_vertex
        self.mst = []


    def print_solution(self):
        print("Edge : Weight")
        for s, d, w in self.mst:
            print("%s -> %s : %s " %(s, d, w))

    # Time Complexity O(V^3)
    # Space Complexity O(V)
    def prims_algo(self):
        visited = [0]*self.v
        edgenum = 0
        visited[0] = True
        while edgenum < self.v - 1:
            min = sys.maxsize
            for i in range(self.v):
                if visited[i]:
                    for j in range(self.v):
                        if not visited[j] and self.edges[i][j]:
                            if min > self.edges[i][j]:
                                min = self.edges[i][j]
                                s, d = i, j
            self.mst.append([self.nodes[s], self.nodes[d], self.edges[s][d]])
            visited[d] = True
            edgenum += 1
        self.print_solution()


edges = [[0, 10, 20, 0, 0],
         [10, 0, 30, 5, 0],
         [20, 30, 0, 15, 6],
         [0, 5, 15, 0, 8],
         [0, 0, 6, 8, 0]]

nodes = ['A', "B", "C", "D", "E"]
g = Graph(5, edges, nodes)
g.prims_algo()


print(sys.maxsize)