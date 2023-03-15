N, K = map(int, input().split())
coin = list(int(input()) for _ in range(N))
coin.sort()
dp = [1e6] * (K + 1)
for c in coin:
    if c > K:
        continue
    dp[c] = 1
    for j in range(c + 1, K + 1):
        dp[j] = min(dp[j], dp[j - c] + 1)
if dp[K] != 1e6:
    print(dp[K])
else:
    print(-1)