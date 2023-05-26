from collections import deque


def dfs(x, y):
    visited[x][y] = 1
    q = deque([(x, y)])
    while q:
        x, y = q.popleft()
        for i in range(8):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < M and 0 <= ny < N:
                if not visited[nx][ny] and graph[nx][ny]:
                    q.append((nx, ny))
                    visited[nx][ny] = 1
    return 1


M, N = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(M)]
dx = [-1, -1, -1, 1, 1, 1, 0, 0]
dy = [1, -1, 0, 1, -1, 0, 1, -1]
visited = [[0] * N for _ in range(M)]
ans = 0
for i in range(M):
    for j in range(N):
        if not visited[i][j] and graph[i][j]:
            ans += dfs(i, j)
print(ans)