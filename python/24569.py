N = int(input())
player = [0] * N
for n in range(N):
    if int(input()) * 5 - int(input()) * 3 > 40:
        player[n] = 1
print(sum(player), end='')
if sum(player) == N:
    print('+')