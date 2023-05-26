import sys
N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
LIS = [arr[0]]
for n in range(1, N):
    if LIS[-1] < arr[n]:
        LIS.append(arr[n])
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
print(len(LIS))