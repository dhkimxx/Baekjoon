dp = [0] * 1000001
dp[0] = 1
dp[1] = 1
dp[2] = 2
dp[3] = 4
for n in range(4, 1000001):
    for i in range(1, 4):
        dp[n] += dp[n - i] % 1000000009

for _ in range(int(input())):
    N = int(input())
    print(dp[N] % 1000000009)