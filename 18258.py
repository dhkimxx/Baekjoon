from collections import deque
import sys

queue = deque()
N = int(sys.stdin.readline())
for n in range(N):
    order = list(sys.stdin.readline().split())
    if order[0] == 'push':
        queue.append(order[1])

    if order[0] == 'pop':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue.popleft())

    if order[0] == 'size':
        print(len(queue))

    if order[0] == 'empty':
        if len(queue) == 0:
            print(1)
        else:
            print(0)

    if order[0] == 'front':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[0])

    if order[0] == 'back':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[-1])