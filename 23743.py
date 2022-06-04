import heapq

N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b, c = map(int, input().split())
    graph[a].append((c, b))
    graph[b].append((c, a))
exit_time = [0] + list(map(int, input().split()))
for i in range(1, N + 1):
    graph[0].append((exit_time[i], i))


def prim():
    q = [(0, 0)]
    total_warp_time = 0
    while q:
        cost, now = heapq.heappop(q)
        if not visited[now]:
            visited[now] = 1
            total_warp_time += cost
            for next in graph[now]:
                heapq.heappush(q, (next[0], next[1]))
    return total_warp_time


visited = [0] * (N + 1)
print(prim())
