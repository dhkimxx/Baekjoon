import heapq

N, P = map(int, input().split())
visit_cost = [1e9] + [int(input()) for _ in range(N)]
graph = [[] for _ in range(N + 1)]
for _ in range(P):
    S, E, L = map(int, input().split())
    graph[S].append((L * 2 + visit_cost[E] + visit_cost[S], E))
    graph[E].append((L * 2 + visit_cost[E] + visit_cost[S], S))

visited = [False] * (N + 1)
q = [(0, 1)]
cnt = 0
ans = min(visit_cost)
while q:
    cost, now = heapq.heappop(q)
    if not visited[now]:
        visited[now] = True
        cnt += 1
        ans += cost
        for next in graph[now]:
            heapq.heappush(q, (next[0], next[1]))
print(ans)