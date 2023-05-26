def dfs(level, sub):
    if len(sub) == 6:
        print(*sub)
        return
    if level == k:
        return

    sub.append(li[level])
    dfs(level + 1, sub)
    sub.pop()
    dfs(level + 1, sub)


while 1:
    k, *li = map(int, input().split())
    if k == 0:
        exit()
    dfs(0, [])
    print()
