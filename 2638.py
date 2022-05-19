from collections import deque

N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(sx, sy):
    q = deque([(sx, sy)])
    visited[sx][sy] = 1
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < N and 0 <= ny < M:
                if graph[nx][ny]:
                    if visited[nx][ny]:
                        graph[nx][ny] = 0
                    else:
                        visited[nx][ny] = 1
                if not visited[nx][ny] and not graph[nx][ny]:
                    q.append((nx, ny))
                    visited[nx][ny] = 1


timer = 1
while 1:
    visited = [[0] * M for _ in range(N)]
    bfs(0, 0)
    if sum(map(sum, graph)) == 0:
        print(timer)
        break
    timer += 1