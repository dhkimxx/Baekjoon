from collections import deque
import copy

N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(sx, sy):
    q = deque([(sx, sy)])
    visited[sx][sy] = True
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < N and 0 <= ny < M:
                if graph[nx][ny] != 0 and not visited[nx][ny]:
                    visited[nx][ny] = True
                    q.append((nx, ny))
    return 1


year = 0
while 1:
    temp_graph = [[0] * M for _ in range(N)]
    for x in range(N):
        for y in range(M):
            if graph[x][y] != 0:
                sea = 0
                for i in range(4):
                    nx, ny = x + dx[i], y + dy[i]
                    if 0 <= nx < N and 0 <= ny < M:
                        if graph[nx][ny] == 0:
                            sea += 1
                temp_graph[x][y] = max(0, graph[x][y] - sea)
    graph = copy.deepcopy(temp_graph)
    year += 1

    if sum(map(sum, graph)) == 0:
        print(0)
        break

    visited = [[False] * M for _ in range(N)]
    cnt = 0
    for x in range(N):
        for y in range(M):
            if graph[x][y] != 0 and not visited[x][y]:
                cnt += bfs(x, y)
    if cnt >= 2:
        print(year)
        break
