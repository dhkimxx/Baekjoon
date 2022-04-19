import sys
N, M = map(int, sys.stdin.readline().split())
arr = [0] + list(map(int, sys.stdin.readline().split()))
remain = [0] * M
remain[0] = 1
for i in range(1, N + 1):
    arr[i] = (arr[i] + arr[i - 1]) % M
    remain[arr[i]] += 1
result = 0
for i in range(0, M):
    result += remain[i] * (remain[i] - 1) // 2
print(result)