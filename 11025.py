N, K = map(int, input().split())
result = 1
for n in range(2, N + 1):
    if (result + K) % n == 0:
        result = n
    elif result + K > n:
        result = (result + K) % n
    else:
        result = result + K
print(result)
