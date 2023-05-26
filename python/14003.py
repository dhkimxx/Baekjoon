import sys
N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
LIS = [A[0]]
DP = [1]*N
maxDP = 0
maxDP_idx = 0
for n in range(1, N):
    if LIS[-1] < A[n]:
        LIS.append(A[n])
        DP[n] = len(LIS)
    else:
        start = 0
        end = len(LIS) - 1
        LIS_idx = 0
        while end - start >= 0:
            mid = (start + end) // 2
            if LIS[mid] < A[n]:
                LIS_idx = mid + 1
                start = mid + 1
            else:
                end = mid - 1
        LIS[LIS_idx] = A[n]
        DP[n] = LIS_idx + 1
    if DP[n] > maxDP:
        maxDP_idx = n
        maxDP = DP[n]

print(len(LIS))

resultLIS = [A[maxDP_idx]]
for n in range(maxDP_idx, -1, -1):
    if DP[n] == DP[maxDP_idx] - 1 and A[n] < A[maxDP_idx]:
        resultLIS.append(A[n])
        maxDP_idx = n

print(' '.join(map(str, reversed(resultLIS))))