import sys
from collections import deque

N, K = map(int, sys.stdin.readline().split())
visited = [0] * 100001


def bfs(start):
    queue = deque([start])
    visited[start] = 1
    while queue:
        if visited[K]:
            return visited[K] - 1
        x = queue.popleft()
        nx = [x + 1, x - 1, 2 * x]
        for i in range(3):
            if nx[i] == x:
                continue
            if nx[i] < 0 or nx[i] > 100000:
                continue
            if visited[nx[i]] == 0 or visited[nx[i]] > visited[x] + 1:
                visited[nx[i]] = visited[x] + 1
                queue.append(nx[i])


print(bfs(N))