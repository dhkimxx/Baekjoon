import sys
from collections import deque

M, N = map(int, sys.stdin.readline().split())
graph = []
queue = deque()
for i in range(N):
    graph.append(list(map(int, sys.stdin.readline().split())))
    for j in range(M):
        if graph[i][j] == 1:
            queue.append((i, j))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(queue):
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= N or ny >= M:
                continue
            if graph[nx][ny] == -1:
                continue
            if graph[nx][ny] == 0:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))


bfs(queue)

day = 0
for n in range(N):
    for m in range(M):
        day = max(day, graph[n][m] - 1)
        if graph[n][m] == 0:
            print(-1)
            sys.exit()
print(day)