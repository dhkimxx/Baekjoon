#DFS 이용

import sys
N = int(sys.stdin.readline())
graph = []
for n in range(N):
    graph.append(list(map(int, sys.stdin.readline().rstrip())))

def dfs(x, y, cnt):
    if x < 0 or y < 0 or x >= N or y >= N:
        return cnt - 1
    if graph[x][y] == 0:
        return cnt - 1
    if graph[x][y] != 0:
        graph[x][y] = 0
        cnt = dfs(x - 1, y, cnt + 1)
        cnt = dfs(x + 1, y, cnt + 1)
        cnt = dfs(x, y - 1, cnt + 1)
        cnt = dfs(x, y + 1, cnt + 1)
        return cnt

result = []
for i in range(N):
    for j in range(N):
        if graph[i][j] != 0:
            result.append(dfs(i, j, 1))

print(len(result))
for r in sorted(result):
    print(r)
#BFS 이용
'''
import sys
from collections import deque

N = int(sys.stdin.readline())
graph = []
for n in range(N):
    graph.append(list(map(int, sys.stdin.readline().rstrip())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    cnt = 0
    queue = deque([(x, y)])
    graph[x][y] = 0
    while queue:
        x, y = queue.popleft()
        cnt += 1
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= N or ny >= N:
                continue
            if graph[nx][ny] == 1:
                graph[nx][ny] = 0
                queue.append((nx, ny))

    return cnt

result = []
for i in range(N):
    for j in range(N):
        if graph[i][j] != 0:
            result.append(bfs(i, j))

print(len(result))
for r in sorted(result):
    print(r)
'''