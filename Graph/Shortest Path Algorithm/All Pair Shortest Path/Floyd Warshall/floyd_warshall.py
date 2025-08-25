# Floyd Warshall Algorithm

inf = float("inf")
def print_solution(nV, distance):
    for i in range(nV):
        for j in range(nV):
            if distance[i][j] == inf:
                print("INF", end=" ")
            else:
                print(distance[i][j], end=" ")
        print(" ")

# Time Complexity O(V^3)
def floyd_warshall(nV, G):
    distance = G
    for k in range(nV):
        for i in range(nV):
            for j in range(nV):
                distance[i][j] = min(distance[i][j], distance[i][k] + distance[k][j])

    print_solution(nV, distance)

graph = [[0, 8, inf, 1],
         [inf, 0, 1, inf],
         [4, inf, 0, inf],
         [inf, 2, 9, 0]]

floyd_warshall(4, graph)