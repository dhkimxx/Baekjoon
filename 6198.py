N = int(input())
height = [int(input()) for _ in range(N)]
count = [0] * N
stack = []
for i in range(N - 1, -1, -1):
    while stack:
        if stack[-1][1] < height[i]:
            stack.pop()
        else:
            count[i] = stack[-1][0] - i - 1
            stack.append([i, height[i]])
            break
    if not stack:
        count[i] = N - i - 1
        stack.append([i, height[i]])
print(sum(count))