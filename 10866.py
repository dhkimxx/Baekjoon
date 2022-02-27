from collections import deque
import sys
N = int(sys.stdin.readline())
deq = deque()
for n in range(N):
    order = list(sys.stdin.readline().split())
    if order[0] == "push_front":
        deq.appendleft(order[1])
    elif order[0] == "push_back":
        deq.append(order[1])
    elif order[0] == "size":
        print(len(deq))
    elif order[0] == "empty":
        if len(deq) == 0:
            print(1)
        else:
            print(0)
    else:
        if len(deq) == 0:
            print(-1)
            continue
        elif order[0] == "pop_front":
            print(deq.popleft())
        elif order[0] == "pop_back":
            print(deq.pop())
        elif order[0] == "front":
            print(deq[0])
        elif order[0] == "back":
            print(deq[-1])
