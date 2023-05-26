from collections import deque

N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]

dx = [-1, 1, 0, 0, -1, 1, -1, 1]
dy = [0, 0, -1, 1, -1, 1, 1, -1]

checked_index = []

def bfs(sx, sy, checked_index):
    q = deque([(sx, sy)])
    visited[sx][sy] = 1
    checked = [(sx, sy)]
    while q:
        x, y = q.popleft()
        for i in range(8):
            nx, ny = x + dx[i], y + dy[i]
            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue
            if visited[nx][ny]:
                continue
            if graph[x][y] < graph[nx][ny]:
                return 0
            if graph[x][y] == graph[nx][ny]:
                visited[nx][ny] = 1
                q.append((nx, ny))
                checked.append((nx, ny))
    checked_index += checked
    return 1

ans = 0
for i in range(N):
    for j in range(M):
        if (i, j) not in checked_index:
            visited = [[0] * M for _ in range(N)]
            ans += bfs(i, j, checked_index)
print(ans)