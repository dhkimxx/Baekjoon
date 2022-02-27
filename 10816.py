import sys

N = int(sys.stdin.readline())
C_N = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())
C_M = list(map(int, sys.stdin.readline().split()))

dic = {}
for c_n in C_N:
    if c_n in dic:
        dic[c_n] += 1
    else:
        dic[c_n] = 1
for c_m in C_M:
    if c_m in dic:
        print(dic[c_m], end=' ')
    else:
        print(0, end=' ')
