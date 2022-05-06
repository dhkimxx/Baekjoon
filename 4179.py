from collections import deque

R, C = map(int, input().split())
visited_J = [[0] * C for _ in range(R)]
visited_F = [[0] * C for _ in range(R)]
graph = []
queue_J = deque()
queue_F = deque()

for r in range(R):
    graph.append(list(input()))
    for c in range(C):
        if graph[r][c] == 'J':
            graph[r][c] = '.'
            queue_J.append((r, c))
            visited_J[r][c] = 1
            if r == 0 or r == R - 1 or c == 0 or c == C - 1:
                print(1)
                exit()
        if graph[r][c] == 'F':
            queue_F.append((r, c))
            visited_F[r][c] = 1

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs():
    while queue_F:
        x, y = queue_F.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < R and 0 <= ny < C:
                if not visited_F[nx][ny] and graph[nx][ny] == '.':
                    visited_F[nx][ny] = visited_F[x][y] + 1
                    queue_F.append((nx, ny))

    while queue_J:
        x, y = queue_J.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < R and 0 <= ny < C:
                if not visited_J[nx][ny] and graph[nx][ny] == '.':
                    if visited_F[nx][ny] == 0 or visited_J[x][y] + 1 < visited_F[nx][ny]:
                        visited_J[nx][ny] = visited_J[x][y] + 1
                        queue_J.append((nx, ny))
                        if nx == 0 or ny == 0 or nx == R - 1 or ny == C - 1:
                            return visited_J[nx][ny]
    return 'IMPOSSIBLE'

print(bfs())