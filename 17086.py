from collections import deque


N, M = map(int, input().split())
graph = []
babyShark = []
for n in range(N):
    graph.append(list(map(int, input().split())))
    for m in range(M):
        if graph[n][m] == 1:
            babyShark.append((n, m))
d = [(-1, -1), (1, 1), (-1, 1), (1, -1), (0, 1), (0, -1), (-1, 0), (1, 0)]


def bfs():
    queue = deque(babyShark)
    while queue:
        x, y = queue.popleft()
        for i in range(8):
            nx, ny = x + d[i][0], y + d[i][1]
            if nx < 0 or ny < 0 or nx >= N or ny >= M or graph[nx][ny] != 0:
                continue
            queue.append((nx, ny))
            graph[nx][ny] = graph[x][y] + 1


bfs()
print(max(map(max, graph)) - 1)
