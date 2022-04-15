import sys
import heapq

input = sys.stdin.readline

N, E = map(int, input().split())
graph = [[] for _ in range(N + 1)]
distance = [[1e9] * (N + 1) for _ in range(N + 1)]
for _ in range(E):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))
v1, v2 = map(int, input().split())


def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start][start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if dist > distance[start][now]:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[start][i[0]]:
                distance[start][i[0]] = cost
                heapq.heappush(q, (cost, i[0]))


for i in [1, v1, v2, N]:
    dijkstra(i)

result = min(distance[1][v1] + distance[v1][v2] + distance[v2][N],
             distance[1][v2] + distance[v2][v1] + distance[v1][N])
if result >= 1e9:
    print(-1)
else:
    print(result)