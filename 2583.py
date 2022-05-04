from collections import deque

M, N, K = map(int, input().split())
graph = [[1] * (M) for _ in range(N)]
visited = [[False] * (M) for _ in range(N)]
rectangle = [tuple(map(int, input().split())) for _ in range(K)]
for r in rectangle:
    x1, y1, x2, y2 = r
    for i in range(x1, x2):
        for j in range(y1, y2):
            graph[i][j] = 0

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(sx, sy):
    q = deque([(sx, sy)])
    visited[sx][sy] = True
    area = 1
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny]:
                if graph[nx][ny] == 1:
                    q.append((nx, ny))
                    visited[nx][ny] = True
                    area += 1
    return area

ans = []
for i in range(0, N):
    for j in range(0, M):
        if not visited[i][j] and graph[i][j] == 1:
            ans.append(bfs(i, j))
print(len(ans))
print(' '.join(map(str, sorted(ans))))