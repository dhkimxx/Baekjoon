from collections import deque

K = int(input())
W, H = map(int, input().split())
visited = [[[0, 0] for _ in range(W)] for _ in range(H)]
graph = [list(map(int, input().split())) for _ in range(H)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
hdx = [-2, -1, 1, 2, 2, 1, -1, -2]
hdy = [1, 2, 2, 1, -1, -2, -2, -1]


def bfs():
    q = deque([0, 0, 0])
    visited[0][0][0] = 1
    while q:
        x, y,  = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < H and 0 <= ny < W:
                if not graph[nx][ny] and not visited[nx][ny]

print(graph)
