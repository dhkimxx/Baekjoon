import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())
graph = []
for n in range(N):
    graph.append(list(map(int, sys.stdin.readline().rstrip())))
visited = [[[0] * 2 for _ in range(M)] for _ in range(N)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs():
    queue = deque([(0, 0, 0)])
    visited[0][0][0] = 1
    while queue:
        x, y, w = queue.popleft()
        if x == N - 1 and y == M - 1:
            return visited[x][y][w]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= N or ny >= M:
                continue
            if visited[nx][ny][w] != 0:
                continue
            if graph[nx][ny] == 1 and w == 0:
                queue.append((nx, ny, 1))
                visited[nx][ny][1] = visited[x][y][0] + 1
            if graph[nx][ny] == 0:
                queue.append((nx, ny, w))
                visited[nx][ny][w] = visited[x][y][w] + 1
    return -1


print(bfs())
