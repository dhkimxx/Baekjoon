from collections import deque

N, M = map(int, input().split())
graph = []
for i in range(N):
    graph.append(list(input()))
    for j in range(M):
        if graph[i][j] == 'R':
            R = [i, j]
        if graph[i][j] == 'B':
            B = [i, j]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
visited = [[[[0] * 10 for _ in range(10)]
            for _ in range(10)] for _ in range(10)]


def bfs():
    q = deque([R + B + [0]])
    visited[R[0]][R[1]][B[0]][B[1]] = 1
    ans = -1
    while q:
        rx, ry, bx, by, count = q.popleft()
        print(rx, ry, bx, by, count, q)
        if count > 10:
            break
        if graph[rx][ry] == 'O' and graph[bx][by] != 'O':
            ans = count
            break
        for i in range(4):
            next_rx, next_ry = rx, ry
            next_bx, next_by = bx, by
            while 1:
                if graph[next_rx][next_ry] != '#' and graph[next_rx][next_ry] != 'O':
                    next_rx += dx[i]
                    next_ry += dy[i]
                else:
                    if graph[next_rx][next_ry] == '#':
                        next_rx -= dx[i]
                        next_ry -= dy[i]
                        break
            while 1:
                if graph[next_bx][next_by] != '#' and graph[next_bx][next_by] != 'O':
                    next_bx += dx[i]
                    next_by += dy[i]
                else:
                    if graph[next_bx][next_by] == '#':
                        next_bx -= dx[i]
                        next_by -= dy[i]
                        break
            if next_rx == next_bx and next_ry == next_by:
                if graph[next_rx][next_ry] != 'O':
                    red_dist = abs(next_rx - rx) + abs(next_ry - ry)
                    blue_dist = abs(next_bx - bx) + abs(next_by - by)
                    if red_dist > blue_dist:
                        next_rx -= dx[i]
                        next_ry -= dy[i]
                    else:
                        next_bx -= dx[i]
                        next_by -= dy[i]
            if visited[next_rx][next_ry][next_bx][next_by] == 0:
                visited[next_rx][next_ry][next_bx][next_by] = 1
                q.append([next_rx, next_ry, next_bx, next_by, count + 1])

    return ans


print(bfs())