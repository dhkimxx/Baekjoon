import sys
N = int(sys.stdin.readline())
sum = 0
xor = 0
for n in range(N):
    query = list(map(int, sys.stdin.readline().split()))
    if query[0] == 1:
        sum += query[1]
        xor ^= query[1]
    if query[0] == 2:
        sum -= query[1]
        xor ^= query[1]
    if query[0] == 3:
        print(sum)
    if query[0] == 4:
        print(xor)