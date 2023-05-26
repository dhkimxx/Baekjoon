import copy
from collections import deque

N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
safe_zone = 0
index = []
virus = []
for i in range(N):
    for j in range(M):
        if graph[i][j] == 0:
            index.append((i, j))
            safe_zone += 1
        if graph[i][j] == 2:
            virus.append((i, j))
len_index = len(index)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y, graph):
    q = deque([(x, y)])
    polluted_zone = 0
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue
            if graph[nx][ny] == 0:
                graph[nx][ny] = 2
                q.append((nx, ny))
                polluted_zone += 1
    return polluted_zone

ans = 0
for i in range(0, len_index):
    for j in range(i + 1, len_index):
        for k in range(j + 1, len_index):
            total_polluted_zone = 0
            temp_graph = copy.deepcopy(graph)
            x1, y1 = index[i]
            x2, y2 = index[j]
            x3, y3 = index[k]
            temp_graph[x1][y1] = 1
            temp_graph[x2][y2] = 1
            temp_graph[x3][y3] = 1
            for v in virus:
                X, Y = v
                total_polluted_zone += bfs(X, Y, temp_graph)
            ans = max(ans, safe_zone - 3 - total_polluted_zone)
print(ans)