import sys

T = int(sys.stdin.readline())
for t in range(T):
    N = int(sys.stdin.readline())
    beauty = [0] * 11
    for n in range(N):
        temp = list(map(int, sys.stdin.readline().split()))
        beauty[temp[1]] = max(beauty[temp[1]], temp[0])
    if min(beauty[1:]) == 0:
        print('MOREPROBLEMS')
    else:
        print(sum(beauty))