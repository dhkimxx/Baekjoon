import sys
N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
maxLength = 0
maxIndex = 0
LIS = [arr[0]]
dp = [1] * N
for n in range(1, N):
    if LIS[-1] < arr[n]:
        LIS.append(arr[n])
        dp[n] = len(LIS)
    else:
        start = 0
        end = len(LIS) - 1
        index = 0
        while end - start >= 0:
            mid = (start + end) // 2
            if LIS[mid] < arr[n]:
                index = mid + 1
                start = mid + 1
            else:
                end = mid - 1
        LIS[index] = arr[n]
        dp[n] = max(dp[n], dp[index])
    if maxLength < len(LIS):
        maxLength = len(LIS)
        maxIndex = n
    print(dp[n], LIS)

result = []
for j in range(maxIndex, -1, -1):
    if dp[maxIndex] == dp[j] + 1 and arr[maxIndex] > arr[j]:
        result.append(arr[j])
        maxIndex = j
print(result)
print(len(LIS),dp)