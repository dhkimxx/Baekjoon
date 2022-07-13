from collections import deque

N, M = int(input()), int(input())
P = list(map(int, input().split()))
ans = 0
for i in range(0, N + 1):
    score = 0
    for p in P:
        xor_sum = sum(list(map(int, bin(p ^ i)[2:])))
        score = min(score, xor_sum)
    ans = max(score, ans)
print(ans)