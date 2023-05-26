import heapq

N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]
graph.append(list(map(int, input().split())))
visited = [0] * (N + 1)
q = [(0, N)]
ans = 0
while q:
    cost, now = heapq.heappop(q)
    if not visited[now]:
        visited[now] = 1
        ans += cost
        for next in range(0, N):
            heapq.heappush(q, (graph[now][next], next))
print(ans)