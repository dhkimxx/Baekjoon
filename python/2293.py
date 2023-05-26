N, K = map(int, input().split())
coin = [int(input()) for _ in range(N)]
ans = 0
dp = [0] * (K + 1)
dp[0] = 1
for c in coin:
    for k in range(c, K + 1):
        dp[k] += dp[k-c]

print(dp)
