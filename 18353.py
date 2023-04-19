N = int(input())
a = [0] + list(map(int, input().split()))
dp = [0] * (N + 1)

for i in range(1, N + 1):
    dp[i] = 1
    for j in range(1, i):
        if a[i] < a[j]:
            dp[i] = max(dp[i], dp[j] + 1)
print(N - max(dp))