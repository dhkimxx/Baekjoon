from collections import deque

R, C = map(int, input().split())
visited_melt = [[0] * C for _ in range(R)]
visited_swan = [[0] * C for _ in range(R)]
graph = []
swan = deque([])
melt = deque([])
for r in range(R):
    graph.append(list(input()))
    for c in range(C):
        if graph[r][c] == 'L':
            swan.append((r, c))
            if len(swan) == 1:
                visited_swan[r][c] = 1
            else:
                visited_swan[r][c] = -1
        if graph[r][c] == '.':
            melt.append((r, c))
            visited_melt[r][c] = 1

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

day = 0

while 1:
    temp = deque()
    while swan:
        x, y = swan.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < R and 0 <= ny < C:
                if visited_swan[x][y] != visited_swan[nx][ny] and \
                        visited_swan[x][y] + visited_swan[nx][ny] == 0\
                        and graph[nx][ny] != 'X':
                    print(day)
                    exit()
                if not visited_swan[nx][ny]:
                    if graph[nx][ny] == '.':
                        visited_swan[nx][ny] = visited_swan[x][y]
                        swan.append((nx, ny))
                    if graph[nx][ny] == 'X':
                        visited_swan[nx][ny] = visited_swan[x][y]
                        temp.append((nx, ny))
    swan = temp.copy()
    temp = deque()
    while melt:
        x, y = melt.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < R and 0 <= ny < C and not visited_melt[nx][ny]:
                if graph[nx][ny] == 'X':
                    temp.append((nx, ny))
                    visited_melt[nx][ny] = 1
                    graph[nx][ny] = '.'
    melt = temp.copy()
    day += 1