import sys
sys.setrecursionlimit(100001)


def dfs(v, s):
    global result
    visited[v] = 1
    nv = students[v]
    if visited[nv]:
        if nv in s:
            result += s[s.index(nv):]
    else:
        s.append(nv)
        dfs(nv, s)


for _ in range(int(input())):
    N = int(input())
    students = [0] + list(map(int, input().split()))
    visited = [0] * (N + 1)
    result = []
    for n in range(1, N + 1):
        if not visited[n]:
            stack = [n]
            dfs(n, stack)
    print(N - len(result))