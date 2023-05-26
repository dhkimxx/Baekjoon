from collections import deque
import sys
N = int(sys.stdin.readline())
for i in range(N):
    Q = list(sys.stdin.readline())[:-1]
    stack = deque()
    for q in Q:
        if q == '(':
            stack.append('(')
        if q == ')':
            if len(stack) != 0:
                stack.pop()
            else:
                result = "NO"
                break
        if len(stack) != 0:
            result = "NO"
        else:
            result = "YES"
    print(result)