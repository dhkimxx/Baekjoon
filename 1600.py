from collections import deque

K = int(input())
W, H = map(int, input().split())
visited = [[[1e9] * 31 for _ in range(W)] for _ in range(H)]
graph = [list(map(int, input().split())) for _ in range(H)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
hdx = [-2, -1, 1, 2, 2, 1, -1, -2]
hdy = [1, 2, 2, 1, -1, -2, -2, -1]


def bfs():
    q = deque([(0, 0, 0)])
    visited[0][0][0] = 0
    while q:
        x, y, cnt = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < H and 0 <= ny < W:
                if not graph[nx][ny] and visited[nx][ny][cnt] == 1e9:
                    visited[nx][ny][cnt] = visited[x][y][cnt] + 1
                    q.append((nx, ny, cnt))
        if cnt < K:
            for i in range(8):
                nx, ny = x + hdx[i], y + hdy[i]
                if 0 <= nx < H and 0 <= ny < W:
                    if not graph[nx][ny] and visited[nx][ny][cnt + 1] == 1e9:
                        visited[nx][ny][cnt + 1] = visited[x][y][cnt] + 1
                        q.append((nx, ny, cnt + 1))

    if min(visited[H - 1][W - 1]) == 1e9:
        return -1
    else:
        return min(visited[H - 1][W - 1])


print(bfs())
