from collections import deque
N, K = map(int, input().split())
INF = 500001
visited = [0] * INF
def bfs():
    q = deque([(N, K, 0)])
    visited[N] = 1
    while q:
        v, target, timer = q.popleft()
        if v == target:
            return timer
        for nv in [v - 1, v + 1, 2 * v]:
            next_timer = timer + 1
            next_target = target + next_timer
            if 0 <= nv < INF and 0 <= next_target < INF and not visited[nv]:
                visited[nv] = 1

    return -1
print(bfs())