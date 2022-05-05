from collections import deque

N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
visited = [[False] * M for _ in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(sx, sy):
    cnt = 1
    q = deque([(sx, sy)])
    visited[sx][sy] = True
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < N and 0 <= ny < M:
                if not visited[nx][ny] and graph[nx][ny]:
                    visited[nx][ny] = True
                    q.append((nx, ny))
                    cnt += 1
    return cnt


ans = []
for i in range(N):
    for j in range(M):
        if not visited[i][j] and graph[i][j]:
            ans.append(bfs(i, j))
print(len(ans))
if len(ans) == 0:
    print(0)
else:
    print(max(ans))