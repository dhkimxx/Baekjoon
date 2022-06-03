from collections import deque

N = int(input())
time = [0] * (N + 1)
graph = [[] for _ in range(N + 1)]
inDegree = [0] * (N + 1)
result = [0] * (N + 1)

for a in range(1, N + 1):
    t, pre_n, *pre = map(int, input().split())
    time[a] = t
    inDegree[a] += pre_n
    for b in pre:
        graph[b].append(a)

q = deque()
for i in range(1, N + 1):
    if inDegree[i] == 0:
        q.append(i)
        result[i] = time[i]

ans = 0
while q:
    now = q.popleft()
    ans = max(ans, result[now])
    for next in graph[now]:
        inDegree[next] -= 1
        result[next] = max(result[next], result[now] + time[next])
        if inDegree[next] == 0:
            q.append(next)
print(ans)
