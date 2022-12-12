import heapq
N, M = map(int, input().split())
C = list(map(int, input().split()))
W = list(map(int, input().split()))

q = []
for c in C:
    heapq.heappush(q, -c)

for w in W:
    now = -heapq.heappop(q)
    if now < w:
        print(0)
        exit()
    else:
        heapq.heappush(q, -(now - w))
print(1)
