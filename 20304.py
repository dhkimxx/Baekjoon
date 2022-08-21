from collections import deque

N = int(input())
M = int(input())
P = list(map(int, input().split()))

safety = [21 for _ in range(N + 1)]
q = deque()

for p in P:
    safety[p] = 0
    q.append(p)

ans = 0

while q:
    cur = q.popleft()
    for i in range(20):
        x = (1 << i) ^ cur
        if x <= N and safety[cur] + 1 < safety[x]:
            safety[x] = safety[cur] + 1
            ans = max(safety[x], ans)
            q.append(x)
print(ans)
