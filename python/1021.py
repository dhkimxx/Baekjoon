from collections import deque
import sys
N, M = map(int, sys.stdin.readline().split())
Que = deque()
for n in range(1, N + 1):
    Que.append(n)
target = deque(map(int, sys.stdin.readline().split()))
count = 0
while len(target) > 0:
    if Que[0] == target[0]:
        Que.popleft()
        target.popleft()
    elif Que.index(target[0]) <= len(Que) // 2:
        Que.rotate(-1)
        count += 1
    else:
        Que.rotate(1)
        count += 1
print(count)
