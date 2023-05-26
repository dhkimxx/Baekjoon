import sys

N = int(sys.stdin.readline())
score = []
for i in range(N):
    score.append(int(sys.stdin.readline()))
dp = [0] * N
dp[0] = score[0]
if N >= 2:
    dp[1] = score[0] + score[1]
if N >= 3:
    for i in range(2, N):
        dp[i] = max(dp[i - 2] + score[i], dp[i - 3] + score[i - 1] + score[i])
print(dp[-1])