dp = [1] * 1001
for i in range(2, 1001):
    for j in range(1, i//2 + 1):
        dp[i] += dp[j]
for _ in range(int(input())):
    print(dp[int(input())])
