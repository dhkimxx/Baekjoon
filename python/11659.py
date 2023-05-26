import sys
input = sys.stdin.readline
N, M = map(int, input().split())
arr = [0] + list(map(int, input().split()))
for n in range(1, N + 1):
    arr[n] = arr[n - 1] + arr[n]
for m in range(M):
    i, j = map(int, input().split())
    print(arr[j] - arr[i - 1])