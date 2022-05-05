from collections import deque

N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]
for i in range(N - 1):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

def bfs(start, target):
    q = deque([start])
    visited[start] = 1
    while q:
        v = q.popleft()
        if v == target:
            return visited[v] - 1
        for i in graph[v]:
            nv = i[0]
            if not visited[nv]:
                visited[nv] = visited[v] + i[1]
                q.append(nv)

for t in range(M):
    visited = [0] * (N + 1)
    start, end = map(int, input().split())
    print(bfs(start, end))