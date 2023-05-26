N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
dp = [[0] * M for _ in range(N)]

for i in range(N):
    for j in range(M):
        if dp[i][j] == 0:
            dp[i][j] = graph[i][j]
        if i + 1 < N:
            dp[i + 1][j] = max(dp[i + 1][j], dp[i][j] + graph[i + 1][j])
        if j + 1 < M:
            dp[i][j + 1] = max(dp[i][j + 1], dp[i][j] + graph[i][j + 1])
        if i + 1 < N and j + 1 < M:
            dp[i + 1][j + 1] = max(dp[i + 1][j + 1], dp[i][j] + graph[i + 1][j + 1])

print(dp[N - 1][M - 1])