import sys

INF = int(1e9)

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
graph = [[INF] * (N + 1) for _ in range(N + 1)]
for m in range(M):
    A, B, cost = map(int, sys.stdin.readline().split())
    graph[A][B] = min(cost, graph[A][B])


for k in range(1, N + 1):
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            if i != j:
                graph[i][j] = min(graph[i][k] + graph[k][j], graph[i][j])

for i in range(1, N + 1):
    for j in range(1, N + 1):
        if graph[i][j] == INF:
            print(0, end=' ')
        else:
            print(graph[i][j], end=' ')
    print()