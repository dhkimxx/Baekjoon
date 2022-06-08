def factorial(N):
    result = 1
    for n in range(2, N + 1):
        result *= n
    return result


N, K = map(int, input().split())
print(factorial(N) // (factorial(N - K) * factorial(K)) % 10007)