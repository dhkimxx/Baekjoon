from collections import deque

N = int(input())
a, b = map(int, input().split())
graph = [[0] * (N + 1) for _ in range(N + 1)]
M = int(input())
for _ in range(M):
    x, y = map(int, input().split())
    graph[x][y] = 1
    graph[y][x] = 1

visited = [0] * (N + 1)
q = deque([(a, 0)])
ans = -1
while q:
    now, distance = q.popleft()
    if now == b:
        ans = distance
        break
    visited[now] = 1
    for i in range(1, N + 1):
        if not visited[i] and graph[now][i]:
            visited[i] = 1
            q.append((i, distance + 1))

print(ans)