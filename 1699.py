N = int(input())
dp = [1e9] * (N + 1)

for i in range(1, N + 1):
    if i ** 2 <= N:
        dp[i ** 2] = 1
    for j in range(1, N // (i ** 2) + 1):
        dp[(i ** 2) * j] = j
    for j in range(i ** 2 + 1, N + 1):
        dp[j] = min(dp[j], dp[j - (i ** 2)] + dp[i ** 2])
print(dp[N])