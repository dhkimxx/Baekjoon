from collections import deque

N = int(input())
graph = [[] for _ in range(N + 1)]
parent = [0] * (N + 1)
for _ in range(N - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)


def bfs(start):
    q = deque([start])
    parent[start] = 1
    while q:
        v = q.pop()
        for nv in graph[v]:
            if parent[nv]:
                continue
            parent[nv] = v
            q.append(nv)


bfs(1)
print('\n'.join(map(str, parent[2:])))