from collections import deque

H, W = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(H)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(sx, sy):
    q = deque([(sx, sy)])
    visited[sx][sy] = 1
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < H and 0 <= ny < W:
                if graph[nx][ny]:
                    graph[nx][ny] = 0
                    visited[nx][ny] = 1
                if not visited[nx][ny] and not graph[nx][ny]:
                    q.append((nx, ny))
                    visited[nx][ny] = 1


timer = 0
while sum(map(sum, graph)):
    cnt = sum(map(sum, graph))
    visited = [[0] * W for _ in range(H)]
    bfs(0, 0)
    timer += 1
print(timer)
print(cnt)