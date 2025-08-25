
inf = float('inf')


def print_solution(no_vertices, graph):
    for i in range(no_vertices):
        for j in range(no_vertices):
            if graph[i][j] == inf:
                print("Inf", end=" ")
            else:
                print(graph[i][j], end=" ")
        print(" ")


# Time Complexity O(V^3)
# Space Complexity O(V^2)
def floyd_warshall(nV, graph):
    distance = graph

    for k in range(nV):
        for i in range(nV):
            for j in range(nV):
                if distance[i][j] > distance[i][k] + distance[k][j]:
                    distance[i][j] = distance[i][k] + distance[k][j]
    print_solution(nV, distance)




graph = [[0, 8, inf, 1],
         [inf, 0, 1, inf],
         [4, inf, 0, inf],
         [inf, 2, 9, 0]]

floyd_warshall(4, graph)