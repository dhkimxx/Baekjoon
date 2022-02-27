from collections import deque
import sys

T = int(sys.stdin.readline())
for t in range(T):
    method = list(sys.stdin.readline().rstrip())
    N = int(sys.stdin.readline())
    deq = deque(sys.stdin.readline().rstrip().strip(']').strip('[').split(','))
    reverseCounter = 0
    deleteCounter = 0
    result = ''
    for m in method:
        if m == 'R':
            reverseCounter += 1
        elif m == 'D':
            if deq == deque([]) or deq == deque(['']):
                result = 'error'
            else:
                if reverseCounter % 2 == 1:
                    deq.pop()
                else:
                    deq.popleft()
    if reverseCounter % 2 == 1:
        deq.reverse()
    if result != 'error':
        result = '[' + ','.join(deq) + ']'
    print(result)
