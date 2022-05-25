import heapq

N = int(input())
graph = [[] for _ in range(N + 1)]
for i in range(1, N):
    temp = list(map(int, input().split()))
    for j, cost in enumerate(temp):
        graph[i].append((cost, i + j + 1))
        graph[i + j + 1].append((cost, i))

visited = [False] * (N + 1)
ans = 0
cnt = 0
q = [(0, 1, 0)]

new_graph = [[] for _ in range(N + 1)]
while q and cnt < N:
    cost, now, last = heapq.heappop(q)
    if not visited[now]:
        if last != 0:
            new_graph[now].append(last)
            new_graph[last].append(now)
        visited[now] = True
        cnt += 1
        ans += cost
        for next in graph[now]:
            heapq.heappush(q, (next[0], next[1], now))

for i in range(1, N + 1):
    print(len(new_graph[i]), *sorted(new_graph[i]))