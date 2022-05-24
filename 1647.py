import sys
import heapq
input = sys.stdin.readline

N, M = map(int, input().split())
visited = [False] * (N + 1)
graph = [[] for _ in range(N + 1)]
for _ in range(M):
    A, B, C = map(int, input().split())
    graph[A].append((C, B))
    graph[B].append((C, A))

total_cost = 0
max_cost = 0
cnt = 0
q = [(0, 1)]
while q and cnt < N:
    cost, now = heapq.heappop(q)
    if not visited[now]:
        visited[now] = True
        total_cost += cost
        max_cost = max(max_cost, cost)
        cnt += 1
        for next in graph[now]:
            heapq.heappush(q, (next[0], next[1]))
print(total_cost - max_cost)