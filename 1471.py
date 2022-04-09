import sys

sys.setrecursionlimit(100000)


def numSum(n):
    numberSum = 0
    while n != 0:
        numberSum += n % 10
        n = n // 10
    return numberSum


def dfs(v):
    global count
    if visited[v]:
        return
    visited[v] = True
    stack.append(v)
    count += 1
    if dp[nextVertex[v]] != 0:
        count += dp[nextVertex[v]]
        return
    dfs(nextVertex[v])


N = int(sys.stdin.readline())
nextVertex = [0] * (N + 1)
dp = [0] * (N + 1)

for i in range(1, N + 1):
    nextVertex[i] = i + numSum(i)
    if nextVertex[i] > N:
        nextVertex[i] -= N

result = 0
for i in range(1, N + 1):
    if dp[i] != 0:
        continue
    visited = [0] * (N + 1)
    stack = []
    count = 0
    dfs(i)
    print(*stack)
    dp[i] = count
    result = max(count, result)
    for s in stack[1:]:
        dp[s] = count - 1

print(result)