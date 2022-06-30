from collections import deque

N, M, K = map(int, input().split())
graph = [list(map(int, input())) for _ in range(N)]
visited = [[[1e9] * 11 for _ in range(M)] for _ in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs():
    q = deque([(0, 0, 0)])
    visited[0][0][0] = 1
    while q:
        x, y, cnt = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < N and 0 <= ny < M:
                if not graph[nx][ny]:
                    if visited[nx][ny][cnt] > visited[x][y][cnt] + 1:
                        visited[nx][ny][cnt] = visited[x][y][cnt] + 1
                        q.append((nx, ny, cnt))
                else:
                    if cnt < K:
                        if visited[nx][ny][cnt + 1] > visited[x][y][cnt] + 1:
                            if visited[x][y][cnt] % 2 == 1:
                                visited[nx][ny][cnt + 1] = visited[x][y][cnt] + 1
                                q.append((nx, ny, cnt + 1))
                            else:
                                visited[nx][ny][cnt + 1] = visited[x][y][cnt] + 2
                                q.append((nx, ny, cnt + 1))

    if min(visited[N - 1][M - 1]) == 1e9:
        return -1
    else:
        return min(visited[N - 1][M - 1])

print(bfs())


