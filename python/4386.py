import heapq

N = int(input())
xy = []
for n in range(N):
    x, y = map(float, input().split())
    xy.append([x, y])

graph = [[] for _ in range(N)]
for i in range(N):
    for j in range(i + 1, N):
        cost = ((xy[i][0] - xy[j][0]) ** 2 + (xy[i][1] - xy[j][1]) ** 2) ** 0.5
        graph[i].append((cost, j))
        graph[j].append((cost, i))

q = [(0, 0)]
visited = [0] * N
ans = 0
while q:
    cost, now = heapq.heappop(q)
    if not visited[now]:
        visited[now] = 1
        ans += cost
        for next in graph[now]:
            heapq.heappush(q, (next[0], next[1]))
print(round(ans, 2))