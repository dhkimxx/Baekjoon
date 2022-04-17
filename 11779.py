import sys
input = sys.stdin.readline
import heapq

N, M = int(input()), int(input())
graph = [[] for _ in range(N + 1)]
distance = [1e9] * (N + 1)
parent = [0] * (N + 1)

for _ in range(M):
    a, b, c = map(int, input().split())
    graph[a].append([b, c])
    parent[b] = a
start, end = map(int, input().split())


def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if dist > distance[now]:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))
                parent[i[0]] = now


dijkstra(start)
route = [end]
now = end
while now != start:
    now = parent[now]
    route.append(now)
print(distance[end])
print(len(route))
print(' '.join(map(str, reversed(route))))
# import sys
# input = sys.stdin.readline
# import heapq
#
# N, M = int(input()), int(input())
# graph = [[] for _ in range(N + 1)]
# distance = [1e9] * (N + 1)
#
# for _ in range(M):
#     a, b, c = map(int, input().split())
#     graph[a].append([b, c])
#
# start, end = map(int, input().split())
# route = [[] for _ in range(N + 1)]
# route[start].append(start)
#
#
# def dijkstra(start):
#     q = []
#     heapq.heappush(q, (0, start))
#     distance[start] = 0
#     while q:
#         dist, now = heapq.heappop(q)
#         if dist > distance[now]:
#             continue
#         for i in graph[now]:
#             cost = dist + i[1]
#             if cost < distance[i[0]]:
#                 distance[i[0]] = cost
#                 heapq.heappush(q, (cost, i[0]))
#                 route[i[0]] = route[now] + [i[0]]
#
#
# dijkstra(start)
# print(distance[end])
# print(len(route[end]))
# print(' '.join(map(str, route[end])))
