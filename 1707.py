import sys

def dfs(v, graph, visited):
    visited[v] = 1


K = int(sys.stdin.readline())
for k in range(K):
    V, E = map(int, sys.stdin.readline().split())
    graph = [[] for _ in range(V + 1)]
    visited = [0] * (V + 1)
    for e in range(E):
        u, v = map(int, sys.stdin.readline().split())
        graph[u].append(v)
        graph[v].append(u)

    for i in range(1, V + 1):
        if visited[i] == '0':
            dfs(i)

