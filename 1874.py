from collections import deque
import sys

N = int(sys.stdin.readline())
que = deque()
for n in range(1, N + 1):
    que.append(n)
stack = deque()
result = deque()
for n in range(1, N + 1):
    target = int(sys.stdin.readline())
    while len(que) != 0 and que[0] <= target:
        stack.append(que.popleft())
        result.append('+')
    print(que, stack)
    if target < max(stack):
        print('NO')
        sys.exit()
    stack.pop()
    result.append('-')
for r in result:
    print(r)

