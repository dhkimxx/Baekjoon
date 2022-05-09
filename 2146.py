from collections import deque

N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs_numbering(sx, sy, num):
    q = deque([(sx, sy)])
    visited[sx][sy] = True
    graph[sx][sy] = num
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < N and 0 <= ny < N:
                if not visited[nx][ny] and graph[nx][ny]:
                    visited[nx][ny] = True
                    graph[nx][ny] = num
                    q.append((nx, ny))
    return 1


cnt = 1
visited = [[False] * N for _ in range(N)]
for i in range(N):
    for j in range(N):
        if not visited[i][j] and graph[i][j]:
            cnt += bfs_numbering(i, j, cnt)


def bfs_bridge(sx, sy):
    q = deque([(sx, sy)])
    visited[sx][sy] = 1
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < N and 0 <= ny < N:
                if not visited[nx][ny]:
                    if graph[nx][ny] == 0:
                        visited[nx][ny] = visited[x][y] + 1
                        q.append((nx, ny))
                    if graph[nx][ny] and graph[nx][ny] != graph[sx][sy]:
                        return visited[x][y] - 1
    return 1e9


ans = 1e9
for i in range(N):
    for j in range(N):
        visited = [[0] * N for _ in range(N)]
        if graph[i][j]:
            ans = min(ans, bfs_bridge(i, j))
print(ans)
