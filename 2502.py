D, K = map(int, input().split())
dpA = [0] * (D + 1)
dpB = [0] * (D + 1)

dpA[1], dpB[1] = 1, 0
dpA[2], dpB[2] = 0, 1
for i in range(3, D + 1):
    dpA[i] = dpA[i - 1] + dpA[i - 2]
    dpB[i] = dpB[i - 1] + dpB[i - 2]

for i in range(1, 100000):
    if (K - dpA[D] * i) % dpB[D] == 0:
        print(i)
        print((K - dpA[D] * i) // dpB[D])
        break

# dp[1] = a
# dp[2] = b
# dp[3] = a + b
# dp[4] = a + 2 * b
# dp[5] = 2 * a + 3 * b
# dp[6] = 3 * a + 5 * b
