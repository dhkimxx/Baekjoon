import heapq

N, M = map(int, input().split())
q = []
for _ in range(M):
    city, cost = map(int, input().split())
    heapq.heappush(q, (cost, city))
B = [0] + list(map(int, input().split()))
visited = [0] * (N + 1)
ans = 0
while q:
    cost, now = heapq.heappop(q)
    if 1 <= now <= N:
        if not visited[now]:
            visited[now] = 1
            ans += cost
            heapq.heappush(q, (B[now], now + 1))
            heapq.heappush(q, (B[now - 1], now - 1))
            if now == 1:
                heapq.heappush(q, (B[N], N))
            if now == N:
                heapq.heappush(q, (B[N], 1))
print(ans)
