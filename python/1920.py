import sys

N = int(sys.stdin.readline())
A = sorted(list(map(int, sys.stdin.readline().split())))
M = int(sys.stdin.readline())
B = list(map(int, sys.stdin.readline().split()))

for m in range(M):
    start = 0
    end = N - 1
    mid = (start + end) // 2
    result = 0
    while end - start >= 0:
        if A[mid] == B[m]:
            result = 1
            break
        elif A[mid] < B[m]:
            start = mid + 1
        elif A[mid] > B[m]:
            end = mid - 1
        mid = (start + end) // 2
    print(result)