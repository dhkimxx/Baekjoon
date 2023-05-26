import math

M, N = int(input()), int(input())
M, N = math.ceil(M ** 0.5), math.floor(N ** 0.5)
ans = []
for i in range(M, N + 1):
    ans.append(i ** 2)
if ans:
    print(sum(ans))
    print(M ** 2)
else:
    print(-1)