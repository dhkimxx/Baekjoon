for _ in range(int(input())):
    N, M, W = map(int, input().split())
    INF = int(1e9)
    graph = [[INF] * (N + 1) for _ in range(N + 1)]
    distance = [INF] * (N + 1)
    for _ in range(M):
        S, E, T = map(int, input().split())
        graph[S][E] = min(graph[S][E], T)
        graph[E][S] = min(graph[E][S], T)
    for _ in range(W):
        S, E, T = map(int, input().split())
        graph[S][E] = min(graph[S][E], -T)

    def bf():
        for k in range(1, N + 1):
            for i in range(1, N + 1):
                for j in range(1, N + 1):
                    if distance[j] == INF and graph[i][j] != INF:
                        distance[j] = graph[i][j]
                    if distance[j] > distance[i] + graph[i][j]:
                        distance[j] = distance[i] + graph[i][j]
                        if k == N:
                            return 1
        return 0

    if bf():
        print('YES')
    else:
        print('NO')