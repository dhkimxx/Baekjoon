import sys
import heapq

N = int(sys.stdin.readline())
heap = []
A = []
LIS = [1] * N
for n in range(N):
    a, b = map(int, sys.stdin.readline().split())
    heapq.heappush(heap,(a, b))
for n in range(N):
    A.append(heapq.heappop(heap)[1])


for i in range(0, N):
    for j in range(0, i):
        if A[i] > A[j]:
            LIS[i] = max(LIS[j] + 1, LIS[i])
print(N - max(LIS))