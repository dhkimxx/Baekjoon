import sys

input = sys.stdin.readline
V, E = map(int, input().split())
INF = int(1e9)
graph = [[INF] * (V + 1) for _ in range(V + 1)]

for _ in range(E):
    a, b, c = map(int, input().split())
    graph[a][b] = c


def fw():
    result = INF
    for k in range(1, V + 1):
        for i in range(1, V + 1):
            for j in range(1, V + 1):
                if graph[i][j] > graph[i][k] + graph[k][j]:
                    graph[i][j] = graph[i][k] + graph[k][j]
                if graph[i][j] != INF and graph[j][i] != INF:
                    result = min(result, graph[i][j] + graph[j][i])

    if result == INF:
        return -1
    else:
        return result


print(fw())