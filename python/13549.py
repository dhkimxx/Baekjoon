from collections import deque

N, K = map(int, input().split())
INF = int(1e9)
cost = [INF] * 100001


def bfs(start, end):
    q = deque([start])
    cost[start] = 1
    while q:
        v = q.popleft()
        for nv in [v - 1, v + 1, v * 2]:
            if 0 <= nv <= 100000:
                if nv != v * 2 and cost[nv] > cost[v] + 1:
                    cost[nv] = cost[v] + 1
                    q.append(nv)
                if nv == v * 2 and cost[nv] > cost[v]:
                    cost[nv] = cost[v]
                    q.append(nv)
    return cost[end] - 1


print(bfs(N, K))
