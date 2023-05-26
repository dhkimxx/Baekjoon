import sys
from collections import deque

N = int(sys.stdin.readline())
graph1 = []
graph2 = []
for i in range(N):
    temp = sys.stdin.readline().rstrip()
    graph1.append(temp)
    graph2.append(temp.replace('R', 'G'))
visited1 = [[0] * N for _ in range(N)]
visited2 = [[0] * N for _ in range(N)]
color_count1 = {'R': 0, 'G': 0, 'B': 0}
color_count2 = {'R': 0, 'G': 0, 'B': 0}

dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(x, y, graph, visited):
    start_color = graph[x][y]
    q = deque([(x, y)])
    visited[x][y] = 1
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= N or ny < 0 or ny >= N:
                continue
            if graph[nx][ny] != start_color:
                continue
            if visited[nx][ny]:
                continue
            visited[nx][ny] = 1
            q.append((nx, ny))
    return start_color

for i in range(N):
    for j in range(N):
        if visited1[i][j] == 0:
            color_count1[bfs(i, j, graph1, visited1)] += 1
        if visited2[i][j] == 0:
            color_count2[bfs(i, j, graph2, visited2)] += 1
print(sum(color_count1.values()), sum(color_count2.values()))