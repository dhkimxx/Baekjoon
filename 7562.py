import sys
from collections import deque

dx = [-2, -1, 1, 2,  2,  1, -1, -2]
dy = [1,   2, 2, 1, -1, -2, -2, -1]


T = int(sys.stdin.readline())
for t in range(T):
    I = int(sys.stdin.readline())
    x, y = map(int, sys.stdin.readline().split())
    targetX, targetY = map(int, sys.stdin.readline().split())

    graph = [[0] * I for _ in range(I)]
    visited = [[False] * I for _ in range(I)]

    queue = deque([(x, y)])
    visited[x][y] = True

    while queue:
        if visited[targetX][targetY]:
            print(graph[targetX][targetY])
            break
        x, y = queue.popleft()
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= I or ny >= I:
                continue
            if visited[nx][ny]:
                continue
            if not visited[nx][ny]:
                visited[nx][ny] = True
                queue.append((nx, ny))
                graph[nx][ny] = graph[x][y] + 1
