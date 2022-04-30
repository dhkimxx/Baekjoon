import sys
from collections import deque
while 1:
    arr = list(map(int, sys.stdin.readline().split()))
    if arr[0] == 0:
        break
    stack = deque()
    max_size = 0
    last_size = 0
    for i in range(1, arr[0] + 1):
        stack.append(arr[i])
        if last_size < len(stack) * min(stack):
            stack = deque([])
        if len(stack) * min(stack) < last_size:
            max_size = last_size
        last_size = len(stack) * min(stack)
        print('len:', len(stack), 'size:', len(stack) * min(stack), stack)
    print(arr[1:])
