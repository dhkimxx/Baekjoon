def dfs(now, cnt):
    global res
    if now == 10:
        if cnt >= 5:
            res += 1
        return
    for i in range(1, 6):
        if now >= 2 and sub[now - 1] == sub[now - 2] and sub[now - 1] == i:
            continue
        else:
            sub.append(i)
            if i == answer[now]:
                dfs(now + 1, cnt + 1)
            else:
                dfs(now + 1, cnt)
            sub.pop()


answer = list(map(int, input().split()))
sub = []
res = 0
dfs(0, 0)
print(res)