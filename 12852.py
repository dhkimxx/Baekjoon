from collections import deque

N = int(input())
visited = [0] * (N + 1)
q = deque([(N, 0, [N])])
visited[N] = 1
while q:
    now, cnt, ans = q.popleft()
    if now == 1:
        print(cnt)
        print(*ans)
        break
    if now % 3 == 0:
        next = now // 3
        if not visited[next]:
            visited[next] = 1
            q.append((next, cnt + 1, ans + [next]))
    if now % 2 == 0:
        next = now // 2
        if not visited[next]:
            visited[next] = 1
            q.append((next, cnt + 1, ans + [next]))
    next = now - 1
    if not visited[next]:
        visited[next] = 1
        q.append((next, cnt + 1, ans + [next]))
