import sys
sys.setrecursionlimit(10000)

N = int(sys.stdin.readline())
nextVertex = [0] * (N + 1)
dp = [0] * (N + 1)
cs = -2

def numSum(n):
    numberSum = 0
    while n != 0:
        numberSum += n % 10
        n = n // 10
    return numberSum


for i in range(1, N + 1):
    nextVertex[i] = i + numSum(i)
    if nextVertex[i] > N:
        nextVertex[i] -= N


def go(v):
    global cs
    if dp[v]:
        return dp[v]
    if visited[v]:
        cs = v
        return 0
    visited[v] = True
    ans = go(nextVertex[v]) + 1
    dp[v] = ans
    if cs >= 0:
        stack.append(v)
    if cs == v:
        cs = -1
    return dp[v]

result = 0
for i in range(1, N + 1):
    visited = [False] * (N + 1)
    stack = []
    temp = go(i)
    if cs == -1:
        for j in range(0, len(stack)):
            dp[stack[j]] = len(stack)
        cs = -2
    result = max(result, temp)

print(result)
