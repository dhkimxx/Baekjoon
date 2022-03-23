#DFS 이용
import sys

T = int(sys.stdin.readline())
for _ in range(T):

    M, N, K = map(int, sys.stdin.readline().split())
    graph = [[0] * M for _ in range(N)]
    for _ in range(K):
        x, y = map(int, sys.stdin.readline().split())
        graph[y][x] = 1

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    def dfs(y, x):
        if y < 0 or x < 0 or y >= N or x >= M:
            return False
        if graph[y][x] == 1:
            graph[y][x] = 0
            for i in range(4):
                ny = y + dy[i]
                nx = x + dx[i]
                dfs(ny, nx)
            return True
        return False

    result = 0
    for i in range(N):
        for j in range(M):
            if dfs(i, j):
                result += 1
    print(result)

#BFS 이용
'''
import sys
from collections import deque

T = int(sys.stdin.readline())
for _ in range(T):

    M, N, K = map(int, sys.stdin.readline().split())
    graph = [[0] * M for _ in range(N)]
    for _ in range(K):
        x, y = map(int, sys.stdin.readline().split())
        graph[y][x] = 1

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    def bfs(y, x):
        queue = deque()
        queue.append((y, x))
        graph[y][x] = 0

        while queue:
            y, x = queue.popleft()
            for i in range(4):
                ny = y + dy[i]
                nx = x + dx[i]
                if nx < 0 or ny < 0 or nx >= M or ny >= N:
                    continue
                if graph[ny][nx] == 1:
                    queue.append((ny, nx))
                    graph[ny][nx] = 0
        return

    result = 0
    for i in range(N):
        for j in range(M):
            if graph[i][j] == 1:
                bfs(i, j)
                result += 1
    print(result)'''