n = int(input())
dp = [0, 1] + [0] * (n - 1)
for N in range(2, n + 1):
    dp[N] = dp[N - 1] + dp[N - 2]
print(dp[n])