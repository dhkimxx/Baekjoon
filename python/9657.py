N = int(input())
dp = [False] * (N + 1)
for i in range(0, N + 1):
    for j in (i + 1, i + 3, i + 4):
        if not dp[i] and j < N + 1:
            dp[j] = True
if dp[N]:
    print('SK')
else:
    print('CY')
