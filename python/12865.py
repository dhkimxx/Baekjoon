N, K = map(int, input().split())
weight = [0]
value = [0]
dp = [[0] * (K + 1) for _ in range(N + 1)]
for i in range(N):
    W, V = map(int, input().split())
    weight.append(W)
    value.append(V)

for i in range(1, N + 1):
    for j in range(1, K + 1):
        if weight[i] <= j:
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - weight[i]] + value[i])
        else:
            dp[i][j] = dp[i - 1][j]

print(dp[-1][-1])
