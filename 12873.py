from collections import deque

N = int(input())
q = deque([i for i in range(1, N + 1)])
ans = 0
t = 1
while q:
    q.rotate(-(t ** 3 - 1))
    ans = q.popleft()
    t += 1
print(ans)