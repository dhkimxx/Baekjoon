import sys
N = int(sys.stdin.readline())
score = []
for i in range(N):
    score.append(int(sys.stdin.readline()))
dp = [0] * N
for i in range(N):
    point = 0
    for j in range(i):
