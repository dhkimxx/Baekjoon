from collections import deque

N, K = map(int, input().split())
if N == K:
    print(0)
    exit()
INF = 500000
visited = [[0] * 2 for _ in range(INF + 1)]
ok = False
turn = 1
q = deque([N])
visited[N][0] = 1
while q:
    K += turn
    if K > INF:
        break
    if visited[K][turn % 2]:
        ok = True
        break
    ThisTurnSize = len(q)
    for j in range(ThisTurnSize):
        dist = q.popleft()
        for nx in [dist + 1, dist - 1, dist * 2]:
            if nx < 0 or nx > INF:
                continue
            if nx == K:
                ok = True
                break
            if visited[nx][turn % 2]:
                continue
            visited[nx][turn % 2] = 1
            q.append(nx)
        if ok:
            break
    if ok:
        break
    turn += 1
if ok:
    print(turn)
else:
    print(-1)
