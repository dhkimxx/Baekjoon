from collections import deque

N, K = map(int, input().split())
visited = [[1e9, 1e9] for _ in range(500001)]
q = deque([(N, 0)])
visited[N][0] = 0
while q:
    v, t = q.popleft()
    for nv in [v + 1, v - 1, 2 * v]:
        if 0 <= nv <= 500000 and visited[nv][(t + 1) % 2] == 1e9:
            visited[nv][(t + 1) % 2] = visited[v][t % 2] + 1
            q.append((nv, t + 1))

time = 0
while K <= 500000:
    if visited[K][time % 2] != 1e9:
        if visited[K][time % 2] <= time:
            print(time)
            exit()
    time += 1
    K += time
print(-1)