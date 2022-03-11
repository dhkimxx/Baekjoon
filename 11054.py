import sys
N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
reverseA = list(reversed(A))
length = []
dpLIS = [1] * N
dpLDS = [0] * N
for i in range(0, N):
    for j in range(0, i):
        if A[i] > A[j]:
            dpLIS[i] = max(dpLIS[i], dpLIS[j] + 1)
        if reverseA[i] > reverseA[j]:
            dpLDS[i] = max(dpLDS[i], dpLDS[j] + 1)

dpLDS.reverse()
for i in range(0, N):
    length.append(dpLIS[i] + dpLDS[i])
print(max(length))
'''
import sys
N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
length = []
dpLIS = [1] * N
dpLDS = [0] * N
for i in range(0, N):
    for j in range(0, i):
        if A[i] > A[j]:
            dpLIS[i] = max(dpLIS[i], dpLIS[j] + 1)
        if A[N - 1 - i] > A[N - 1 - j]:
            dpLDS[N - 1 - i] = max(dpLDS[N - 1 - i], dpLDS[N - 1 - j] + 1)
            
for i in range(0, N):
    length.append(dpLIS[i] + dpLDS[i])
print(max(length))
'''
