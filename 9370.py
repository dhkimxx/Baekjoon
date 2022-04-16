import sys
import heapq
input = sys.stdin.readline


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


for _ in range(int(input())):
    N, M, T = map(int, input().split())
    S, G, H = map(int, input().split())
    graph = [[] for _ in range(N + 1)]
    distance = [[1e9] * (N + 1) for _ in range(N + 1)]
    for _ in range(M):
        A, B, D = map(int, input().split())
        graph[A].append((B, D))
        graph[B].append((A, D))
    candidate = []
    for _ in range(T):
        candidate.append(int(input()))
    for start in [S, G, H]:
        dijkstra(start)
    for end in sorted(candidate):
        result = min(distance[S][G] + distance[G][H] + distance[H][end],
                     distance[S][H] + distance[H][G] + distance[G][end])
        if distance[S][end] == result:
            print(end, end=' ')
    print()