N, K = map(int, input().split())
P = 1000000007
factorial = [1] * (N + 1)
for i in range(1, N + 1):
    factorial[i] = i * factorial[i - 1] % P
A = factorial[N] % P
B = (factorial[K] * factorial[N - K]) % P
print(A % B)