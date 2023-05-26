import sys

while 1:
    n, *arr = list(map(int, sys.stdin.readline().split()))
    if n == 0: break
    stack = []
    ans = 0
    arr.append(0)
    for i, h in enumerate(arr):
        while stack and arr[stack[-1]] > h:
            height = arr[stack.pop()]
            if stack:
                width = i - stack[-1] -1
            else:
                width = i
            ans = max(ans, height * width)
        stack.append(i)
    print(ans)