from collections import deque


def bfs(sx, sy):
    q = deque([(sx, sy)])
    visited[sx][sy] = 1
    while q:
        x, y = q.popleft()
        for l in range(8):
            nx, ny = x + dx[l], y + dy[l]
            if 0 <= nx < H and 0 <= ny < W:
                if not visited[nx][ny] and graph[nx][ny]:
                    visited[nx][ny] = 1
                    q.append((nx, ny))
    return 1


dx = [-1, 1, 0, 0, 1, 1, -1, -1]
dy = [0, 0, -1, 1, -1, 1, 1, -1]

while 1:
    W, H = map(int, input().split())
    if not W and not H:
        break
    graph = []
    for h in range(H):
        graph.append(list(map(int, input().split())))
    visited = [[0] * W for _ in range(H)]
    ans = 0
    for i in range(H):
        for j in range(W):
            if not visited[i][j] and graph[i][j]:
                ans += bfs(i, j)
    print(ans)