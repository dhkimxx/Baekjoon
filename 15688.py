import sys
N = int(sys.stdin.readline())
A = []
for n in range(N):
    A.append(int(sys.stdin.readline()))
for a in sorted(A):
    print(a)