N = int(input())
towers = list(map(int, input().split()))
stack = []
ans = []
for i in range(len(towers)):
    while stack:
        if stack[-1][1] < towers[i]:
            stack.pop()
        else:
            ans.append(stack[-1][0] + 1)
            stack.append([i, towers[i]])
            break
    if not stack:
        ans.append(0)
        stack.append([i, towers[i]])
print(*ans)