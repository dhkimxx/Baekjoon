N, M = map(int, input().split())
graph = [list(input()) for _ in range(N)]
d = {'D': (1, 0), 'U': (-1, 0), 'R': (0, 1), 'L': (0, -1)}


def dfs(x, y):
    global ans
    visited[x][y] = 1
    nx, ny = x + d[graph[x][y]][0], y + d[graph[x][y]][1]
    if visited[nx][ny] == 0:
        dfs(nx, ny)
    if visited[nx][ny] == 1:
        ans += 1
    visited[x][y] = 2


visited = [[0] * M for _ in range(N)]
ans = 0
for i in range(N):
    for j in range(M):
        if not visited[i][j]:
            dfs(i, j)
print(ans)