import heapq

N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]
inDegree = [0] * (N + 1)
for i in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    inDegree[b] += 1

heap = []
for i in range(1, N + 1):
    if inDegree[i] == 0:
        heapq.heappush(heap, i)

ans = []
while heap:
    now = heapq.heappop(heap)
    ans.append(now)
    for next in graph[now]:
        inDegree[next] -= 1
        if inDegree[next] == 0:
            heapq.heappush(heap, next)

print(*ans)