import sys
N = int(sys.stdin.readline())
Q = list(sys.stdin.readline().rstrip())
result = 0
for n in range(N):
    result += (ord(Q[n]) - 96) * (31 ** n)
print(result % 1234567891)