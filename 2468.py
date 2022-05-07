from collections import deque

N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]
max_level = max(map(max, graph))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(sx, sy):
    q = deque([(sx, sy)])
    visited[sx][sy] = 1
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
                if graph[nx][ny] > level:
                    visited[nx][ny] = 1
                    q.append((nx, ny))
    return 1

ans = 0
for level in range(0, max_level):
    visited = [[0] * N for _ in range(N)]
    cnt = 0
    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                if graph[i][j] > level:
                    cnt += bfs(i, j)
    ans = max(ans, cnt)
print(ans)