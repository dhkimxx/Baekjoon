N = int(input())
p = 15 * 100000
dp = [1] * p
for i in range(3, p):
    dp[i] = (dp[i - 1] + dp[i - 2]) % 1000000
print(dp[N%p])