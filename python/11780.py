import sys
input = sys.stdin.readline

N, M = int(input()), int(input())
graph = [[1e9] * (N + 1) for _ in range(N + 1)]
route = [[[] for _ in range(N + 1)] for _ in range(N + 1)]

for _ in range(M):
    a, b, c = map(int, input().split())
    if graph[a][b] > c:
        graph[a][b] = c
        route[a][b] = [a, b]

for k in range(1, N + 1):
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            if k == i or i == j or k == j:
                continue
            if graph[i][j] > graph[i][k] + graph[k][j]:
                graph[i][j] = graph[i][k] + graph[k][j]
                route[i][j] = route[i][k][:-1] + route[k][j]

for i in range(1, N + 1):
    for j in range(1, N + 1):
        if graph[i][j] == 1e9:
            print(0, end=' ')
        else:
            print(graph[i][j], end=' ')
    print()

for i in range(1, N + 1):
    for j in range(1, N + 1):
        if len(route[i][j]) == 0:
            print(0)
        else:
            print(len(route[i][j]), end=' ')
            print(' '.join(map(str, route[i][j])))

# import sys
# input = sys.stdin.readline
#
# N, M = int(input()), int(input())
# graph = [[1e9] * (N + 1) for _ in range(N + 1)]
# preCity = [[0] * (N + 1) for _ in range(N + 1)]
#
# for _ in range(M):
#     a, b, c = map(int, input().split())
#     if graph[a][b] > c:
#         graph[a][b] = c
#         preCity[a][b] = a
#
# for k in range(1, N + 1):
#     for i in range(1, N + 1):
#         for j in range(1, N + 1):
#             if k == i or i == j or k == j:
#                 continue
#             if graph[i][j] > graph[i][k] + graph[k][j]:
#                 graph[i][j] = graph[i][k] + graph[k][j]
#                 preCity[i][j] = preCity[k][j]
#
# for i in range(1, N + 1):
#     for j in range(1, N + 1):
#         if graph[i][j] == 1e9:
#             print(0, end=' ')
#         else:
#             print(graph[i][j], end=' ')
#     print()
#
# for i in range(1, N + 1):
#     for j in range(1, N + 1):
#         if graph[i][j] == 1e9:
#             print(0)
#         else:
#             route = [j]
#             now = j
#             while now != i:
#                 now = preCity[i][now]
#                 route.append(now)
#             print(len(route), ' '.join(map(str, reversed(route))))