import sys

N = int(sys.stdin.readline())
graph = []
for _ in range(N):
    graph.append(list(map(int, sys.stdin.readline().split())))


def dfs(v):
    for i in range(N):
        if graph[v][i] == 1 and visited[i] == 0:
            visited[i] = 1
            dfs(i)
    return


for i in range(N):
    visited = [0] * N
    dfs(i)
    print(*visited)
'''
N = int(input())
graph = []
for _ in range(N):
    graph.append(list(map(int, input().split())))

for k in range(N):
    for i in range(N):
        for j in range(N):
            if graph[i][k] == 1 and graph[k][j] == 1:
                graph[i][j] = 1

for row in graph:
    for col in row:
        print(col, end=" ")
    print()
'''