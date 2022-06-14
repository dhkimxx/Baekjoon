from collections import deque
N, K = map(int, input().split())
visited = [0] * 100001
parent = [0] * 100001
q = deque([N])
visited[N] = 1
while q:
    v = q.popleft()
    if v == K:
        print(visited[v] - 1)
        now = K
        route = [K]
        while now != N:
            route.append(parent[now])
            now = parent[now]
        print(*reversed(route))
        break
    for nv in [v - 1, v + 1, 2 * v]:
        if 0 <= nv <= 100000 and not visited[nv]:
            visited[nv] = visited[v] + 1
            parent[nv] = v
            q.append(nv)