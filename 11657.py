import sys

input = sys.stdin.readline
N, M = map(int, input().split())
edges = []
distance = [1e9] * (N + 1)
for _ in range(M):
    a, b, c = map(int, input().split())
    edges.append((a, b, c))


def bf(start):
    distance[start] = 0
    for i in range(N):
        for j in range(M):
            v = edges[j][0]
            nv = edges[j][1]
            cost = edges[j][2]
            if distance[v] != 1e9 and distance[nv] > distance[v] + cost:
                distance[nv] = distance[v] + cost
                if i == N - 1:
                    print(-1)
                    return 0
    return 1


if bf(1):
    for i in range(2, N + 1):
        if distance[i] != 1e9:
            print(distance[i])
        else:
            print(-1)