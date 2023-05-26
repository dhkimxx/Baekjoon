from collections import deque


def bfs(a, b):
    q = deque([(a, b)])
    visited[a][b] = 0
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < N and 0 <= ny < M:
                if graph[nx][ny] == 1 and visited[nx][ny] == -1:
                    visited[nx][ny] = visited[x][y] + 1
                    q.append((nx, ny))

    return True


def answer_print():
    for i in range(N):
        for j in range(M):
            if graph[i][j] > 0:
                if visited[i][j] == -1:
                    print(-1, end=' ')
                else:
                    print(visited[i][j], end=' ')
            else:
                print(0, end=' ')
        print()


N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
visited = [[-1] * M for _ in range(N)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

flag = False
for i in range(N):
    for j in range(M):
        if graph[i][j] == 2:
            flag = bfs(i, j)
            break
    if flag:
        answer_print()
        break
