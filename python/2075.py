import heapq
N = int(input())
q = []
for i in range(N):
    for j in list(map(int, input().split())):
        if len(q) < N:
            heapq.heappush(q, j)
        else:
            heapq.heapreplace(q, j) #heapq.heappushpop(q, j)
print(heapq.heappop(q))
