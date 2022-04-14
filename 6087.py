import sys
from collections import deque

W, H = map(int, sys.stdin.readline().split())
visited = [[0] * W for _ in range(H)]
graph = []
C = []
direction = []
for h in range(H):
    direction.append([])
    graph.append(list(sys.stdin.readline().rstrip()))
    for w in range(W):
        direction[h].append(0)
        if graph[h][w] == 'C':
            C.append((w, h))

dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]


def bfs(start):
    queue = deque([start])
    while queue:
        x, y = queue.pop()
        for i in range(0, 4):
            if i == direction[x][y]:
                continue
            nx = x + dx[i - 1]
            ny = y + dy[i - 1]
            if nx < 0 or ny < 0 or nx >= H or ny >= W:
                continue
            if graph[nx][ny] == '*':
                continue




bfs(C[0])

for h in range(H):
    for m in range(len(visited[h])):
        if visited[h][m] == 10000:
            visited[h][m] = '#'
        print(visited[h][m], end=' ')
    print()
print()
for h in range(H):
    for m in range(len(visited[h])):
        print(direction[h][m], end=' ')
    print()
print()
for h in range(H):
    print(*graph[h])
