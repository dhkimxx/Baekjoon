import sys
N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
LIS = []
maxLength = 0
for i in range(0, N):
    LIS.append([A[i]])
    for j in range(0, i):
        if A[i] > A[j] and len(LIS[i]) < len(LIS[j]) + 1:
            LIS[i] = LIS[j] + [A[i]]
    if len(LIS[i]) > maxLength:
        maxLengthLIS = LIS[i]
        maxLength = len(LIS[i])
print(maxLength)
for lis in maxLengthLIS:
    print(lis, end=" ")