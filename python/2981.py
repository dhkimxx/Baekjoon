import math
import sys
N = int(sys.stdin.readline())
arr = [int(input()) for _ in range(N)]
arr.sort()
gap = []
ans = []
for i in range(N - 1):
    gap.append(arr[i + 1] - arr[i])
prev = gap[0]
for i in range(1, len(gap)):
    prev = math.gcd(prev, gap[i])
for i in range(2, int(math.sqrt(prev)) + 1):
    if prev % i == 0:
        ans.append(i)
        ans.append(prev//i)
print(' '.join(map(str, list(set(sorted(ans))) + [prev])))
