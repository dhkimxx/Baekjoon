T, W = map(int, input().split())
tree = [int(input()) for _ in range(T)]
dp = [[[0] * 3 for _ in range(W + 1)] for _ in range(T + 1)]
for t in range(1, T + 1):
    if tree[t - 1] == 1:
        dp[t][0][1] = dp[t - 1][0][1] + 1
    else:
        dp[t][0][2] = dp[t - 1][0][2] + 1

    for w in range(1, W + 1):
        if tree[t - 1] == 1:
            dp[t][w][1] = max(dp[t - 1][w - 1][2] + 1, dp[t - 1][w][1] + 1)
            dp[t][w][2] = max(dp[t - 1][w - 1][1], dp[t - 1][w][2])
        else:
            dp[t][w][1] = max(dp[t - 1][w - 1][2], dp[t - 1][w][1])
            dp[t][w][2] = max(dp[t - 1][w - 1][1] + 1, dp[t - 1][w][2] + 1)
print(max(max(map(max, dp))))
