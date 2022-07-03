from collections import deque

N, M = map(int, input().split())
graph = [[[] for _ in range(N)] for _ in range(N)]
visited = [[0] * N for _ in range(N)]
light_on = [[0] * N for _ in range(N)]
for _ in range(M):
    x, y, a, b = map(int, input().split())
    graph[x - 1][y - 1].append((a - 1, b - 1))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

q = deque([(0, 0)])
visited[0][0] = 1
light_on[0][0] = 1
while q:
    x, y = q.popleft()
    for nx, ny in graph[x][y]:
        if not light_on[nx][ny]:
            light_on[nx][ny] = 1
            visited = [[0] * N for _ in range(N)]
            visited[0][0] = 1
            q = deque([(0, 0)])
            break

    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < N and 0 <= ny < N:
            if light_on[nx][ny] and not visited[nx][ny]:
                visited[nx][ny] = 1
                q.append((nx, ny))

print(sum(map(sum, light_on)))
