import sys
from collections import deque
N, M, R = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(N + 1)]
visited = [0] * (N + 1)
for _ in range(M):
    A, B = map(int, sys.stdin.readline().split())
    graph[A].append(B)
    graph[B].append(A)

def bfs(start):
    count = 1
    q = deque([start])
    visited[start] = count
    count += 1
    while q:
        v = q.popleft()
        for nv in sorted(graph[v], reverse=True):
            if visited[nv]:
                continue
            q.append(nv)
            visited[nv] = count
            count += 1

bfs(R)
print('\n'.join(map(str, visited[1:])))