import sys
import heapq
input = sys.stdin.readline

N = int(input())
visited = [False] * (N + 1)
graph = [[] for _ in range(N + 1)]
q = [(0, 1)]
for _ in range(int(input())):
    a, b, c = map(int, input().split())
    graph[a].append((c, b))
    graph[b].append((c, a))

ans = 0
cnt = 0
while q and cnt < N:
    cost, now = heapq.heappop(q)
    if not visited[now]:
        visited[now] = True
        ans += cost
        cnt += 1
        for next in graph[now]:
            heapq.heappush(q, (next[0], next[1]))
print(ans)