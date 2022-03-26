import sys
from collections import deque

M, N, H = map(int, sys.stdin.readline().split())
graph = []
queue = deque()

for k in range(H):
    graph.append([])
    for i in range(N):
        graph[k].append(list(map(int, sys.stdin.readline().split())))
        for j in range(M):
            if graph[k][i][j] == 1:
                queue.append((k, i, j))

dz = [0, 0, 0, 0, -1, 1]
dx = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, -1, 1, 0, 0]


def bfs(queue):
    while queue:
        z, x, y = queue.popleft()
        for i in range(6):
            nz = z + dz[i]
            nx = x + dx[i]
            ny = y + dy[i]

            if nz < 0 or nx < 0 or ny < 0:
                continue
            if nz >= H or nx >= N or ny >= M:
                continue
            if graph[nz][nx][ny] == -1:
                continue
            if graph[nz][nx][ny] == 0:
                graph[nz][nx][ny] = graph[z][x][y] + 1
                queue.append((nz, nx, ny))


bfs(queue)

day = 0
for h in range(H):
    for n in range(N):
        for m in range(M):
            day = max(day, graph[h][n][m] - 1)
            if graph[h][n][m] == 0:
                print(-1)
                sys.exit()
print(day)