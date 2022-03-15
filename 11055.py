import sys
N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
LIS = []
maxSum = A[0]
for i in range(0, N):
    LIS.append([A[i]])
    for j in range(i):
        if A[j] < A[i] and sum(LIS[j]) + A[i] > sum(LIS[i]):
            LIS[i] = LIS[j] + [A[i]]
    sumOfLIS = sum(LIS[i])
    if sumOfLIS > maxSum:
        maxSum = sumOfLIS
        maxLIS = LIS[i]
print(maxSum)