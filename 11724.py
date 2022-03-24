import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(N + 1)]
visited = [False] * (N + 1)
for m in range(M):
    A, B = map(int, sys.stdin.readline().split())
    graph[A].append(B)
    graph[B].append(A)


def dfs(v):
    visited[v] = True
    for i in graph[v]:
        if not visited[i]:
            dfs(i)
    return


def bfs(start):
    queue = deque([start])
    visited[start] = True
    while queue:
        v = queue.popleft()
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
    return


countComponent = 0
for n in range(1, N + 1):
    if not visited[n]:
        dfs(n)
        #bfs(n)
        countComponent += 1
print(countComponent)
