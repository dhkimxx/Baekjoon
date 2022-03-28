import sys
import math

T = int(sys.stdin.readline())
for t in range(T):
    N = int(sys.stdin.readline())
    if N % 2:
        print(0)
        continue
    arr = []
    for n in range(1, N + 1):
        arr.append(n)
