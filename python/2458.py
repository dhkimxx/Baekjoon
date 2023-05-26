import sys

INF = int(1e9)

N, M = map(int, sys.stdin.readline().split())
graph = [[INF] * (N + 1) for _ in range(N + 1)]

for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    graph[a][b] = -1
    graph[b][a] = 1

for k in range(1, N + 1):
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            if i == j:
                graph[i][j] = 0
                continue
            if graph[i][k] == 1 and graph[k][j] == 1:
                graph[i][j] = 1
                graph[j][i] = -1
            if graph[i][k] == -1 and graph[k][j] == -1:
                graph[i][j] = -1
                graph[j][i] = 1

result = 0
for i in range(1, N + 1):
    if graph[i][1:].count(INF) == 0:
        result += 1
print(result)