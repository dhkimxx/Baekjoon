from collections import deque

N, M = int(input()), int(input())
graph = [[] for _ in range(N + 1)]
visited = [0] * (N + 1)
q = deque()
visited[1] = 1
for _ in range(M):
    a, b = map(int, input().split())
    if a == 1:
        q.append(b)
        visited[b] = 1
    if b == 1:
        q.append(a)
        visited[a] = 1
    graph[a].append(b)
    graph[b].append(a)

while q:
    v = q.popleft()
    for nv in graph[v]:
        if not visited[nv]:
            visited[nv] = 1

print(sum(visited) - 1)
