K, N = map(int, input().split())
arr = [0] + list(map(int, input().split()))
for i in range(1, K + 1):
    arr[i] = arr[i - 1] + arr[i]
max = -1e9
for i in range(0, K - N + 1):
    if max < arr[i + N] - arr[i]:
        max = arr[i + N] - arr[i]
print(max)