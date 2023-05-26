R, S = map(int, input().split())
graph = []
for _ in range(R):
    graph.append(list(input()))

dx = [-1, -1, -1, 1, 1, 1, 0, 0]
dy = [0, 1, -1, 0, 1, -1, -1, 1]


def bfs(x, y):
    visited = [[0] * S for _ in range(R)]
    visited[x][y] = 1
    cnt = 0
    for i in range(8):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < R and 0 <= ny < S:
            if graph[nx][ny] == 'o' and not visited[nx][ny]:
                visited[nx][ny] = 1
                cnt += 1
    return cnt


res1 = 0
res2 = 0
for i in range(R):
    for j in range(S):
        if graph[i][j] == 'o':
            res1 += bfs(i, j)
        else:
            res2 = max(res2, bfs(i, j))

print(res1 // 2 + res2)
