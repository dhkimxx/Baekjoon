from collections import deque
N, M = int(input()), int(input())
P = list(map(int, input().split()))
safety = [21] * (N + 1)
q = deque()
for p in P:
    safety[p] = 0
    q.append(p)
while q:
    cur = q.popleft()
    for i in range(20):
        x = (1 << i) ^ cur
        if x <= N and safety[cur] + 1 < safety[x]:
            safety[x] = safety[cur] + 1
            q.append(x)
print(max(safety))
