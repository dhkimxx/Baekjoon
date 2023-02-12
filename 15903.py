# n, m = map(int, input().split())
# a = list(map(int, input().split()))
# a.sort()
# for _ in range(m):
#     a[0], a[1] = a[0] + a[1], a[0] + a[1]
#     a.sort()
# print(sum(a))

import heapq

n, m = map(int, input().split())
a = list(map(int, input().split()))
heapq.heapify(a)

for _ in range(m):
    temp = heapq.heappop(a) + heapq.heappop(a)
    heapq.heappush(a, temp)
    heapq.heappush(a, temp)
print(sum(a))