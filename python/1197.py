import heapq
import sys
input = sys.stdin.readline

V, E = map(int, input().split())
visited = [False] * (V + 1)
graph = [[] for _ in range(V + 1)]
q = [(0, 1)]
for _ in range(E):
    A, B, C = map(int, input().split())
    graph[A].append((C, B))
    graph[B].append((C, A))

cnt = 0
ans = 0
while q:
    if cnt == V:
        break
    cost, now = heapq.heappop(q)
    if not visited[now]:
        visited[now] = True
        ans += cost
        cnt += 1
        for next in graph[now]:
            heapq.heappush(q, (next[0], next[1]))
print(ans)