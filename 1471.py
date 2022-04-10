import sys

sys.setrecursionlimit(100000)

N = int(input())
visited = [False] * (N + 1)
dp = [0] * (N + 1)
stack = []


def nextVertex(n):
    SUM = n
    while n:
        SUM += n % 10
        n //= 10
    if SUM > N:
        SUM -= N
    return SUM


def dfs(v):
    if dp[v]:
        return dp[v]
    if visited[v]:
        cycle = []
        cycleSize = 0
        while 1:
            cycleSize += 1
            cycle.append(stack.pop())
            if cycle[-1] == v:
                break
        for c in cycle:
            dp[c] = cycleSize
        return dp[v]
    visited[v] = True
    stack.append(v)
    temp = dfs(nextVertex(v))
    if dp[v] == 0:
        dp[v] = temp + 1
    return dp[v]


result = 0
for i in range(1, N + 1):
    if visited[i]:
        continue
    result = max(result, dfs(i))
print(result)
