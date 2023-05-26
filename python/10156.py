N, K, M = map(int, input().split())
if N * K <= M:
    print(0)
else:
    print(N * K - M)