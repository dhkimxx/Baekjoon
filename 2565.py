import sys

N = int(sys.stdin.readline())
A = [0] * 500
LIS = [1] * 500
for n in range(N):
    a, b = map(int, sys.stdin.readline().split())
    A[a - 1] = b
for i in range(0, 500):
    for j in range(0, i):
        if A[i] > A[j] != 0:
            LIS[i] = max(LIS[j] + 1, LIS[i])
print(N - max(LIS))