from collections import deque
import sys

input = sys.stdin.readline
N, M, P = map(int, input().split())
S = [0] + list(map(int, input().split()))
visited = [[0] * M for _ in range(N)]
result = [0] * (P + 1)
Q = [deque([]) for _ in range(10)]

for n in range(N):
    temp = list(input())
    for m in range(M):
        if temp[m] == '#':
            visited[n][m] = 1
        elif temp[m] != '.':
            visited[n][m] = 1
            result[int(temp[m])] += 1
            Q[int(temp[m])].append((n, m))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

while 1:
    flag = 1
    for p in range(1, P + 1):
        for _ in range(min(S[p], max(N, M))):
            for _ in range(len(Q[p])):
                x, y = Q[p].popleft()
                for i in range(4):
                    nx, ny = x + dx[i], y + dy[i]
                    if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny]:
                        visited[nx][ny] = 1
                        result[p] += 1
                        Q[p].append((nx, ny))
                        flag = 0
    if flag:
        break
print(' '.join(map(str, result[1:])))
