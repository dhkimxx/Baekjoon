import heapq

N = int(input())
a = int(input())
q = []
for _ in range(N-1):
    heapq.heappush(q, -int(input()))
ans = 0
while q:
    tmp = -heapq.heappop(q)
    if a <= tmp:
        ans += 1
        a += 1
        heapq.heappush(q, -(tmp - 1))
print(ans)