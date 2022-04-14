import sys
from collections import deque

W, H = map(int, sys.stdin.readline().split())
c = [[[0] * 4 for _ in range(W)] for _ in range(H)]
graph = []
R = []
for h in range(H):
    graph.append(list(sys.stdin.readline().rstrip()))
    for w in range(W):
        if graph[h][w] == 'C':
            R.extend([h, w])
x1, y1, x2, y2 = R
dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]
queue = deque([])


def turn(x, y, dir):
    ndir = [(dir + 1) % 4, (dir + 3) % 4]
    for k in ndir:
        if not c[x][y][k] or c[x][y][k] > c[x][y][dir] + 1:
            c[x][y][k] = c[x][y][dir] + 1
            queue.append([x, y, k])


def bfs(x, y):
    queue.extend([[x, y, 0], [x, y, 1], [x, y, 2], [x, y, 3]])
    c[x][y] = [1, 1, 1, 1]
    ans = []
    while queue:
        x, y, dir = queue.popleft()
        nx = x + dx[dir]
        ny = y + dy[dir]
        if 0 <= nx < H and 0 <= ny < W:
            if not c[nx][ny][dir] or c[nx][ny][dir] > c[x][y][dir]:
                if graph[nx][ny] == '.':
                    c[nx][ny][dir] = c[x][y][dir]
                    queue.appendleft([nx, ny, dir])
                    turn(nx, ny, dir)
                if nx == x2 and ny == y2:
                    c[nx][ny][dir] = c[x][y][dir]
                    ans.append(c[nx][ny][dir])
    print(min(ans) - 1)


bfs(x1, y1)
