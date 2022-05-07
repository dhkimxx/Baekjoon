from collections import deque

dz = [0, 0, 0, 0, -1, 1]
dx = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, -1, 1, 0, 0]


def bfs():
    while q:
        z, x, y = q.popleft()
        for i in range(6):
            nz = z + dz[i]
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nz < L and 0 <= nx < R and 0 <= ny < C:
                if not visited[nz][nx][ny]:
                    if graph[nz][nx][ny] == '.':
                        q.append((nz, nx, ny))
                        visited[nz][nx][ny] = visited[z][x][y] + 1
                    if graph[nz][nx][ny] == 'E':
                        return f"Escaped in {visited[z][x][y]} minute(s)."
    return "Trapped!"


while 1:
    L, R, C = map(int, input().split())
    if L == 0 and R == 0 and C == 0:
        break

    visited = [[[0] * C for _ in range(R)] for _ in range(L)]
    graph = []
    q = deque()
    for l in range(L):
        floor = []
        for r in range(R):
            floor.append(list(input()))
            for c in range(C):
                if floor[r][c] == 'S':
                    q.append((l, r, c))
                    visited[l][r][c] = 1
        graph.append(floor)
        temp = input()

    print(bfs())
