def factorial(n):
    result = 1
    for i in range(2, n + 1):
        result = i * result
    return result


for _ in range(int(input())):
    N, M = map(int, input().split())
    print(factorial(M) // (factorial(N) * factorial(M - N)))