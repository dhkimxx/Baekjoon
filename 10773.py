import sys
K = int(sys.stdin.readline())
stack = []
for k in range(K):
    n = int(sys.stdin.readline())
    if n == 0:
        stack.pop()
    else:
        stack.append(n)
print(sum(stack))