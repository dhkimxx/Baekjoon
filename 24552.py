from collections import deque
import sys

S = list(sys.stdin.readline().rstrip())
stack = deque()
left = 0
right = 0
for s in S:
    if s == '(':
        left += 1
        stack.append(s)
    if s == ')':
        right += 1
        if len(stack) > 0: stack.pop()
    print(stack, len(stack))
print(f"(: {left}  ): {right}")
