N = int(input())
wine = []
dp = [0] * N
for i in range(N):
    wine.append(int(input()))
if N == 1 or N == 2:
    print(sum(wine))
if N >= 3:
    dp[0] = wine[0]
    dp[1] = wine[0] + wine[1]
    dp[2] = max(wine[0] + wine[1], wine[1] + wine[2], wine[0] + wine[2])
    if N == 3:
        print(dp[2])
    else:
        for i in range(3, N):
            dp[i] = max(dp[i - 1], wine[i] + dp[i - 2], wine[i] + wine[i - 1] + dp[i - 3])
        print(dp[-1])