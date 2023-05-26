N, K = map(int, input().split())
P = 1000000007
dp = [1] * (N + 1)
for i in range(2, N + 1):
    dp[i] = i * dp[i - 1] % P


def pow(A, B):
    if B == 1:
        return A % P
    if B % 2 == 0:
        return pow(A, B//2) ** 2 % P
    if B % 2 == 1:
        return A * (pow(A, B//2) ** 2) % P


a = dp[N]
b = dp[N - K] * dp[K] % P
print(a * pow(b, P - 2) % P)