N = int(input())
dp = [0] * (N + 1)
dp[0] = 1
dp[1] = 1
for i in range(2, N + 1):
    dp[i] = dp[i - 1] + dp[i - 2]

ans = 1
start = 1
for _ in range(int(input())):
    vip = int(input())
    ans = ans * dp[vip - start]
    start = vip + 1
ans = ans * dp[N + 1 - start]
print(ans)
