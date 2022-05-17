def dfs(x, y, visited):
    global ans
    ans = max(ans, visited[ord(graph[x][y]) - 65])
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < R and 0 <= ny < C:
            if not visited[ord(graph[nx][ny]) - 65]:
                visited[ord(graph[nx][ny]) - 65] = visited[ord(graph[x][y]) - 65] + 1
                dfs(nx, ny, visited)
                visited[ord(graph[nx][ny]) - 65] = 0
    return

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
R, C = map(int, input().split())
graph = []
visited = [0] * 26
for r in range(R):
    graph.append(list(input().rstrip()))
visited[ord(graph[0][0]) - 65] = 1
ans = 0
dfs(0, 0, visited)
print(ans)