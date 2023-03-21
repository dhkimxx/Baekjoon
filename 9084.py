for _ in range(int(input())):
    N = int(input())
    coin = list(map(int, input().split()))
    M = int(input())

    dp = [0] * (M + 1)
    dp[0] = 1
    for c in coin:
        for m in range(1, M + 1):
            if c <= m:
                dp[m] += dp[m - c]
    print(dp[M])
